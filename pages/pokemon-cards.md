---
layout: page
title: Pokemon Cards
permalink: /pokemon-cards
---

<style>
  :root {
    --pointer-x: 50%;
    --pointer-y: 50%;
    --card-scale: 1;
    --card-opacity: 0;
    --translate-x: 0px;
    --translate-y: 0px;
    --rotate-x: 0deg;
    --rotate-y: 0deg;
    --background-x: var(--pointer-x);
    --background-y: var(--pointer-y);
    --pointer-from-center: 0;
    --pointer-from-top: var(--pointer-from-center);
    --pointer-from-left: var(--pointer-from-center);
  }

  .card {
    --grain: url("{{ site.github.url }}/assets/img/pokemon/grain.webp");
    --glitter: url("{{ site.github.url }}/assets/img/pokemon/glitter.png");
  }
  .card[data-rarity="rare holo vmax"] .card__shine,
  .card[data-rarity="rare holo vmax"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/vmaxbg.jpg");
  }
  .card[data-rarity="rare ultra"][data-supertype="pokémon"] .card__shine,
  .card[data-rarity="rare ultra"][data-supertype="pokémon"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/illusion.png");
  }
  .card[data-rarity="radiant rare"] .card__shine,
  .card[data-rarity="radiant rare"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/trainerbg.png");
  }
  .card[data-rarity="rare holo vstar"] .card__shine,
  .card[data-rarity="rare holo vstar"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/ancient.png");
  }
  .card[data-rarity="rare rainbow"] .card__shine,
  .card[data-rarity="rare rainbow"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/illusion-mask.png");
  }
  .card[data-rarity="rare secret"] .card__shine,
  .card[data-rarity="rare secret"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/geometric.png");
  }
  .card[data-rarity="rare shiny"] .card__shine,
  .card[data-rarity="rare shiny"] .card__glare {
    --foil: url("{{ site.github.url }}/assets/img/pokemon/illusion.png");
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 3rem 1.5rem;
    justify-items: center;
    margin-top: 2rem;
  }
  .card-grid .card {
    width: 100%;
    max-width: 300px;
    pointer-events: auto;
  }
  .card-label {
    text-align: center;
    margin-top: 0.75rem;
    font-family: "Source Code Pro", monospace;
    font-size: 0.8rem;
    color: #666;
    letter-spacing: 0.02em;
  }
  .card-label strong {
    display: block;
    font-family: "Instrument Serif", serif;
    font-size: 1.05rem;
    color: #222;
    margin-bottom: 0.15rem;
  }
  .pokemon-cards-intro {
    max-width: 640px;
    line-height: 1.6;
    color: #444;
    margin-bottom: 2rem;
  }
  @media screen and (max-width: 600px) {
    .card-grid {
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 2rem 1rem;
    }
  }
</style>

<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/base.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/basic.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/reverse-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/regular-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/cosmos-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/amazing-rare.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/radiant-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/v-regular.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/v-full-art.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/v-max.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/v-star.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/rainbow-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/secret-rare.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/trainer-gallery-holo.css">
<link rel="stylesheet" href="{{ site.github.url }}/assets/css/pokemon-cards/cards/shiny-rare.css">

<p class="pokemon-cards-intro">
  Hover over a card to see the holographic shine effect. Click to flip.
  CSS effects by <a href="https://github.com/simeydotme/pokemon-cards-css" target="_blank" rel="noopener">Simon Goellner</a>.
</p>

