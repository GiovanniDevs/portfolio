# Portfolio CMS (Wagtail)

A personal portfolio and blog CMS built with Wagtail and Django.

This project started from the official Wagtail beginner and extended tutorials, and was then expanded with custom homepage sections, content blocks, rich text editor extensions, and production-focused configuration.

## Project Scope

This repository implements a content-managed portfolio website with:

- A custom homepage with hero, about, featured work, and featured posts
- A full blog system (authors, tags, gallery images, code blocks)
- Reusable StreamField blocks for portfolio content
- Site-wide navigation/footer settings managed in Wagtail admin
- Contact form page powered by Wagtail forms
- Production-ready settings for static/media and database deployment

This README documents what currently exists. You can add product details such as wireframes, deployment provider steps, and content strategy as needed.

## Features

## 1) Content Models and CMS Features

- `HomePage` model with:
  - Hero image/text/lead/CTA fields
  - Rich text intro + about sections
  - Top project showcase fields (title, summary, stack, links)
  - StreamField sections for featured projects and featured posts
  - Latest blog post added to template context
- `BlogIndexPage` with reverse chronological live post listing
- `BlogPage` with:
  - Date, intro, StreamField body
  - Author relationships
  - Tags
  - Search indexing for intro/body
  - Gallery relation with orderable images
- `BlogTagIndexPage` to filter posts by `?tag=`
- `PortfolioPage` (child of Home) with StreamField body
- `FormPage` and inline `FormField` definitions via Wagtail forms

## 2) Custom StreamField Blocks

- Shared blocks in `base` app:
  - Heading block (size-aware)
  - Captioned image block
  - Paragraph and embed support
- Portfolio blocks:
  - Card block
  - Featured posts block (chooses blog pages)
- Homepage-specific project card block
- Blog custom code block with language selector

## 3) Snippets, Settings, and Template Tags

- Global navigation settings (`LinkedIn`, `GitHub`, `Email`)
- Editable footer snippet with draft/revision/preview support
- Custom template tags for:
  - Footer text rendering
  - Site root lookup
  - Latest CV/Resume document lookup

## 4) Frontend and UX

- Custom templates for home/blog/portfolio/form/search
- Bootstrap + custom CSS
- Font Awesome icons
- Favicon, semantic main layout, responsive navigation/footer
- Wagtail user bar integrated in header

## 5) Search

- Search view and paginated search template are implemented
- Search route is currently commented in URL config (see "Known Gaps / TODO")

## 6) Production and Ops

- WhiteNoise static handling
- Cloudinary media storage in production settings
- PostgreSQL via `dj-database-url` in production
- SSL redirect and trusted CSRF origin support
- Build script for install + collectstatic + migrate

## Tutorial Alignment

The implementation broadly covers the official Wagtail tutorial journey:

- Beginner tutorial: homepage extension, blog, authors, tags, gallery, context overrides
- Extended tutorial: footer/settings/snippets, menu, forms, StreamField portfolio, search, deployment readiness

The project also adds custom functionality beyond tutorial scope (custom rich text features, code blocks, advanced homepage sections, CV document lookup).

## Tech Stack

- Python 3
- Django 6.0.3
- Wagtail 7.3.1
- SQLite (development)
- PostgreSQL (production)
- WhiteNoise
- Cloudinary (`django-cloudinary-storage`)
- django-taggit, django-modelcluster
- Bootstrap 5, Font Awesome

## Repository Layout

```
.
├── build.sh
├── README.md
└── mysite/
		├── manage.py
		├── requirements.txt
		├── base/
		├── blog/
		├── home/
		├── portfolio/
		├── search/
		└── mysite/
				├── urls.py
				└── settings/
						├── base.py
						├── dev.py
						└── production.py
```

## Local Development Setup

## Prerequisites

- Python 3.10+
- `pip`
- Virtual environment support (`venv`)

## Install

From repository root:

```bash
cd mysite
python -m venv .venv
```

Activate virtual environment:

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and run:

```bash
python manage.py migrate
python manage.py runserver
```

Create admin user:

```bash
python manage.py createsuperuser
```

Admin URL: `http://127.0.0.1:8000/admin/`

## Build Script

The repository includes `build.sh`:

```bash
#!/usr/bin/env bash
set -o errexit
cd mysite
pip install -r requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py migrate
```

Useful for CI/deployment build steps.

## Configuration

## Development

- Uses `mysite/settings/dev.py`
- SQLite database
- Debug enabled

## Production

`mysite/settings/production.py` expects environment variables, including:

- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`
- `DATABASE_URL` (for `dj-database-url`)
- `DJANGO_CSRF_TRUSTED_ORIGINS`

## Known Gaps / TODO

- Search endpoint in `mysite/urls.py` is currently commented out:
  - `path("search/", search_views.search, name="search")`
- README does not yet include:
  - Wireframes/design rationale
  - Deployment provider runbook
  - Content model diagrams
  - Test strategy and coverage details

## Suggested Next Additions

You mentioned you will add missing details. Good additions to this README:

- Product goals and target audience
- Wireframes / UX screenshots
- Deployment platform steps (Render/Fly/Heroku/etc.)
- CI pipeline notes
- Backup and media strategy
- Security checklist (secrets, hosts, HTTPS, admin hardening)
- Manual test checklist and regression scenarios

## License

Add your preferred license here.
