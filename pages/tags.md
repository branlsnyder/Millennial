---
layout: page
title: Tags
permalink: /tags
---
<p id="tag-heading"></p>
<div class="posts-tabular" id="tag-posts">
{% for post in site.posts %}
<div class="tabular-entry"{% for tag in post.tags %} data-tag-{{ tag | slugify }}{% endfor %}>
  {%- if post.image -%}<img class="tabular-thumbnail" src="{{ site.url }}/assets/img/{{ post.image }}" alt="{{ post.title }}">{%- endif -%}
  <div class="tabular-text">
    <h3><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></h3>
    <p>{{ post.date | date: "%Y" }}{%- if post.subtitle -%} — {{ post.subtitle }}{%- endif -%}</p>
  </div>
</div>
{% endfor %}
</div>

<script>
(function() {
  var heading = document.getElementById('tag-heading');
  var entries = document.querySelectorAll('#tag-posts .tabular-entry');
  var hash = window.location.hash.replace('#', '').toLowerCase();

  if (hash) {
    heading.textContent = 'Tag: ' + hash.replace(/-/g, ' ');
    for (var i = 0; i < entries.length; i++) {
      entries[i].style.display = entries[i].hasAttribute('data-tag-' + hash) ? '' : 'none';
    }
  } else {
    heading.textContent = 'All tags';
  }
})();
</script>
