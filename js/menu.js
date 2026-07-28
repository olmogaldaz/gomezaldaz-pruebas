document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('site-header');
  if (!header) return;

  const toggle = header.querySelector('.menu-toggle');
  const nav = header.querySelector('.main-nav');

  if (toggle && nav) {
    const isSpanish = document.documentElement.lang === 'es';

    const setMenuState = (isOpen) => {
      nav.classList.toggle('open', isOpen);
      toggle.textContent = isOpen ? '✕' : '☰';
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.setAttribute(
        'aria-label',
        isOpen
          ? (isSpanish ? 'Cerrar menú' : 'Close menu')
          : (isSpanish ? 'Abrir menú' : 'Open menu')
      );
    };

    toggle.addEventListener('click', () => {
      setMenuState(!nav.classList.contains('open'));
    });

    document.addEventListener('click', (event) => {
      if (nav.classList.contains('open') && !header.contains(event.target)) {
        setMenuState(false);
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('open')) {
        setMenuState(false);
        toggle.focus();
      }
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