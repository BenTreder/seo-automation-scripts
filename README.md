cat > README.md <<'EOF'
# SEO Automation Scripts

A clean collection of practical Python scripts for auditing and improving websites.

These tools help check common SEO and website quality items such as:

- Page titles
- Meta descriptions
- Canonical tags
- Image alt text
- Internal links
- Broken links
- Sitemap generation
- Basic site structure

## Why This Exists

This repo is designed for small business websites, local SEO projects, static HTML websites, and simple PHP/HTML sites.

## Scripts

| Script | Purpose |
|---|---|
| `meta_checker.py` | Checks titles, meta descriptions, canonicals, and H1 tags |
| `image_alt_checker.py` | Finds images missing alt text |
| `internal_link_report.py` | Reports internal links found across HTML files |
| `broken_link_checker.py` | Checks internal links for missing local files |
| `sitemap_builder.py` | Builds a simple XML sitemap from local HTML files |

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
