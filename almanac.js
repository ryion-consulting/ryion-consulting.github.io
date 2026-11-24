/* Ryion — the small amount of movement on the page.
   Everything here is decoration: with scripts off, the pages read the same. */
(() => {
  const calm = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Sections arrive as they scroll into view.
  const seen = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); seen.unobserve(e.target); }
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  document.querySelectorAll("[data-reveal]").forEach((el) => seen.observe(el));

  // App Store media is for review on this Mac: offer the link (and the videos) only where the
  // git-ignored _artifacts link resolves, i.e. on the local preview server.
  const review = document.querySelector(".review-link");
  const away = document.querySelector(".store-off");
  if (review) {
    fetch(new URL("_artifacts/README.txt", review.href), { method: "HEAD", cache: "no-store" })
      .then((r) => { if (r.ok) review.hidden = false; else if (away) away.hidden = false; })
      .catch(() => { if (away) away.hidden = false; });
  }

  if (calm) return;

  // The compass: its needle turns to the pointer, and the ring of ticks turns with the page.
  const rose = document.querySelector(".rose-svg");
  const needle = rose && rose.querySelector(".rose-needle");
  const ticks = rose && rose.querySelector(".rose-ticks");
  let target = -32, shown = -32, pointerSeen = false;

  if (rose) {
    addEventListener("pointermove", (e) => {
      if (e.pointerType === "touch") return;
      const r = rose.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      if (Math.hypot(dx, dy) < 12) return;
      target = Math.atan2(dx, -dy) * 180 / Math.PI;
      pointerSeen = true;
    }, { passive: true });
  }

  // Phones on the tinted plates drift a little against the scroll.
  const arts = [...document.querySelectorAll(".entry-art, .app-hero-art")];

  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      ticking = false;
      const y = scrollY, vh = innerHeight;
      if (ticks) ticks.style.transform = `rotate(${(y * 0.06).toFixed(2)}deg)`;
      if (!pointerSeen) target = -32 + y * 0.12;
      for (const a of arts) {
        const r = a.getBoundingClientRect();
        if (r.bottom < -50 || r.top > vh + 50) continue;
        const mid = (r.top + r.height / 2 - vh / 2) / vh; // -1 … 1 across the viewport
        a.style.setProperty("--y", `${(mid * -26).toFixed(1)}px`);
      }
    });
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (needle) {
    const swing = () => {
      // Turn the short way round, and ease into place like a damped needle.
      let d = ((target - shown + 540) % 360) - 180;
      shown += d * 0.08;
      needle.style.transform = `rotate(${shown.toFixed(2)}deg)`;
      requestAnimationFrame(swing);
    };
    needle.style.transition = "none";
    swing();
  }
})();
