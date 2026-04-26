from pathlib import Path
from datetime import date
import sys
import xml.etree.ElementTree as ET


def page_url(base_url, root, path):
    rel = path.relative_to(root)

    if rel.name == "index.html":
        url_path = "/" if str(rel.parent) == "." else f"/{rel.parent.as_posix()}/"
    else:
        url_path = "/" + rel.with_suffix("").as_posix()

    return base_url.rstrip("/") + url_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/sitemap_builder.py /path/to/site https://example.com")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    base_url = sys.argv[2].strip().rstrip("/")
    output = Path("sitemap.xml")

    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"
    })

    html_files = sorted(root.rglob("*.html"))

    for path in html_files:
        if any(part.startswith("_") for part in path.relative_to(root).parts):
            continue

        url = ET.SubElement(urlset, "url")

        loc = ET.SubElement(url, "loc")
        loc.text = page_url(base_url, root, path)

        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = date.today().isoformat()

        changefreq = ET.SubElement(url, "changefreq")
        changefreq.text = "weekly"

        priority = ET.SubElement(url, "priority")
        priority.text = "1.0" if path.name == "index.html" and path.parent == root else "0.8"

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(output, encoding="utf-8", xml_declaration=True)

    print(f"Added {len(html_files)} HTML files")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
