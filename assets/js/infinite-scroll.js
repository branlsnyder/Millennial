(() => {
  const { currentPage, totalPages, baseUrl } = window.__paginator;
  if (currentPage >= totalPages) return;

  const grid = document.querySelector(".posts-grid");
  const sentinel = document.getElementById("scroll-sentinel");
  if (!grid || !sentinel) return;

  let loading = false;
  let nextPage = currentPage + 1;

  function showLoading() {
    sentinel.classList.add("loading");
    sentinel.innerHTML = '<div class="loading-spinner"></div>';
  }

  function hideLoading() {
    sentinel.classList.remove("loading");
    sentinel.innerHTML = "";
  }

  async function loadNextPage() {
    if (loading || nextPage > totalPages) return;
    loading = true;
    showLoading();

    try {
      const url = `${baseUrl}/page${nextPage}/`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const html = await res.text();
      const doc = new DOMParser().parseFromString(html, "text/html");
      const newPosts = doc.querySelectorAll(".posts-grid article");
      if (newPosts.length === 0) {
        sentinel.remove();
        return;
      }

      newPosts.forEach((article) => grid.appendChild(article));
      nextPage++;

      if (nextPage > totalPages) {
        sentinel.remove();
      }
    } catch (err) {
      console.error("Infinite scroll error:", err);
      sentinel.innerHTML = '<p class="scroll-error">Failed to load more posts.</p>';
    } finally {
      loading = false;
      hideLoading();
    }
  }

  const observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) loadNextPage();
    },
    { rootMargin: "200px" }
  );

  observer.observe(sentinel);
})();
