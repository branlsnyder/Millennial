---
layout: page
title: Improvisation
category: performance
permalink: /improvisation
---

<div class="posts-grid">
{% for post in site.posts %}
{% if post.category == "performance"%}
{% include featured-post.html %}
{% endif %}
{% endfor %}
</div>