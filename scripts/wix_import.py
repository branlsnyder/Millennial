#!/usr/bin/env python3
"""Import scraped Wix markdown into Jekyll _posts."""

from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

WIX_PAGES = Path(
    "/Users/brandonwoosnyder/Dropbox/docs-d/04_Repos/Work REPOS/Wix_export_manual/scraper/output/pages"
)
WIX_IMAGES = Path(
    "/Users/brandonwoosnyder/Dropbox/docs-d/04_Repos/Work REPOS/Wix_export_manual/scraper/output/assets/images"
)
JEKYLL_POSTS = Path(__file__).resolve().parent.parent / "_posts"
JEKYLL_IMG = Path(__file__).resolve().parent.parent / "assets" / "img"

SKIP_SLUGS = {
    "blank-1",
    "copy-of-works-tree-and-synthetic-1",  # Wix 404 placeholder page
    "works",
    "index",
    "about",
    "profile-zoehanson574-profile",
    "single-post-grow-your-blog-community",
    "single-post-design-a-stunning-blog",
    "single-post-manage-your-blog-from-your-live-site",
}

SKIP_PREFIXES = ("writings-",)

SLUG_TO_EXISTING = {
    "brrrr": "brrrr",
    "call-response": "call/response",
    "problem-of-deer": "the problem(s) of deer",
    "browser2021": "browser sound",
}

WORKS_SLUGS = {
    "problem-of-deer",
    "call-response",
    "brrrr",
    "musicaboutii",
    "copy-of-works-spirit-animal-univers-2",
    "sound-installation-home",
    "copy-of-works-spirit-animal-univers-1",
    "copy-of-works-give-sound-receive-1",
    "give-sound-receive-sound",
    "works-tree-and-synthetic",
    "copy-of-works-2-1",
    "copy-of-works-tree-and-synthetic-1",
    "wac-paper-2024",
    "browser2021",
}

PERFORMANCE_SLUGS = {
    "problem-of-deer",
    "give-sound-receive-sound",
    "copy-of-works-give-sound-receive-1",
    "musicaboutii",
}

MONTH_MAP = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}

RECENT_POSTS_RE = re.compile(r"^Recent Posts\s*$.*?(?=^# )", re.MULTILINE | re.DOTALL)
ARCHIVE_BLOCK_RE = re.compile(r"^Archive\s*$.*?(?=^Tags\s*$|^# )", re.MULTILINE | re.DOTALL)
TAGS_SIDEBAR_RE = re.compile(r"^Tags\s*$[\s\S]*?(?=^# )", re.MULTILINE)
FOOTER_NOISE_RE = re.compile(
    r"\n\d+ views\n\n0\n\n0 comments\n\nPost not marked as liked\n\n## Comments\n\n---\n\nWrite a comment\.\.\..*",
    re.DOTALL,
)
DATE_LINE_RE = re.compile(
    r"^- (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\s*$",
    re.MULTILINE | re.IGNORECASE,
)
READ_TIME_RE = re.compile(r"^- \d+ min read\s*$", re.MULTILINE)
UPDATED_RE = re.compile(r"^Updated:.*$", re.MULTILINE)
TAGS_FOOTER_RE = re.compile(r"\nTags:\n\n(?:- \[.*?\]\(.*?\)\n)+", re.MULTILINE)
BACK_TO_WORKS_RE = re.compile(
    r"\n\[Back to Works\]\(https://www\.brandonlincolnsnyder\.com/works\)\s*$"
)
YEAR_IN_HEADING_RE = re.compile(r"\[(\d{4})\]")
DATE_IN_SLUG_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
IMG_RE = re.compile(r"!\[([^\]]*)\]\((/assets/images/[^)]+)\)")
YOUTUBE_RE = re.compile(
    r"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})"
)


