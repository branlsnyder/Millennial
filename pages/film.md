---
layout: page
title: Film/Video
category: film
permalink: /film
---
<div class="posts-tabular">
{% for post in site.posts %}
{% if post.categories contains "film"%}
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
