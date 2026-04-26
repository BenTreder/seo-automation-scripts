# SEO Automation Scripts

A collection of practical Python scripts built to help website owners, developers, SEO specialists, and small businesses quickly audit common technical SEO issues.

These scripts help simplify repetitive website audits and identify common problems that impact search rankings, user experience, and site maintenance.

---

## What This Repository Helps With

This toolkit helps audit:

- Missing page titles
- Missing meta descriptions
- Missing canonical tags
- Missing H1 tags
- Missing image alt text
- Internal link structure
- Broken internal links
- XML sitemap generation

These scripts work especially well for:

- Static HTML websites  
- Small business websites  
- Local SEO projects  
- Portfolio websites  
- Lead generation websites  
- Basic PHP websites  
- Website redesign audits  

---

# Included Scripts

---

## 1. Meta Checker

**File:**

`scripts/meta_checker.py`

Checks:

- Title tags
- Title length
- Meta descriptions
- Meta description length
- Canonical tags
- H1 tags
- Missing SEO metadata

### Output:

`meta_report.csv`

---

## 2. Image Alt Text Checker

**File:**

`scripts/image_alt_checker.py`

Checks:

- Missing image alt text
- Image source paths
- Existing alt text

### Output:

`image_alt_report.csv`

---

## 3. Internal Link Report

**File:**

`scripts/internal_link_report.py`

Checks:

- Internal links
- Anchor text
- Link paths

### Output:

`internal_link_report.csv`

---

## 4. Broken Link Checker

**File:**

`scripts/broken_link_checker.py`

Checks:

- Broken internal links
- Missing pages
- Invalid local links

### Output:

`broken_link_report.csv`

---

## 5. Sitemap Builder

**File:**

`scripts/sitemap_builder.py`

Builds:

- XML sitemap
- Basic URL structure
- Last modified dates
- Priority values

### Output:

`sitemap.xml`

---

# Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/seo-automation-scripts.git
cd seo-automation-scripts
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# How To Use

## Run Meta Checker

```bash
python scripts/meta_checker.py /path/to/website
```

Example:

```bash
python scripts/meta_checker.py /Users/yourname/mywebsite
```

---

## Run Image Alt Checker

```bash
python scripts/image_alt_checker.py /path/to/website
```

---

## Run Internal Link Report

```bash
python scripts/internal_link_report.py /path/to/website
```

---

## Run Broken Link Checker

```bash
python scripts/broken_link_checker.py /path/to/website
```

---

## Run Sitemap Builder

```bash
python scripts/sitemap_builder.py /path/to/website https://example.com
```

Example:

```bash
python scripts/sitemap_builder.py /Users/yourname/mywebsite https://mywebsite.com
```

---

# Example Repository Structure

```txt
seo-automation-scripts/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── scripts/
    ├── meta_checker.py
    ├── image_alt_checker.py
    ├── internal_link_report.py
    ├── broken_link_checker.py
    └── sitemap_builder.py
```

---

# Who This Is For

This repository is useful for:

- Web designers  
- SEO specialists  
- Freelancers  
- Agencies  
- Small business website owners  
- Developers managing multiple websites  

---

# Important Privacy Notes

Do NOT upload:

- Private client websites
- API keys
- Cloudflare credentials
- Hosting credentials
- Analytics credentials
- Customer information
- Internal business reports
- Private server paths

Keep this repository clean and reusable.

---

# Future Improvements

Potential future scripts:

- Schema markup checker
- Open Graph tag checker
- Page speed audit helper
- Redirect checker
- Duplicate title detector
- Sitemap validator
- Robots.txt checker

---

# About

Built by Ben Treder

Website: https://bentreder.com

I build websites, improve SEO, solve technical issues, and help businesses improve their online presence through practical systems and automation.
