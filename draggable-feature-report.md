# Draggable Homepage Headshot — Experiment Report

## What changed

`#home-headshot` on the homepage is now freely draggable (x/y, no constraints) using
[anime.js v4](https://animejs.com/documentation/draggable/) `createDraggable()`. It
sits above the posts-grid (`z-index: 1`). Dragging uses CSS transforms, so it never
affects text wrapping or layout flow of other elements.

## Files touched (all changes live on the `draggable-components` branch)

1. **`_layouts/default.html`** — added anime.js UMD bundle from jsDelivr CDN, with `defer`:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/animejs/dist/bundles/anime.umd.min.js" defer></script>
   ```

2. **`_layouts/home.html`** — inside the existing `DOMContentLoaded` handler, added:
   ```js
   const { createDraggable } = anime;
   createDraggable(img);
   ```

3. **`_sass/_home.scss`** — two edits:
   - `.home-image` gained `position: relative; z-index: 1;` so the image renders in front of the posts-grid when dragged over it.
   - `@keyframes gentle-rotate` now animates the standalone `rotate:` property instead of `transform: rotate(...)`. Required because anime.js drags via the inline `transform` style; the old `transform` keyframe animation would have overridden it and made dragging invisible. The `rotate` property composes with the drag transform, so the wobble animation still plays.

## How to revert to the version without this feature

**Option A — switch branches (simplest).** The main deployed branch is `gh-pages`,
which does not contain these changes:

```bash
git checkout gh-pages
```

**Option B — stay on this branch and undo the changes.** These edits are currently
uncommitted, so either:

```bash
# discard all uncommitted changes on this branch
git restore _layouts/default.html _layouts/home.html _sass/_home.scss
```

or, if they are committed later, revert just these files:

```bash
git checkout gh-pages -- _layouts/default.html _layouts/home.html _sass/_home.scss
```

To rebuild after reverting: `bundle exec jekyll build`

## Notes

- The anime.js CDN script is loaded on **every** page (it was added to the global
  `default.html` layout), so other pages still fetch it even though only the homepage
  uses it. Removing the script tag from `_layouts/default.html` eliminates that too.
- This report file (`draggable-feature-report.md`) is documentation only and has no
  effect on the site; delete it if you don't want it in the revert.
