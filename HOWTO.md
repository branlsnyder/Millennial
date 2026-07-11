# How To

## Create a new post

Two options:

**A) Use the script:**

```sh
python3 scripts/new_post.py "Post Title" -c composition -t tag1 tag2
```

**B) Manually** — create a file in `_posts/` named `YYYY-MM-DD-your-slug.md` with front matter:

```yaml
---
layout: post
title: "Post Title"
subtitle: "Optional subtitle"
category: composition     # composition | performance | workshops | writings
tags: [tag1, tag2]
image: thumbnail.jpg      # filename in assets/img/
---
```

Write the body in markdown below the `---`.

## Edit the header (navigation)

Open `_data/settings.yml` and edit the `menu:` list. Each entry adds a link:

```yaml
menu:
- {name: 'Composition', url: 'composition'}
- {name: 'About',       url: 'about'}
```

The `url` value must match a page's `permalink` (e.g. `/about` → `about`). Social icons (YouTube, Instagram, etc.) are in the `social:` list below the menu.

## Edit the homepage

Open `_layouts/home.html`. The greeting text and headshot are in the `.home-salutation-group` div. The post grid below it is automatically populated from `_posts/`. To hide a post from the homepage, add `homeExclude` to its tags.

## Edit the events CSV

Open `_data/events.csv`. Each row is a performance:

```
Date,Title,Location,Performer
3/1/2026,Winter Ceremony (Short Film Score),SXSW Film Festival,
```

The `Title` must match the post's `title:` exactly. The matching events render automatically on that post's page.

## Change the style (fonts, colors, layout)

Open `assets/css/main.scss`. Key variables at the top:

```scss
$heading-font-family: "Instrument Serif", serif;
$base-font-family: "Alegreya", serif;
$body-font-family: "Alegreya", serif;
$brand-color: black;           // link color
$container-width: 1100px;      // max page width
```

Swap the font names or `$brand-color` to anything you like. The Google Fonts import is in `_includes/head.html` — if you change a font, update the `<link>` there too.

For more targeted styling, edit the partials in `_sass/` (e.g. `_header.scss`, `_footer.scss`, `_post.scss`).
