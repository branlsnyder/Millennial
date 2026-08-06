# Draggable Homepage Headshot — Experiment Report

## What changed

`#home-headshot` on the homepage is draggable (x/y) with window/page bounds using
[anime.js v4](https://animejs.com/documentation/draggable/) `createDraggable()`. It
sits above the posts-grid (`z-index: 1`). Dragging uses CSS transforms, so it never
affects text wrapping or layout flow of other elements.

### Bounds (current behavior)

- **Left/right walls** = the edges of the viewport (`window.innerWidth`).
- **Top wall** = the top of the **page** (not the visible viewport).
- **Bottom wall** = the bottom of the **page** (`document.documentElement.scrollHeight`).
- `containerFriction: 1` hard-clamps the element at the walls while dragging, so it
  can never be dragged off-screen.
- `releaseContainerFriction: 0.8` makes a flick glide smoothly into a wall and settle
  there with a damped spring (see "Known bug" below — it does **not** yet visibly
  bounce *past* the wall).

The bounds are supplied as a function returning `[top, right, bottom, left]` translate
offsets relative to the element's initial position, recomputed on init/resize only.
Horizontal scroll offset (`scrollX`) is included for the left/right walls (no
horizontal scrolling on this site, so it is effectively 0).

## Files touched (all changes live on the `draggable-components` branch)

1. **`_layouts/default.html`** — added anime.js UMD bundle from jsDelivr CDN, with `defer`:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/animejs/dist/bundles/anime.umd.min.js" defer></script>
   ```

2. **`_layouts/home.html`** — inside the existing `DOMContentLoaded` handler:
   ```js
   const { createDraggable } = anime;
   const imgRect = img.getBoundingClientRect();
   const imgX = imgRect.left + window.scrollX;
   const imgY = imgRect.top + window.scrollY;
   createDraggable(img, {
     container: () => {
       const docH = document.documentElement.scrollHeight;
       const vw = window.innerWidth;
       const sx = window.scrollX;
       return [
         -imgY,
         vw - imgX - imgRect.width + sx,
         docH - imgY - imgRect.height,
         -imgX + sx,
       ];
     },
     containerFriction: 1,
     releaseContainerFriction: 0.8,
   });
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

**Option B — stay on this branch and undo the changes.** The edits are in
`_layouts/default.html`, `_layouts/home.html`, `_sass/_home.scss`:

```bash
git checkout gh-pages -- _layouts/default.html _layouts/home.html _sass/_home.scss
```

To rebuild after reverting: `bundle exec jekyll build`

## Notes

- The anime.js CDN script is loaded on **every** page (it was added to the global
  `default.html` layout), so other pages still fetch it even though only the homepage
  uses it. Removing the script tag from `_layouts/default.html` eliminates that too.
- This report file (`docs/draggable-feature-report.md`) is documentation only and has
  no effect on the site; delete it if you don't want it in the revert.

## Known bug: release bounce does not overshoot the wall (WIP)

**Goal:** on a fast flick toward a wall, the headshot should visibly bounce *past* the
wall and settle back onto it.

**Current actual behavior (verified in a headless Chrome + CDP test):** on release the
element glides to the wall and settles exactly AT it (damped). It never visibly
overshoots past the wall, so there is no visible "bounce".

**What was verified working:**
- Hard containment on all four walls during drag (`containerFriction: 1`): the element
  stays within `[scrollX, scrollX + innerWidth]` horizontally and `[0, scrollHeight]`
  vertically at all times while dragged.
- A flick releases with captured velocity (`this.velocity` ≈ 11.7 px/ms for a fast
  synthetic flick) and the element animates to the wall over ~1.1–1.4 s.

**Root-cause analysis (from anime.js v4 source, master + the v4.5.0 UMD on CDN):**
1. The release-overshoot path only runs when `!hasReleaseSpring && isOutOfBounds && (durationX || durationY)`. When released while already touching the wall, `dest === current` so `durationX/durationY === 0` and the overshoot path is skipped entirely (no bounce when pushing against a wall).
2. When released mid-air toward a wall, the overshoot path *does* run — it animates
   `overshootCoords` to `bx` (past the wall) then back to `dx` (the wall) using two
   blended animations (`composition: blend`). Empirically the blended value never
   exceeds the wall (`overshootCoords.y` peaked exactly at the wall in testing), so no
   visible overshoot is produced.
3. The default release spring (`releaseStiffness: 80`, `releaseDamping: 20`, `releaseMass: 1`)
   has damping ratio ζ ≈ 1.12 — **overdamped** — so the spring-settle ease also never
   overshoots.

**Suggested next steps (unfinished):**
- Try an **underdamped** release spring via the `releaseEase` param (a spring object is
  detected via its `.ease` property, which sets `hasReleaseSpring`):
  `releaseEase: anime.spring({ mass: 1, stiffness: 200, damping: 20 })`
  (ζ ≈ 0.71 → oscillates). Verify whether the spring-ease path produces a visible
  bounce past the wall and settles back; tune `stiffness`/`damping` for feel.
- If the `blend` overshoot path is preferred, investigate anime.js v4's
  `compositionTypes.blend` for the `overshootCoords` animations to make `bx` visibly
  exceed the wall.
- Re-run the CDP drag test (harness: `/var/folders/sn/56xvvtb5667fmg2m_307jbj00000gn/T/opencode/dragtest.mjs`,
  headless Chrome on `:9222`, Jekyll serve on `:4001`) — the `flick-left`/`flick-down`
  cases assert that the element's edge goes past the wall (`> vw + 15` / `> docH + 30`)
  then settles back within 15px of the wall.
