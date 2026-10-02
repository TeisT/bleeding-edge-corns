/* Bleeding Edge Corns – Interaktionen. Kein Framework. */
(() => {
  const html = document.documentElement;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const isDesktop = () => window.innerWidth >= 1024;
  // Headerhöhe + 1px = Position des klebenden Akkordeon-Kopfs
  const headerH = () => (parseFloat(getComputedStyle(html).getPropertyValue('--hh')) || 96) + 1;

  /* ---------------------------------------------------------- Header: Scrollzustand */
  const onScrollHeader = () => html.classList.toggle('is-scrolled', window.scrollY > 24);
  onScrollHeader();
  window.addEventListener('scroll', onScrollHeader, { passive: true });

  /* ---------------------------------------------------------- Burger-Menü */
  const burger = $('.burger');
  const menu = $('#mobile-menu');
  const setMenu = open => {
    if (!burger || !menu) return;
    html.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü');
    menu.hidden = !open;
  };
  if (burger) {
    burger.addEventListener('click', () => setMenu(!html.classList.contains('menu-open')));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && html.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });
    window.addEventListener('resize', () => { if (isDesktop()) setMenu(false); });
  }

  /* ---------------------------------------------------------- Sprach-Switch (EN-Inhalte noch offen) */
  $$('.lang').forEach(group => {
    const btns = $$('button', group);
    btns.forEach(b => b.addEventListener('click', () => btns.forEach(x => x.setAttribute('aria-pressed', String(x === b)))));
  });

  /* ---------------------------------------------------------- Reveal */
  const revealEls = $$('[data-reveal]');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const ease = 'cubic-bezier(0.2, 0.7, 0.2, 1)';
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target, d = +el.dataset.reveal || 0;
      io.unobserve(el);
      el.style.transition = `opacity 0.9s ${ease} ${d}ms, transform 0.9s ${ease} ${d}ms`;
      el.classList.add('is-in');
      // Danach transform komplett entfernen (Safari-Renderbug in Scroll-Containern)
      setTimeout(() => { el.removeAttribute('data-reveal'); el.classList.remove('is-in'); el.style.transition = ''; }, 900 + d + 100);
    }), { threshold: 0, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.removeAttribute('data-reveal'));
  }

  /* ---------------------------------------------------------- Horizontale Slider */
  const sliders = [];
  $$('[data-slider]').forEach(root => {
    const track = $('[data-track]', root);
    if (!track) return;
    const prev = $('[data-prev]', root), next = $('[data-next]', root);
    const bar = $('[data-bar]', root), thumb = bar && $('.sbar-thumb', bar);

    const measure = () => {
      const max = track.scrollWidth - track.clientWidth;
      // auf 0–1 begrenzen (iOS-Overscroll)
      const p = max > 0 ? Math.min(1, Math.max(0, track.scrollLeft / max)) : 0;
      const f = track.scrollWidth ? Math.min(1, track.clientWidth / track.scrollWidth) : 1;
      if (thumb) {
        thumb.style.width = (f * 100).toFixed(2) + '%';
        thumb.style.left = (p * (1 - f) * 100).toFixed(2) + '%';
        bar.setAttribute('aria-valuenow', String(Math.round(p * 100)));
      }
      if (prev) prev.classList.toggle('is-dim', p < 0.01);
      if (next) next.classList.toggle('is-dim', p > 0.99 || f >= 1);
    };
    const scrollByPage = d => track.scrollBy({ left: d * track.clientWidth * 0.75, behavior: 'smooth' });
    if (prev) prev.addEventListener('click', () => scrollByPage(-1));
    if (next) next.addEventListener('click', () => scrollByPage(1));
    track.addEventListener('scroll', measure, { passive: true });

    // Fortschrittsbalken ziehbar
    if (bar) {
      bar.addEventListener('pointerdown', e => {
        const f = track.clientWidth / track.scrollWidth;
        if (f >= 1) return;
        bar.setPointerCapture(e.pointerId);
        track.style.scrollSnapType = 'none';
        bar.classList.add('is-dragging');
        const move = ev => {
          const r = bar.getBoundingClientRect();
          const p = Math.min(1, Math.max(0, ((ev.clientX - r.left) / r.width - f / 2) / (1 - f)));
          track.scrollLeft = p * (track.scrollWidth - track.clientWidth);
        };
        const up = () => {
          track.style.scrollSnapType = '';
          bar.classList.remove('is-dragging');
          bar.removeEventListener('pointermove', move);
          bar.removeEventListener('pointerup', up);
          bar.removeEventListener('pointercancel', up);
        };
        move(e);
        bar.addEventListener('pointermove', move);
        bar.addEventListener('pointerup', up);
        bar.addEventListener('pointercancel', up);
      });
      bar.tabIndex = 0;
      bar.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight') { e.preventDefault(); scrollByPage(1); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); scrollByPage(-1); }
      });
    }
    sliders.push({ track, measure });
    measure();
    // Bilder laden nach → Breiten ändern sich
    $$('img', track).forEach(img => { if (!img.complete) img.addEventListener('load', measure, { once: true }); });
  });
  if (sliders.length) {
    window.addEventListener('resize', () => sliders.forEach(s => s.measure()));
    window.addEventListener('load', () => sliders.forEach(s => s.measure()));
    // Mausrad (Desktop): vertikales Rad scrollt horizontal, solange der Slider weiterkann
    let wheelT;
    window.addEventListener('wheel', ev => {
      if (!isDesktop()) return;
      const s = sliders.find(x => x.track.contains(ev.target));
      if (!s) return;
      const el = s.track;
      const dy = Math.abs(ev.deltaY) > Math.abs(ev.deltaX) ? ev.deltaY : 0;
      if (!dy) return;
      const max = el.scrollWidth - el.clientWidth;
      if ((dy < 0 && el.scrollLeft <= 0) || (dy > 0 && el.scrollLeft >= max - 1)) return;
      ev.preventDefault();
      el.style.scrollSnapType = 'none';
      el.scrollLeft += dy * (ev.deltaMode === 1 ? 40 : 1);
      clearTimeout(wheelT);
      wheelT = setTimeout(() => { el.style.scrollSnapType = ''; }, 180);
    }, { passive: false });
  }

  /* ---------------------------------------------------------- Galerie-Filter (Startseite) */
  $$('.gallery [role="tablist"]').forEach(list => {
    const root = list.closest('[data-slider]');
    const track = $('[data-track]', root);
    const tabs = $$('[data-filter]', list);
    tabs.forEach(tab => tab.addEventListener('click', () => {
      const cat = tab.dataset.filter;
      tabs.forEach(t => t.setAttribute('aria-selected', String(t === tab)));
      $$('.gfig', track).forEach(fig => { fig.hidden = !(cat === 'Alle' || fig.dataset.cat === cat); });
      track.scrollLeft = 0;
      const s = sliders.find(x => x.track === track);
      if (s) s.measure();
    }));
  });

  /* ---------------------------------------------------------- FAQ-Akkordeon (eins offen) */
  $$('[data-faq]').forEach(faq => {
    const items = $$('.faq-item', faq);
    items.forEach(item => {
      $('.faq-q', item).addEventListener('click', () => {
        const opening = !item.classList.contains('is-open');
        items.forEach(it => {
          const open = it === item && opening;
          it.classList.toggle('is-open', open);
          $('.faq-q', it).setAttribute('aria-expanded', String(open));
          $('.faq-a', it).hidden = !open;
        });
      });
    });
  });

  /* ---------------------------------------------------------- Themen-Akkordeon (Kornnatter) */
  $$('[data-topics]').forEach(list => {
    const topics = $$('.topic', list);
    const setOpen = (topic, open) => {
      topic.classList.toggle('is-open', open);
      topic.classList.remove('is-stuck');
      $('.topic-head', topic).setAttribute('aria-expanded', String(open));
      $('.topic-panel', topic).hidden = !open;
    };
    const checkStuck = () => {
      const t = topics.find(x => x.classList.contains('is-open'));
      if (!t) return;
      const b = $('.topic-head', t).getBoundingClientRect(), r = $('.topic-panel', t).getBoundingClientRect();
      t.classList.toggle('is-stuck', r.top < b.bottom - 2 && r.bottom > b.bottom);
    };
    topics.forEach(topic => {
      $('.topic-head', topic).addEventListener('click', () => {
        const opening = !topic.classList.contains('is-open');
        topics.forEach(t => setOpen(t, t === topic && opening));
        if (opening) {
          const top = topic.getBoundingClientRect().top;
          if (top < headerH()) window.scrollBy({ top: top - headerH(), behavior: 'smooth' });
        }
      });
      $('[data-close]', topic).addEventListener('click', () => {
        setOpen(topic, false);
        const top = topic.getBoundingClientRect().top;
        if (top < headerH()) window.scrollBy({ top: top - headerH() });
        $('.topic-head', topic).focus({ preventScroll: true });
      });
    });
    window.addEventListener('scroll', checkStuck, { passive: true });
    // Direktlink auf ein Thema (#haltung …) öffnet es
    const hash = decodeURIComponent(location.hash.slice(1));
    const target = hash && topics.find(t => t.id === hash);
    if (target) setOpen(target, true);
  });

  /* ---------------------------------------------------------- Kontaktformular */
  const form = $('[data-form]');
  if (form) {
    const box = form.parentElement;
    const success = $('[data-success]', box);
    const sendErr = $('[data-send-error]', form);
    const topicInput = form.elements.thema;
    const animalField = $('[data-animal-field]', form);
    const topicBtns = $$('[data-topic-btn]', form);
    topicBtns.forEach(b => b.addEventListener('click', () => {
      topicBtns.forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      topicInput.value = b.dataset.topicBtn;
      animalField.hidden = b.dataset.topicBtn !== 'Nachzucht';
    }));

    const setErr = (name, msg) => {
      const el = form.elements[name];
      const box = $(`[data-err="${name}"]`, form);
      if (el) el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (box) { box.hidden = !msg; $('span', box).textContent = msg || ''; }
    };
    form.addEventListener('input', e => {
      const n = e.target && e.target.name;
      if (n && $(`[data-err="${n}"]`, form)) setErr(n, '');
    });
    form.addEventListener('change', e => {
      if (e.target && e.target.name === 'consent') setErr('consent', '');
    });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      const v = k => (form.elements[k] && form.elements[k].value || '').trim();
      const er = {};
      if (!v('name')) er.name = 'Bitte gib deinen Namen ein.';
      if (!v('email')) er.email = 'Bitte gib deine E-Mail-Adresse ein.';
      else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))) er.email = 'Bitte gib eine gültige E-Mail-Adresse ein.';
      if (!v('msg')) er.msg = 'Bitte schreib uns eine Nachricht.';
      if (!form.elements.consent.checked) er.consent = 'Bitte stimme der Verarbeitung deiner Angaben zu.';
      ['name', 'email', 'msg', 'consent'].forEach(k => setErr(k, er[k] || ''));
      const first = Object.keys(er)[0];
      if (first) { form.elements[first].focus(); return; }

      sendErr.hidden = true;
      const btn = $('button[type="submit"]', form);
      btn.disabled = true;
      try {
        const fd = new FormData(form);
        if (animalField.hidden) fd.delete('tier');
        const res = await fetch(form.action, { method: 'POST', body: fd, headers: { Accept: 'application/json' } });
        const data = await res.json().catch(() => ({}));
        if (!res.ok || !data.ok) throw new Error('send');
        form.hidden = true;
        success.hidden = false;
        success.focus();
      } catch (_) {
        sendErr.hidden = false;
      } finally {
        btn.disabled = false;
      }
    });

    $('[data-reset]', box).addEventListener('click', () => {
      form.reset();
      topicBtns[0].click();
      ['name', 'email', 'msg', 'consent'].forEach(k => setErr(k, ''));
      success.hidden = true;
      form.hidden = false;
      form.elements.name.focus();
    });
  }

  /* ---------------------------------------------------------- Scrollspy (Impressum/Datenschutz) */
  const toc = $('[data-toc]');
  if (toc) {
    const links = $$('a', toc);
    const heads = links.map(a => document.getElementById(a.hash.slice(1))).filter(Boolean);
    const spy = () => {
      let cur = '';
      heads.forEach(h => { if (h.getBoundingClientRect().top <= 160) cur = h.id; });
      const doc = document.scrollingElement || html;
      if (heads.length && doc.scrollTop + window.innerHeight >= doc.scrollHeight - 4) cur = heads[heads.length - 1].id;
      links.forEach(a => a.classList.toggle('is-current', a.hash.slice(1) === cur));
    };
    spy();
    window.addEventListener('scroll', spy, { passive: true });
  }
})();
