---
layout: page
title: Workshops, Artistic Directing, Teaching
category: workshops
permalink: /workshops
---
Insert paragraph about teaching workshops and suc


<div class="posts-grid">
{% for post in site.posts %}
{% if post.category == "workshops"%}
{% include featured-post.html %}
{% endif %}
{% endfor %}
</div>


