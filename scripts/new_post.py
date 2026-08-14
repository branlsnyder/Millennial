#!/usr/bin/env python3
"""Generate a boilerplate Jekyll post in _posts/ interactively."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO / "_posts"
CATEGORIES = ["composition", "performance", "workshops", "writings"]

FEATURED_VIDEO = (
    '<iframe src="YOUTUBE/EMBED/URL/HERE" title="YouTube video player" '
    'frameborder="0" allow="accelerometer; autoplay; clipboard-write; '
    'encrypted-media; gyroscope; picture-in-picture; web-share" '
    'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    "\n"
    "{: .featured-media}"
)


def featured_photo(filename: str, title: str) -> str:
    stem = Path(filename).stem
    return (
        f'<img src="assets/img/opt/{stem}.webp" alt="{title}">'
        "\n"
        "{: .featured-media}"
    )


def slugify(title: str) -> str:
    s = title.lower().strip()
    s = s.replace("'", "").replace('"', "")
    parts = s.split()
    return "-".join(parts)[:80]


def prompt_title() -> str:
    while True:
        title = input("Post Title? ").strip()
        if title:
            return title
        print("Title cannot be empty.", file=sys.stderr)


def prompt_category() -> str:
    choices = ", ".join(CATEGORIES)
    while True:
        category = input(f"Category? [{choices}] ").strip().lower()
        if category in CATEGORIES:
            return category
        print(f"Invalid category. Choose one of: {choices}", file=sys.stderr)


def prompt_media() -> str:
    while True:
        media = input("Featured Media (video/photo)? ").strip().lower()
        if media in ("video", "photo"):
            return media
        print("Invalid choice. Enter 'video' or 'photo'.", file=sys.stderr)


def prompt_image() -> str:
    while True:
        filename = input("Image filename? ").strip()
        if filename:
            return filename
        print("Image filename cannot be empty.", file=sys.stderr)


def main() -> None:
    title = prompt_title()
    category = prompt_category()
    media = prompt_media()

    post_date = str(date.today())
    filename = f"{post_date}-{slugify(title)}.md"
    out = POSTS_DIR / filename

    if out.exists():
        print(f"Error: {out} already exists", file=sys.stderr)
        sys.exit(1)

    if media == "video":
        image_field = "image: "
        featured = FEATURED_VIDEO
    else:
        image = prompt_image()
        image_field = f"image: {image}"
        featured = featured_photo(image, title)

    lines = [
        "---",
        "layout: post",
        f'title: "{title}"',
        'subtitle: ""',
        f"category: {category}",
        "tags: []",
        image_field,
        "---",
        "",
        featured,
        "",
    ]

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {out}")


if __name__ == "__main__":
    main()
