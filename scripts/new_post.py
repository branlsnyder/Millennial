#!/usr/bin/env python3
"""Generate a boilerplate Jekyll post in _posts/."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO / "_posts"
CATEGORIES = ["composition", "performance", "workshops", "writings"]


def slugify(title: str) -> str:
    s = title.lower().strip()
    s = s.replace("'", "").replace('"', "")
    parts = s.split()
    return "-".join(parts)[:80]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Jekyll post")
    parser.add_argument("title", help="Post title")
    parser.add_argument("-c", "--category", choices=CATEGORIES, default="writings",
                        help="Post category (default: writings)")
    parser.add_argument("-t", "--tags", nargs="*", default=[],
                        help="Space-separated tags")
    parser.add_argument("-s", "--subtitle", default="",
                        help="Optional subtitle")
    parser.add_argument("-i", "--image", default="",
                        help="Thumbnail filename in assets/img/")
    parser.add_argument("-d", "--date", default=str(date.today()),
                        help="Post date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    title = args.title
    post_date = args.date
    filename = f"{post_date}-{slugify(title)}.md"
    out = POSTS_DIR / filename

    if out.exists():
        print(f"Error: {out} already exists", file=sys.stderr)
        sys.exit(1)

    lines = [
        "---",
        f'layout: post',
        f'title: "{title}"',
    ]
    if args.subtitle:
        lines.append(f'subtitle: "{args.subtitle}"')
    lines.append(f"category: {args.category}")
    if args.tags:
        tags = ", ".join(args.tags)
        lines.append(f"tags: [{tags}]")
    if args.image:
        lines.append(f"image: {args.image}")
    lines.append("---")
    lines.append("")

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {out}")


if __name__ == "__main__":
    main()
