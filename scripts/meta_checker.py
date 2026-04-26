```python
from pathlib import Path
from bs4 import BeautifulSoup
import csv
import sys


def get_text(tag):
    return tag.get_text(" ", strip=True) if tag else ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/meta_checker.py /path/to/site")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    output = Path("meta_report.csv")

    rows = []

    for path in root.rglob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(html, "lxml")

        title = soup.find("title")
        desc = soup.find("meta", attrs={"name": "description"})
        canonical = soup.find("link", rel="canonical")
        h1s = soup.find_all("h1")

        title_text = get_text(title)
        desc_text = desc.get("content", "").strip() if desc else ""
        canonical_href = canonical.get("href", "").strip() if canonical else ""

        rows.append({
            "file": str(path.relative_to(root)),
            "title": title_text,
            "title_length": len(title_text),
            "meta_description": desc_text,
            "description_length": len(desc_text),
            "canonical": canonical_href,
            "h1_count": len(h1s),
            "h1_text": " | ".join(get_text(h1) for h1 in h1s),
            "missing_title": "YES" if not title_text else "NO",
            "missing_description": "YES" if not desc_text else "NO",
            "missing_canonical": "YES" if not canonical_href else "NO",
            "missing_h1": "YES" if not h1s else "NO",
        })

    with output.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "file",
            "title",
            "title_length",
            "meta_description",
            "description_length",
            "canonical",
            "h1_count",
            "h1_text",
            "missing_title",
            "missing_description",
            "missing_canonical",
            "missing_h1",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Checked {len(rows)} HTML files")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
