---
layout: page
title: Tags
permalink: /tags
---
<style>.page-content h1{display:none}#tag-heading{font-size:2rem;margin:20px 0 5px}</style>
<h2 id="tag-heading"></h2>
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
  // Get the URL hash (e.g., #instrument-design -> "instrument-design")
  // If no hash, show all posts with heading "All tags"

  if (hash) {
    heading.innerHTML = 'Stuff related to <span class="keywordrand">' + hash.replace(/-/g, ' ') + '</span>';
    // Replace hyphens with spaces for display: "instrument-design" -> "instrument design"
    // Hash text styled with .keywordg (teal color, hover font)
    for (var i = 0; i < entries.length; i++) {
      entries[i].style.display = entries[i].hasAttribute('data-tag-' + hash) ? '' : 'none';
      // Show only posts whose data-tag-* attribute matches the hash
    }
  } else {
    heading.textContent = 'All tags';
  }
})();
</script>
