---
layout: page
title: Teaching
category: workshops
permalink: /teaching
---
## Subjects
<span class="keywordrand">Composition</span>,
<span class="keywordrand">Digital Signal Processing</span>,
<span class="keywordrand">Recording Technology</span>,
<span class="keywordrand">Algorithmic Composition</span>,
<span class="keywordrand">Web Audio</span>,
<span class="keywordrand">Internet Art</span>,
<span class="keywordrand">Music Theory</span>,
<span class="keywordrand">Post Tonal Theory</span>,
<span class="keywordrand">HTML+CSS+JavaScript</span>,
<span class="keywordrand">Instrument Design</span>,
<span class="keywordrand">Jazz Piano</span>,
<span class="keywordrand">Jazz Composition</span>,
<span class="keywordrand">Music Entreprenuership</span>,
<span class="keywordrand">Aural Skills</span>,
<span class="keywordrand">Podcasting</span>,
<span class="keywordrand">Max MSP</span>,
<span class="keywordrand">Ableton Live</span>,
<span class="keywordrand">Pro Tools</span>,
<span class="keywordrand">Logic</span>,
<span class="keywordrand">Reaper</span>,
<span class="keywordrand">Computer Basics</span>, and
<span class="keywordrand">Digital Literacy</span>.

## Experience
<div class="posts-tabular">
{% for post in site.posts %}
{% if post.categories contains "workshops"%}
<div class="tabular-entry">
  {%- if post.image -%}<img class="tabular-thumbnail" src="{{ site.url }}/assets/img/{{ post.image }}" alt="{{ post.title }}">{%- endif -%}
  <div class="tabular-text">
    <h3><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></h3>
    <p>{{ post.date | date: "%Y" }}{%- if post.subtitle -%} — {{ post.subtitle }}{%- endif -%}</p>
  </div>
</div>
{% endif %}
{% endfor %}
</div>


