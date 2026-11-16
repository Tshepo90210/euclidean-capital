/* ============================================================================
   EUCLIDEAN CAPITAL — brand behaviour
   ---------------------------------------------------------------------------
   The firm's own film: it plays muted, it loops, and it always has a control
   (a moving picture that lasts has to be pausable). Under reduced motion it
   rests as its poster.
   ========================================================================== */

for (const control of document.querySelectorAll('[data-film-toggle]')) {
  const section = control.closest('section, .band, .hero') || document;
  const film = section.querySelector('video');
  if (!film) continue;

  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const roomy = matchMedia('(min-width: 1024px)');

  const state = (playing) => {
    control.classList.toggle('is-paused', !playing);
    control.setAttribute('aria-label', playing ? 'Pause the film' : 'Play the film');
  };

  control.addEventListener('click', async () => {
    if (film.paused) {
      try { await film.play(); } catch { return; }
      state(true);
    } else {
      film.pause();
      state(false);
    }
  });

  film.addEventListener('play', () => state(true));
  film.addEventListener('pause', () => state(false));

  const sync = () => {
    if (reduced.matches) {
      film.pause();
      state(false);
    } else if (roomy.matches) {
      film.play().then(() => state(true)).catch(() => state(false));
    } else {
      state(!film.paused);
    }
  };
  sync();
  reduced.addEventListener('change', sync);
  roomy.addEventListener('change', sync);
}
