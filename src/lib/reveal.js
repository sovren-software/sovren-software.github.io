/**
 * Svelte action: adds 'visible' class when element enters viewport.
 * Usage: <div class="reveal" use:reveal>
 * Options: { threshold: 0.15 }
 */
export function reveal(node, options = {}) {
  const threshold = options.threshold ?? 0.15;

  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold }
  );

  observer.observe(node);

  return {
    destroy() {
      observer.disconnect();
    },
  };
}
