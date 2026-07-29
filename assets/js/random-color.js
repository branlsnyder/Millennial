(function() {
  var pool = ['#edb2f1','#fab283','#00ceb9','#8cb0ff','#fcd53a','#93e9f6','#fc533a'];
  var idx = 0;
  // Fisher-Yates shuffle
  for (var i = pool.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = pool[i]; pool[i] = pool[j]; pool[j] = tmp;
  }
  var els = document.querySelectorAll('.colorrand');
  for (var i = 0; i < els.length; i++) {
    (function(el) {
      var originalColor = getComputedStyle(el).color;
      el.addEventListener('mouseenter', function() {
        el.style.color = pool[idx];
        idx = (idx + 1) % pool.length;
      });
      el.addEventListener('mouseleave', function() {
        el.style.color = originalColor;
      });
    })(els[i]);
  }
})();