<div class="card-grid">

  <div>
    <div class="card interactive" data-rarity="common" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.3;--seedy:0.7;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/bulbasaur-common.png" alt="Bulbasaur Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Bulbasaur</strong>Common</div>
  </div>

  <div>
    <div class="card lightning" data-rarity="common" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.6;--seedy:0.2;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/pikachu-common.png" alt="Pikachu Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Pikachu</strong>Common</div>
  </div>

  <div>
    <div class="card water" data-rarity="rare holo" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.8;--seedy:0.4;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/articuno-rare-holo.png" alt="Articuno Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Articuno</strong>Rare Holo</div>
  </div>

  <div>
    <div class="card psychic" data-rarity="rare holo" data-supertype="pokémon" data-subtypes="stage 2"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.1;--seedy:0.9;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/gengar-rare-holo.png" alt="Gengar Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Gengar</strong>Rare Holo</div>
  </div>

  <div>
    <div class="card lightning" data-rarity="rare holo cosmos" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.5;--seedy:0.5;--cosmosbg:200px 400px;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/morpeko-cosmos-holo.png" alt="Morpeko Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Morpeko</strong>Cosmos Holo</div>
  </div>

  <div>
    <div class="card fire" data-rarity="radiant rare" data-supertype="pokémon" data-subtypes="basic radiant"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.4;--seedy:0.6;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/radiant-charizard.png" alt="Radiant Charizard Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Radiant Charizard</strong>Radiant Rare</div>
  </div>

  <div>
    <div class="card grass" data-rarity="amazing rare" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.7;--seedy:0.3;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/celebi-amazing-rare.png" alt="Celebi Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Celebi</strong>Amazing Rare</div>
  </div>

  <div>
    <div class="card dragon" data-rarity="rare holo v" data-supertype="pokémon" data-subtypes="basic v rapid strike"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.2;--seedy:0.8;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/rayquaza-v.png" alt="Rayquaza V Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Rayquaza V</strong>Rare Holo V</div>
  </div>

  <div>
    <div class="card psychic" data-rarity="rare ultra" data-supertype="pokémon" data-subtypes="basic v fusion strike"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.9;--seedy:0.1;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/mew-v-fullart.png" alt="Mew V Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Mew V</strong>Rare Ultra</div>
  </div>

  <div>
    <div class="card water" data-rarity="rare holo vmax" data-supertype="pokémon" data-subtypes="vmax rapid strike"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.45;--seedy:0.55;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/gyarados-vmax.png" alt="Gyarados VMAX Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Gyarados VMAX</strong>Rare Holo VMAX</div>
  </div>

  <div>
    <div class="card darkness" data-rarity="rare rainbow" data-supertype="pokémon" data-subtypes="vmax single strike"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.35;--seedy:0.65;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/umbreon-vmax-rainbow.png" alt="Umbreon VMAX Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Umbreon VMAX</strong>Rare Rainbow</div>
  </div>

  <div>
    <div class="card psychic" data-rarity="rare holo vstar" data-supertype="pokémon" data-subtypes="vstar"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.15;--seedy:0.85;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/mewtwo-vstar.png" alt="Mewtwo VSTAR Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Mewtwo VSTAR</strong>Rare Holo VSTAR</div>
  </div>

  <div>
    <div class="card colorless" data-rarity="rare secret" data-supertype="pokémon" data-subtypes="vstar"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.6;--seedy:0.4;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/arceus-vstar-secret.png" alt="Arceus VSTAR Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Arceus VSTAR</strong>Rare Secret</div>
  </div>

  <div>
    <div class="card fire" data-rarity="trainer gallery rare holo" data-supertype="pokémon" data-subtypes="stage 2" data-trainer-gallery="true"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.75;--seedy:0.25;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/charizard-tg.png" alt="Charizard Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Charizard</strong>Trainer Gallery Holo</div>
  </div>

  <div>
    <div class="card colorless" data-rarity="rare shiny" data-supertype="pokémon" data-subtypes="basic"
      style="--pointer-x:50%;--pointer-y:50%;--card-scale:1;--card-opacity:0;--translate-x:0px;--translate-y:0px;--rotate-x:0deg;--rotate-y:0deg;--background-x:50%;--background-y:50%;--pointer-from-center:0;--pointer-from-top:0.5;--pointer-from-left:0.5;">
      <div class="card__translater">
        <button class="card__rotator" tabindex="0">
          <img class="card__back" src="https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg" alt="Pokemon card back" width="660" height="921" />
          <div class="card__front" style="--seedx:0.55;--seedy:0.45;">
            <img src="{{ site.github.url }}/assets/img/pokemon/cards/minccino-shiny.png" alt="Minccino Pokemon Card" width="660" height="921" />
            <div class="card__shine"></div>
            <div class="card__glare"></div>
          </div>
        </button>
      </div>
    </div>
    <div class="card-label"><strong>Minccino</strong>Rare Shiny</div>
  </div>

