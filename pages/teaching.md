---
layout: page
title: Teaching
category: workshops
permalink: /teaching
---
<div class="posts-tabular">
{% for post in site.posts %}
{% if post.category == "workshops"%}
<div class="tabular-entry">
  <h3><a href="{{ site.github.url }}{{ post.url }}">{{ post.title }}</a></h3>
  <p>{{ post.date | date: "%Y" }}{%- if post.subtitle -%} — {{ post.subtitle }}{%- endif -%}</p>
</div>
{% endif %}
{% endfor %}
</div>


