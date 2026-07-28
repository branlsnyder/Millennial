(function() {
  var pool = ['keywordp','keywordo','keywordg','keywordb','keywordy','keywordc','keywordr'];
  var els = document.querySelectorAll('.keywordrand');
  var idx = 0;
  // Fisher-Yates shuffle
  for (var i = pool.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = pool[i]; pool[i] = pool[j]; pool[j] = tmp;
  }
  for (var i = 0; i < els.length; i++) {
    els[i].classList.add(pool[idx]);
    idx = (idx + 1) % pool.length;
  }
})();