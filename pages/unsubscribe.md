---
layout: page
title: Unsubscribe
permalink: /unsubscribe
---

<div class="newsletter-form">
  <h1>Unsubscribe</h1>
  <p>Enter the email address you'd like removed from my newsletter mailing list.</p>
  <form target="_blank" action="https://formsubmit.co/d525c817889d1f21cc68b1da541145bc" method="POST">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <input type="hidden" name="_subject" value="Newsletter unsubscribe">
    <input type="email" name="email" placeholder="Email Address" required>
    <button type="submit">Unsubscribe</button>
  </form>
  <p>I'll remove your email from the list shortly after receiving your request.</p>
</div>

<script>
(function() {
  var email = new URLSearchParams(window.location.search).get('email');
  if (email) {
    document.querySelector('.newsletter-form input[name="email"]').value = email;
  }
})();
</script>
