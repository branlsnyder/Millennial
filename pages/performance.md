---
layout: page
title: Performance
category: performance
permalink: /performance
---

<div class="posts-grid">
{% for post in site.posts %}
{% if post.category == "performance"%}
{% include featured-post.html %}
{% endif %}
{% endfor %}
</div>