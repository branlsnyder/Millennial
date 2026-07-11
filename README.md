# brandonlincolnsnyder.com

Personal website of **Brandon Woo Snyder** — composer, performer, media artist.

Built with [Jekyll](https://jekyllrb.com/) using the [Millennial](https://github.com/LeNPaul/Millennial) theme by Paul Le, hosted on [GitHub Pages](https://pages.github.com/).

## Prerequisites

- Ruby 3.x (see `.ruby-version`)
- [Bundler](https://bundler.io/)

## Quick start

```sh
bundle install
bundle exec jekyll serve --livereload
```

The site is served at `http://localhost:4000`. The `--livereload` flag auto-refreshes the browser when you edit files.

### Troubleshooting native extension errors

If you see errors like `linked to incompatible libruby.3.2.dylib`, your native gems were compiled against a different Ruby version. Fix with:

```sh
gem pristine --all
```

## Creating a new post

Add a file to `_posts/` following the naming convention:

```
YYYY-MM-DD-your-slug.md
```

### Front matter

```yaml
---
layout: post
title: "My Title"
subtitle: "Optional subtitle"
category: composition       # one of: composition, performance, workshops, writings
tags: [tag1, tag2]
image: my-image.jpg         # filename in assets/img/
---
```

**Categories** map to the page they appear on:
- `composition` -> /composition
- `performance` -> /performance
- `workshops` -> /workshops
- `writings` -> appears only on the homepage feed (no dedicated page)

**Tags** are used for related posts and can be browsed at /tags.

**Image** should be the filename of a thumbnail in `assets/img/`. It appears as a card background on category pages and the homepage.

### Performance history

If a post has performance data, add a row to `_data/events.csv` with the exact post title under the `Title` column. The include `_includes/performance-history.html` automatically renders a list of dates, locations, and performers on the post page.

## Images

Place images in `assets/img/`. Reference them in front matter as `image: filename.jpg` and in markdown body as `![alt](assets/img/filename.jpg)`.

## Site configuration

- `_config.yml` -- Jekyll build settings, title, description, plugins
- `_data/settings.yml` -- menu items, social links, Google Analytics, Disqus
- `_data/events.csv` -- performance/event history for each post

## Directory structure

```
├── _posts/          # Blog posts (markdown)
├── _layouts/        # HTML templates (default, post, page, home, category)
├── _includes/       # Reusable partials (header, footer, featured-post, etc.)
├── _data/           # YAML/CSV data files (settings, events)
├── _sass/           # SCSS partials
├── assets/
│   ├── css/         # Compiled stylesheets
│   └── img/         # Images and thumbnails
├── pages/           # Category landing pages (about, composition, performance, workshops)
└── scripts/         # Utility scripts (wix_import.py)
```