def normalize_title(s: str) -> str:
    s = re.sub(r"\s*\|.*$", "", s)
    s = re.sub(r"\[wix re-import\]\s*", "", s, flags=re.I)
    s = re.sub(r"[^\w\s]", "", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def load_existing_titles() -> set[str]:
    titles = set()
    for path in JEKYLL_POSTS.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        m = re.search(r'^title:\s*"(.+)"', text, re.MULTILINE)
        if m:
            titles.add(normalize_title(m.group(1)))
    return titles


def parse_front_matter(raw: str) -> tuple[dict[str, str], str]:
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    fm: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, parts[2].lstrip("\n")


def extract_main_title(body: str, fm_title: str) -> str:
    m = re.search(r"^# (.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^## (.+?)(?:\s*\[\d{4}\])?\s*$", body, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        title = title.replace(r"\*", "*")
        if title.lower() not in {"program note", "performance history", "about the premiere"}:
            return title
    title = fm_title.split("|")[0].strip()
    title = re.sub(r"^\(Works\)\s*", "", title, flags=re.I)
    return title


def extract_blog_date(body: str, slug: str) -> datetime | None:
    m = DATE_IN_SLUG_RE.search(slug)
    if m:
        y, mo, d = map(int, m.groups())
        return datetime(y, mo, d)
    m = re.search(
        r"^- ((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)) (\d{1,2}), (\d{4})\s*$",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    if m:
        month = MONTH_MAP[m.group(1).lower()[:3]]
        return datetime(int(m.group(3)), month, int(m.group(2)))
    # Slugs like single-post-i-spoke-at-the-2024-web-audio-conference
    m = re.search(r"-(20\d{2})-", slug)
    if m:
        year = int(m.group(1))
        return datetime(year, 1, 1)
    if slug == "browser2021":
        return datetime(2021, 1, 1)
    if slug == "wac-paper-2024":
        return datetime(2024, 9, 1)
    return None


def extract_performance_date(body: str) -> datetime | None:
    """First date in Performance History (supports M/YYYY and D/M/YYYY or M/D/YYYY)."""
    block = re.search(r"^## Performance History\s*$([\s\S]*?)(?:\n## |\Z)", body, re.MULTILINE)
    if not block:
        return None
    text = block.group(1)
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", text)
    if m:
        a, b, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if a > 12:  # D/M/YYYY (e.g. 13/11/2020)
            return datetime(year, b, a)
        if b > 12:  # M/D/YYYY
            return datetime(year, a, b)
        return datetime(year, a, b)  # ambiguous; assume M/D
    m = re.search(r"(\d{1,2})/(\d{4})", text)
    if m:
        return datetime(int(m.group(2)), int(m.group(1)), 1)
    return None


def extract_works_year(body: str) -> int | None:
    m = YEAR_IN_HEADING_RE.search(body)
    return int(m.group(1)) if m else None


def extract_tags(body: str) -> list[str]:
    tags: list[str] = []
    block = re.search(r"^Tags:\s*$([\s\S]*?)(?:\n\d+ views|\n## Comments|\Z)", body, re.MULTILINE)
    if block:
        for m in re.finditer(
            r"\[([^\]]+)\]\(https://www\.brandonlincolnsnyder\.com/writings/tags/", block.group(1)
        ):
            tag = re.sub(r"\s*\(\d+\).*$", "", m.group(1)).strip()
            if tag and tag not in tags:
                tags.append(tag)
    return tags


def clean_body(body: str) -> str:
    body = RECENT_POSTS_RE.sub("", body)
    body = ARCHIVE_BLOCK_RE.sub("", body)
    body = TAGS_SIDEBAR_RE.sub("", body)
    body = FOOTER_NOISE_RE.sub("", body)
    body = TAGS_FOOTER_RE.sub("", body)
    body = DATE_LINE_RE.sub("", body)
    body = READ_TIME_RE.sub("", body)
    body = UPDATED_RE.sub("", body)
    body = BACK_TO_WORKS_RE.sub("", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def rewrite_images(body: str, copied: set[str]) -> tuple[str, str | None]:
    featured = None

    def repl(match: re.Match[str]) -> str:
        nonlocal featured
        alt, src = match.group(1), match.group(2)
        fname = Path(src).name
        src_path = WIX_IMAGES / fname
        if src_path.exists():
            JEKYLL_IMG.mkdir(parents=True, exist_ok=True)
            dest = JEKYLL_IMG / fname
            if fname not in copied:
                shutil.copy2(src_path, dest)
                copied.add(fname)
            if featured is None:
                featured = fname
            return f'<img src="assets/img/{fname}" alt="{alt}">'
        return match.group(0)

    body = IMG_RE.sub(repl, body)
    body = body.replace("](/assets/images/", "](assets/img/")
    return body, featured


def embed_youtube_links(body: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    for line in lines:
        if line.strip().startswith("<iframe"):
            out.append(line)
            continue
        urls = re.findall(
            r"https?://(?:www\.)?(?:youtube\.com/watch\?v=[\w-]+(?:[^\s\)]*)?|youtu\.be/[\w-]+(?:[^\s\)]*)?|youtube\.com/shorts/[\w-]+(?:[^\s\)]*)?)",
            line,
        )
        if urls and not line.strip().startswith("!["):
            vid = YOUTUBE_RE.search(urls[0])
            if vid and ("youtube" in line.lower() or re.match(r"^\[.+\]\(.+\)\s*$", line.strip())):
                embed = (
                    f'<iframe src="https://www.youtube.com/embed/{vid.group(1)}" '
                    'title="YouTube video player" frameborder="0" '
                    'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
                    'gyroscope; picture-in-picture; web-share" '
                    'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
                )
                out.append(embed)
                out.append("{: .featured-media}")
                out.append("")
                continue
        out.append(line)
    return "\n".join(out)


def jekyll_slug(title: str, wix_slug: str) -> str:
    if wix_slug.startswith("single-post-"):
        base = wix_slug.removeprefix("single-post-")
    else:
        base = wix_slug
    base = re.sub(r"^copy-of-works-", "", base)
    base = re.sub(r"^works-", "", base)
    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)
    # Prefer human-readable slug from title for opaque Wix copy-of names
    if base in {"2-1", "spirit-animal-univers-1", "spirit-animal-univers-2", "give-sound-receive-1", "tree-and-synthetic-1"}:
        base = re.sub(r"[^\w]+", "-", title.lower()).strip("-")[:60]
    if not base:
        base = re.sub(r"[^\w]+", "-", title.lower()).strip("-")[:60]
    return base[:80]


def is_duplicate(wix_slug: str, title: str, existing: set[str]) -> bool:
    if wix_slug in SLUG_TO_EXISTING:
        return normalize_title(SLUG_TO_EXISTING[wix_slug]) in existing
    # Blog posts may match by title; works pages only match known slugs
    if wix_slug.startswith("single-post-"):
        return normalize_title(title) in existing
    return False


def infer_category(wix_slug: str) -> str:
    if wix_slug.startswith("single-post-") or wix_slug == "wac-paper-2024":
        return "writings"
    if wix_slug in PERFORMANCE_SLUGS:
        return "performance"
    if wix_slug == "browser2021":
        return "workshops"
    return "composition"


def infer_subtitle(body: str) -> str:
    for line in body.splitlines()[:12]:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!") or line.startswith("<"):
            continue
        if line.startswith("##"):
            break
        if len(line) < 120 and not line.startswith("-"):
            return line
    return ""


def build_post_content(
    wix_slug: str,
    fm: dict[str, str],
    raw_body: str,
    existing: set[str],
    copied: set[str],
) -> tuple[str, dict]:
    cleaned = clean_body(raw_body)
    title = extract_main_title(cleaned, fm.get("title", wix_slug))
    duplicate = is_duplicate(wix_slug, title, existing)
    if duplicate:
        title = f"[Wix re-import] {title}"

    # Parse date before clean_body strips the date line from blog posts
    dt = extract_blog_date(raw_body, wix_slug) or extract_blog_date(cleaned, wix_slug)
    if not dt:
        dt = extract_performance_date(cleaned)
    if not dt:
        year = extract_works_year(cleaned)
        dt = datetime(year or 2017, 1, 1)

    body = re.sub(r"^# .+\n+", "", cleaned, count=1).strip()
    # Drop leading H2 that duplicates the extracted title (common on works pages)
    plain_title = re.sub(r"[^\w\s]", "", title.lower()).strip()
    body = re.sub(
        rf"^## {re.escape(title.split('[')[0].strip())}(?:\s*\[\d{{4}}\])?\s*\n+",
        "",
        body,
        count=1,
        flags=re.IGNORECASE,
    )
    body, featured_image = rewrite_images(body, copied)
    body = embed_youtube_links(body)
    category = infer_category(wix_slug)
    tags = extract_tags(raw_body) or extract_tags(cleaned)
    if duplicate:
        tags = ["wix-re-import", *tags]
    subtitle = infer_subtitle(body)
    if subtitle and body.startswith(subtitle):
        body = body[len(subtitle) :].lstrip()

    note = ""
    if duplicate:
        note = (
            "> **Note:** This post was re-imported from the legacy Wix site. "
            "An edited version may already exist on this site.\n\n"
        )

    if featured_image and not body.lstrip().startswith("<iframe"):
        body = (
            f'<img src="assets/img/{featured_image}" alt="{title}">\n'
            "{: .featured-media}\n\n" + body
        )

    post_slug = jekyll_slug(title, wix_slug)
    filename = f"{dt.strftime('%Y-%m-%d')}-{post_slug}.md"
    out_path = JEKYLL_POSTS / filename
    # Avoid clobbering existing hand-edited posts on same date+slug
    if out_path.exists():
        filename = f"{dt.strftime('%Y-%m-%d')}-{post_slug}-wix-import.md"
        out_path = JEKYLL_POSTS / filename

    safe_title = title.replace('"', "'")
    lines = [
        "---",
        "layout: post",
        f'title: "{safe_title}"',
    ]
    if subtitle:
        lines.append(f'subtitle: "{subtitle.replace(chr(34), chr(39))}"')
    lines.append(f"category: {category}")
    if tags:
        lines.append(f"tags: [{', '.join(tags)}]")
    if featured_image:
        lines.append(f"image: {featured_image}")
    if duplicate:
        lines.append("wix_reimport: true")
    lines.append("---")
    lines.append("")
    full = "\n".join(lines) + "\n" + note + body + "\n"
    return full, {
        "wix_slug": wix_slug,
        "file": filename,
        "title": title,
        "duplicate": duplicate,
        "category": category,
    }


def main() -> None:
    existing = load_existing_titles()
    copied: set[str] = set()
    report: list[dict] = []
    created = 0
    skipped = 0

    for path in sorted(WIX_PAGES.glob("*.md")):
        slug = path.stem
        if slug in SKIP_SLUGS or any(slug.startswith(p) for p in SKIP_PREFIXES):
            skipped += 1
            continue
        if not (slug.startswith("single-post-") or slug in WORKS_SLUGS):
            skipped += 1
            continue

        raw = path.read_text(encoding="utf-8")
        fm, body = parse_front_matter(raw)
        content, meta = build_post_content(slug, fm, body, existing, copied)
        out_path = JEKYLL_POSTS / meta["file"]
        out_path.write_text(content, encoding="utf-8")
        report.append(meta)
        created += 1

    report_path = Path(__file__).resolve().parent.parent / "WIX_IMPORT_REPORT.md"
    lines = [
        "# Wix Import Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"- Posts created: {created}",
        f"- Pages skipped (non-content): {skipped}",
        f"- Images copied to assets/img: {len(copied)}",
        "",
        "## Created posts",
        "",
        "| Wix slug | Jekyll file | Category | Duplicate? |",
        "|----------|-------------|----------|------------|",
    ]
    for r in report:
        lines.append(
            f"| {r['wix_slug']} | {r['file']} | {r['category']} | {'yes' if r['duplicate'] else 'no'} |"
        )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {created} posts, copied {len(copied)} images")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
