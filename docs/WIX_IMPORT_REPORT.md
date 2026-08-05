# Wix Import Report

Generated: 2026-05-18

## Summary

Imported content from `Wix_export_manual/scraper/output` into this Jekyll site's `_posts/` directory.

| Metric | Count |
|--------|------:|
| New markdown posts created | 38 |
| Scraper pages skipped (nav, archives, tags, Wix templates, 404) | 42 |
| Images copied to `assets/img/` | 22 |
| Pre-existing posts on site (unchanged) | 12 |

Import script: `scripts/wix_import.py` (re-runnable).

---

## What was imported

### Writings (blog) — 25 posts

All `single-post/*` articles from the old Wix blog, dated 2017–2024. Assigned `category: writings` (new category; no dedicated Writings page exists yet—posts will appear on the home paginator).

Includes Difference Tones columns, Darmstadt/Liza Lim essays, web-audio articles, and announcements.

### Compositions & performances — 13 posts

Works pages from the old site:

- *home* (sound installation)
- Sights and Sounds of Home
- tree and synthetic
- Lightning | Paper Birch
- Give Sound / Receive Sound
- Taste The Rain
- Music About Music About Background Music - II
- milk bubbles
- WAC 2024 paper (PDF link)
- Plus re-imports of works already on this site (see below)

---

## Duplicates (labeled `[Wix re-import]`)

These already had hand-edited posts on the new site. Wix versions were recreated with:

- Title prefix: `[Wix re-import]`
- Front matter: `wix_reimport: true`, tag `wix-re-import`
- Top-of-post note explaining the duplicate
- Filename suffix: `-wix-import.md` where needed to avoid overwriting

| Wix source | Existing Jekyll post | Imported file |
|------------|---------------------|---------------|
| `brrrr` | `2022-06-02-brrrr.md` | `2022-10-01-brrrr-wix-import.md` |
| `call-response` | `2024-06-05-call-response.md` | `2024-07-01-call-response-wix-import.md` |
| `problem-of-deer` | `2025-03-02-tpod.md` | `2025-03-01-problem-of-deer.md` |
| `browser2021` | `2022-06-03-browser-sound.md` | `2021-01-01-browser2021-wix-import.md` |

You can delete the `-wix-import` copies once you have confirmed nothing worth merging remains.

---

## Skipped content (not imported)

| Reason | Examples |
|--------|----------|
| Site navigation / index | `index`, `works`, `about`, `writings` |
| Blog index pagination | `writings-page-2`, `writings-page-3` |
| Monthly archives | `writings-archive-2017-09`, etc. |
| Tag listing pages | `writings-tags-darmstadt`, etc. |
| Wix default blog templates | `grow-your-blog-community`, `design-a-stunning-blog`, `manage-your-blog-from-your-live-site` |
| Dead / 404 Wix page | `copy-of-works-tree-and-synthetic-1`, `blank-1` |
| Stray profile page | `profile-zoehanson574-profile` |

---

## New works on old site not previously on Jekyll

These are **new** posts (not duplicates):

- `2017-02-17-lightning-paper-birch.md`
- `2017-04-15-tree-and-synthetic.md`
- `2018-04-08-give-sound-receive-sound-wix-import.md` — note: no prior post; filename kept from script run
- `2018-05-08-taste-the-rain.md`
- `2019-02-25-sights-and-sounds-of-home-an-experimental-conversation-between.md`
- `2019-05-01-sound-installation-home.md` (*home*)
- `2020-07-16-milk-bubbles.md`
- `2020-11-13-musicaboutii.md`
- All 25 writings posts

---

## Loose ends & discrepancies

### 1. No Writings index page

The old site had `/writings` with archives and tags. This Jekyll theme only has `composition`, `performance`, and `workshops` category pages. Writings posts use `category: writings` and will show on the **home** feed but not on a dedicated writings page unless you add one later.

### 2. External links still point to Wix

Many posts link to `brandonlincolnsnyder.com/_files/ugd/...` PDFs, old permalinks, and embedded media. Those URLs may break when Wix is taken down. Consider downloading PDFs into `assets/` and updating links.

### 3. YouTube / media gaps

The Wix scrape for **brrrr** did not capture the main full-performance YouTube embed—only the shorts link. Your edited `2022-06-02-brrrr.md` still has the better embed.

### 4. Workshop vs. tutorial naming