</div>

<script>
(function() {
  function clamp(val, min, max) {
    return Math.min(Math.max(val, min === undefined ? 0 : min), max === undefined ? 1 : max);
  }
  function round(val) {
    return Math.round(val * 100) / 100;
  }
  function adjust(val, inMin, inMax, outMin, outMax) {
    return ((val - inMin) / (inMax - inMin)) * (outMax - outMin) + outMin;
  }

  document.querySelectorAll('.card').forEach(function(card) {
    var rotator = card.querySelector('.card__rotator');
    if (!rotator) return;
    var rafId = null;
    var pending = null;

    function updateSprings(bg, rot, glr) {
      card.style.setProperty('--background-x', bg.x + '%');
      card.style.setProperty('--background-y', bg.y + '%');
      card.style.setProperty('--rotate-x', rot.x + 'deg');
      card.style.setProperty('--rotate-y', rot.y + 'deg');
      card.style.setProperty('--pointer-x', glr.x + '%');
      card.style.setProperty('--pointer-y', glr.y + '%');
      card.style.setProperty('--pointer-from-center', glr.fmc);
      card.style.setProperty('--pointer-from-top', glr.y / 100);
      card.style.setProperty('--pointer-from-left', glr.x / 100);
      card.style.setProperty('--card-opacity', glr.o);
    }

    function interact(e) {
      if (e.type === 'touchmove') {
        e.clientX = e.touches[0].clientX;
        e.clientY = e.touches[0].clientY;
      }
      var rect = rotator.getBoundingClientRect();
      var px = clamp(round((100 / rect.width) * (e.clientX - rect.left)));
      var py = clamp(round((100 / rect.height) * (e.clientY - rect.top)));
      var cx = px - 50;
      var cy = py - 50;
      var fmc = clamp(Math.sqrt(cx * cx + cy * cy) / 50, 0, 1);

      pending = {
        bg: { x: adjust(px, 0, 100, 37, 63), y: adjust(py, 0, 100, 33, 67) },
        rot: { x: round(-cx / 3.5), y: round(cy / 3.5) },
        glr: { x: px, y: py, o: 1, fmc: fmc }
      };

      if (rafId === null) {
        rafId = requestAnimationFrame(function() {
          if (pending) {
            updateSprings(pending.bg, pending.rot, pending.glr);
            pending = null;
          }
          rafId = null;
        });
      }
    }

    function interactEnd() {
      if (rafId !== null) { cancelAnimationFrame(rafId); rafId = null; }
      pending = null;
      setTimeout(function() {
        card.style.setProperty('--card-opacity', '0');
        card.style.setProperty('--rotate-x', '0deg');
        card.style.setProperty('--rotate-y', '0deg');
        card.style.setProperty('--pointer-x', '50%');
        card.style.setProperty('--pointer-y', '50%');
        card.style.setProperty('--background-x', '50%');
        card.style.setProperty('--background-y', '50%');
        card.style.setProperty('--pointer-from-center', '0');
      }, 100);
    }

    rotator.addEventListener('pointermove', interact);
    rotator.addEventListener('pointerleave', interactEnd);
    rotator.addEventListener('touchmove', interact, { passive: true });
    rotator.addEventListener('touchend', interactEnd);
  });
})();
</script>
