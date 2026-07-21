---
layout: page
title: Composed Works
category: composition
permalink: /composition
---
<div class="posts-grid">
{% for post in site.posts %}
{% if post.categories contains "composition"%}
{% include featured-post.html %}
{% endif %}
{% endfor %}
</div>



