from pathlib import Path
from bs4 import BeautifulSoup
import csv
import sys
from urllib.parse import urlparse


def is_internal_link(href):
    if not href:
        return False

    href = href.strip()

    if href.startswith("#"):
        return False

    if href.startswith(("mailto:", "tel:", "sms:", "javascript:")):
        return False

    parsed = urlparse(href)

    if parsed.scheme in ("http", "https"):
        return False

    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/internal_link_report.py /path/to/site")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    output = Path("internal_link_report.csv")

    rows = []

    for path in root.rglob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(html, "lxml")

        for a in soup.find_all("a"):
            href = a.get("href", "").strip()
            text = a.get_text(" ", strip=True)

            if is_internal_link(href):
                rows.append({
                    "source_file": str(path.relative_to(root)),
                    "link_text": text,
                    "href": href,
                })

    with output.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["source_file", "link_text", "href"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Found {len(rows)} internal links")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
