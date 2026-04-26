from pathlib import Path
from bs4 import BeautifulSoup
import csv
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/image_alt_checker.py /path/to/site")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    output = Path("image_alt_report.csv")

    rows = []

    for path in root.rglob("*.html"):
        html = path.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(html, "lxml")

        for img in soup.find_all("img"):
            src = img.get("src", "").strip()
            alt = img.get("alt")

            rows.append({
                "file": str(path.relative_to(root)),
                "src": src,
                "alt": alt.strip() if alt else "",
                "missing_alt": "YES" if alt is None or not alt.strip() else "NO",
            })

    with output.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["file", "src", "alt", "missing_alt"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    missing = sum(1 for row in rows if row["missing_alt"] == "YES")

    print(f"Checked {len(rows)} images")
    print(f"Missing alt text: {missing}")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
