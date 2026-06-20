---
layout: page
title: Scroll Card Demo
permalink: /scroll-demo
---

<style>
/* ---- demo page chrome ---- */
.scroll-demo-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 3rem 2rem;
  justify-content: center;
  margin-top: 2rem;
}
.scroll-demo-grid figure {
  margin: 0;
  text-align: center;
  width: 280px;
}
.scroll-demo-grid figcaption {
  margin-top: 0.75rem;
  font-family: "Source Code Pro", monospace;
  font-size: 0.85rem;
  color: #555;
}

/* ========== SCROLL CARD BASE ========== */

.scroll-card {
  position: relative;
  width: 260px;
  height: 360px;
  margin: 14px auto;
  border-radius: 8px 8px 6px 6px;
  overflow: hidden;

  /* subtle cylindrical shading overlay */
  &::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(
      to right,
      rgba(0,0,0,0.25) 0%,
      transparent 20%,
      transparent 80%,
      rgba(0,0,0,0.15) 100%
    );
    pointer-events: none;
    z-index: 1;
  }
}

.scroll-card img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* top rod */
.scroll-card::before {
  content: "";
  position: absolute;
  top: -10px;
  left: -6px;
  right: -6px;
  height: 20px;
  border-radius: 10px;
  background: linear-gradient(to bottom, #c89d6b, #8b6a3c, #c89d6b);
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
  z-index: 2;
}

/* bottom rod: use an extra element since we need two */
.scroll-card .scroll-rod-bottom {
  position: absolute;
  bottom: -10px;
  left: -6px;
  right: -6px;
  height: 20px;
  border-radius: 10px;
  background: linear-gradient(to top, #c89d6b, #8b6a3c, #c89d6b);
  box-shadow: 0 -2px 4px rgba(0,0,0,0.3);
  z-index: 2;
}

/* ========== VARIATIONS ========== */

/* -- tilt + perspective -- */
.scroll-card-perspective {
  transform: perspective(800px) rotateX(4deg) rotateY(-2deg);
  transition: transform 0.3s ease;
}
.scroll-card-perspective:hover {
  transform: perspective(800px) rotateX(0deg) rotateY(0deg);
}

/* -- more pronounced curl via border-radius -- */
.scroll-card-curl {
  border-radius: 30% 30% 6px 6px;
}

/* -- darker parchment overlay variant -- */
.scroll-card-parchment::after {
  background:
    linear-gradient(to right, rgba(0,0,0,0.3) 0%, transparent 20%, transparent 80%, rgba(0,0,0,0.2) 100%),
    radial-gradient(ellipse at center, rgba(245,235,200,0.15) 0%, transparent 70%);
}

/* --- content inside the card --- */
.scroll-card-content {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1rem;
  background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 50%);
  border-radius: inherit;
  z-index: 3;
  color: #fff;
}
.scroll-card-content h3 {
  margin: 0 0 0.25rem;
  font-size: 1.1rem;
  font-weight: 600;
  font-family: "Instrument Serif", serif;
}
.scroll-card-content p {
  margin: 0;
  font-size: 0.85rem;
  opacity: 0.9;
  font-family: "Alegreya", serif;
}
</style>

<div class="scroll-demo-grid">

<figure>
  <div class="scroll-card scroll-card-perspective">
    <img src="{{ site.github.url }}/assets/img/bppbch-thumbnail-2.jpg" alt="Bppbch">
    <div class="scroll-rod-bottom"></div>
    <div class="scroll-card-content">
      <h3>Bppbch</h3>
      <p>8 Instruments and Electronics</p>
    </div>
  </div>
  <figcaption>Base + perspective tilt</figcaption>
</figure>

<figure>
  <div class="scroll-card scroll-card-curl">
    <img src="{{ site.github.url }}/assets/img/brrrr-thumbnail.png" alt="brrrr">
    <div class="scroll-rod-bottom"></div>
    <div class="scroll-card-content">
      <h3>brrrr</h3>
      <p>Snare Drum and Delay Pedal</p>
    </div>
  </div>
  <figcaption>Curved top border-radius</figcaption>
</figure>

<figure>
  <div class="scroll-card scroll-card-perspective scroll-card-parchment">
    <img src="{{ site.github.url }}/assets/img/library-lion-1.png" alt="Library Lion">
    <div class="scroll-rod-bottom"></div>
    <div class="scroll-card-content">
      <h3>About</h3>
      <p>Warm parchment overlay</p>
    </div>
  </div>
  <figcaption>Parchment + perspective</figcaption>
</figure>

<figure>
  <div class="scroll-card scroll-card-perspective scroll-card-curl scroll-card-parchment">
    <img src="{{ site.github.url }}/assets/img/headshot-bare-1.png" alt="Headshot">
    <div class="scroll-rod-bottom"></div>
    <div class="scroll-card-content">
      <h3>Headshot</h3>
      <p>All effects combined</p>
    </div>
  </div>
  <figcaption>Everything together</figcaption>
</figure>

</div>