- Wix: `single-post-p5-sound-crash-course-javascript-for-sound-artists` (WebSoundArt tutorial article)
- Jekyll: `2023-06-03-javascript-for-sound-artists.md` (6-week Browser Sound course)

These are **related but different** content; both were kept.

### 5. Performance history

Some imported works include a `## Performance History` section in the post body. The site also supports `_data/events` for the `performance-history.html` include, but imported events were **not** added to that YAML file.

### 6. Images

- 22 images were copied from the scraper; many posts reference images still hosted on Wix CDN paths that were not downloaded.
- Duplicate featured image appears in some posts (hero + inline same file).

### 7. Formatting artifacts

- Program notes from Wix sometimes have excessive blank lines / spacing (e.g. tree and synthetic).
- Some subtitles picked up markdown link syntax from the first paragraph.
- `*home*` title retains escaped asterisks in places.

### 8. Posts on Jekyll not in Wix scrape

These exist only on the new site (added after or not on old Wix works list):

- Jam, Bppbch, Sea Fret, Spectator Sport, LUL solo set, NYPL workshops, etc.

### 9. `sea-fret.md` content issue (pre-existing)

`2026-01-01-sea-fret.md` currently contains **brrrr** copy and thumbnail—not Sea Fret content. This was not introduced by the import but is worth fixing separately.

---

## Files created (full list)

| Jekyll file | Category |
|-------------|----------|
| `2017-02-17-lightning-paper-birch.md` | composition |
| `2017-04-15-tree-and-synthetic.md` | composition |
| `2017-09-26-when-artist-change-outfits.md` | writings |
| `2017-10-17-hearing-the-pathway.md` | writings |
| `2017-11-14-a-reverberant-goodbye.md` | writings |
| `2017-11-14-spirituality-and-sound.md` | writings |
| `2018-04-08-give-sound-receive-sound-wix-import.md` | performance |
| `2018-05-08-taste-the-rain.md` | performance |
| `2018-05-31-earbuds-and-worldbuilding.md` | writings |
| `2018-07-26-good-morning-darmstadt.md` | writings |
| `2018-08-21-losing-my-uniqueness.md` | writings |
| `2018-09-08-the-fuzzy-boundary-betweenen-myself-new-music-and-cola-whiskey.md` | writings |
| `2018-09-22-darmstadt-in-the-aftermath-of-grid-liza-lim-ii.md` | writings |
| `2018-10-20-collaborative-composition-liza-lim-iii.md` | writings |
| `2018-12-10-a-gradual-process-an-mec-original.md` | writings |
| `2019-02-25-sights-and-sounds-of-home-an-experimental-conversation-between.md` | composition |
| `2019-04-03-leading-me-an-audio-essay-for-betweenen-lands.md` | writings |
| `2019-04-07-difference-tones-april-2019.md` | writings |
| `2019-05-10-did-i-steward-authority-well-difference-tones-may-2019.md` | writings |
| `2019-06-13-why-i-moved-to-germany-difference-tones-june-2019.md` | writings |
| `2019-07-19-im-a-living-educational-video-difference-tones-july-2019.md` | writings |
| `2019-09-11-piano-god-and-daily-routines-difference-tones-september-2019.md` | writings |
| `2019-11-24-difference-tones-november-2019.md` | writings |
| `2019-05-01-sound-installation-home.md` | composition |
| `2020-05-06-quiet-time-featured-in-poiema-issue-3.md` | writings |
| `2020-07-16-milk-bubbles.md` | composition |
| `2020-11-13-musicaboutii.md` | performance |
| `2021-01-01-browser2021-wix-import.md` | workshops |
| `2022-10-01-brrrr-wix-import.md` | composition |
| `2024-02-16-audio-visual-relationships-in-web-based-sound-art.md` | writings |
| `2024-02-16-interactive-web-sound-art.md` | writings |
| `2024-02-16-will-nfts-actually-help-artists-make-money-royalties-and-smart-contracts.md` | writings |
| `2024-05-01-online-communities-for-web-based-sound-art.md` | writings |
| `2024-05-01-p5-sound-crash-course-javascript-for-sound-artists.md` | writings |
| `2024-07-01-call-response-wix-import.md` | composition |
| `2024-09-01-wac-paper-2024.md` | writings |
| `2024-09-02-i-spoke-at-the-2024-web-audio-conference.md` | writings |
| `2025-03-01-problem-of-deer.md` | performance |
