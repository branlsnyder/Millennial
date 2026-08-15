(function() {
  var header = document.querySelector('.site-header');
  if (!header) return;

  var SOLID_RGB = '26, 26, 26';
  var hero = document.querySelector('.hero');
  var heroHeight = 0;

  function measureHero() {
    heroHeight = hero ? hero.offsetHeight : 0;
  }

  function update() {
    if (!hero || heroHeight <= 0) {
      header.classList.remove('is-transparent');
      header.style.backgroundColor = '';
      return;
    }
    var progress = window.scrollY / heroHeight;
    progress = Math.max(0, Math.min(1, progress));
    if (progress >= 1) {
      header.classList.remove('is-transparent');
      header.style.backgroundColor = '';
    } else {
      header.classList.add('is-transparent');
      header.style.backgroundColor = 'rgba(' + SOLID_RGB + ', ' + progress.toFixed(3) + ')';
    }
  }

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function() {
      update();
      ticking = false;
    });
  }

  measureHero();
  update();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function() {
    measureHero();
    update();
  }, { passive: true });
})();
