document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('site-header');
  if (!header) return;

  const toggle = header.querySelector('.menu-toggle');
  const nav = header.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('open');
    });
  }

  // Mark active section in the menu
  const normalizePath = (p) => {
    if (!p) return '/';
    p = p.split('?')[0].split('#')[0];
    if (!p.endsWith('/')) p += '/';
    return p;
  };

  const currentPath = normalizePath(location.pathname);

  header.querySelectorAll('.main-nav a').forEach((a) => {
    const hrefPath = normalizePath(
      new URL(a.getAttribute('href'), location.origin).pathname
    );

    if (hrefPath === currentPath) {
      a.classList.add('active');
    }
  });
});
