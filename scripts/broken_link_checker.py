from pathlib import Path
from bs4 import BeautifulSoup
import csv
import sys
from urllib.parse import urlparse, unquote

IGNORE_PREFIXES = ("mailto:", "tel:", "sms:", "javascript:", "#")


def clean_href(href):
    href = href.strip()
    href = href.split("#")[0]
    href = href.split("?")[0]
    return unquote(href)


def local_target_exists(root, current_file, href):
    href = clean_href(href)

    if not href:
        return True

    if href.startswith(IGNORE_PREFIXES):
        return True

    parsed = urlparse(href)

    if parsed.scheme in ("http", "https"):
        return True

    if href.startswith("/"):
        target = root / href.lstrip("/")
    else:
        target = current_file.parent / href

    if target.is_dir():
        return (target / "index.html").exists() or (target / "index.php").exists()

    if target.exists():
        return True

    if target.suffix == "":
        return (
            target.with_suffix(".html").exists()
            or target.with_suffix(".php").exists()
            or (target / "index.html").exists()
            or (target / "index.php").exists()
        )

    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/broken_link_checker.py /path/to/site")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    output = Path("broken_link_report.csv")

    rows = []

    for path in root.rglob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(html, "lxml")

        for a in soup.find_all("a"):
            href = a.get("href", "").strip()

            if not href or href.startswith(IGNORE_PREFIXES):
                continue

            exists = local_target_exists(root, path, href)

            if not exists:
                rows.append({
                    "source_file": str(path.relative_to(root)),
                    "href": href,
                    "link_text": a.get_text(" ", strip=True),
                })

    with output.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["source_file", "href", "link_text"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Broken internal links found: {len(rows)}")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
