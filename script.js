// NAV scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// Mobile menu
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
hamburger.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});
function closeMobile() {
  mobileMenu.classList.remove('open');
}

// Scroll reveal
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });
reveals.forEach(el => observer.observe(el));

// Contact form
// Contact form -> WhatsApp
function handleForm(e) {
  e.preventDefault();

  const name =
    document.getElementById('name')?.value || '';

  const email =
    document.getElementById('email')?.value || '';

  const phone =
    document.getElementById('phone')?.value || '';

  const message =
    document.getElementById('message')?.value || '';

  const whatsappMessage = `
🌍 NEW EXPORT INQUIRY

👤 Name: ${name}

📧 Email: ${email}

📱 Phone: ${phone}

📝 Message:
${message}
`;

  const whatsappURL =
    `https://wa.me/918208468798?text=${encodeURIComponent(whatsappMessage)}`;

  window.open(whatsappURL, '_blank');

  const msg = document.getElementById('formMsg');
  if (msg) {
    msg.textContent = 'Opening WhatsApp...';
  }

  e.target.reset();
}
// Smooth active nav on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY + 120;
  sections.forEach(section => {
    const link = document.querySelector(`.nav-links a[href="#${section.id}"]`);
    if (!link) return;
    if (section.offsetTop <= scrollY && section.offsetTop + section.offsetHeight > scrollY) {
      document.querySelectorAll('.nav-links a').forEach(l => l.style.color = '');
      link.style.color = '#E8B85A';
    }
  });
});

// ── Scroll progress bar ──────────────────────────────────────────────────────
const progressBar = document.getElementById('progress-bar');
function updateProgress() {
  if (!progressBar) return;
  const scrolled = window.scrollY;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = (total > 0 ? (scrolled / total) * 100 : 0) + '%';
}
window.addEventListener('scroll', updateProgress, { passive: true });

// ── Back to top ──────────────────────────────────────────────────────────────
const bttBtn = document.getElementById('bttBtn');
window.addEventListener('scroll', () => {
  if (bttBtn) bttBtn.classList.toggle('visible', window.scrollY > 450);
}, { passive: true });
if (bttBtn) {
  bttBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// ── Animated stat counters ───────────────────────────────────────────────────
function runCounter(el) {
  if (el.dataset.counted) return;
  el.dataset.counted = 'true';
  const target = parseInt(el.dataset.target, 10);
  const suffix = el.dataset.suffix || '';
  if (isNaN(target)) return;
  const duration = 900;
  const start = performance.now();
  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.round(eased * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
    else el.classList.add('counted');
  }
  requestAnimationFrame(step);
}

const counterEls = document.querySelectorAll('.stat-num[data-target]');
if (counterEls.length) {
  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) runCounter(e.target); });
  }, { threshold: 0.5 });
  counterEls.forEach(el => counterObs.observe(el));
}

// ── Flip business card on click ──────────────────────────────────────────────
const bcardWrap = document.querySelector('.bcard-svg-wrap');
if (bcardWrap) {
  let flipped = false;
  bcardWrap.title = 'Click to flip card';
  bcardWrap.style.transition = 'transform 0.6s ease, box-shadow 0.4s ease';
  bcardWrap.addEventListener('click', () => {
    flipped = !flipped;
    bcardWrap.style.transform = flipped
      ? 'rotateY(180deg) translateY(-8px)'
      : 'rotateY(0deg)';
  });
}


// Close mobile menu on outside click
document.addEventListener('click', (e) => {
  if (mobileMenu && mobileMenu.classList.contains('open')) {
    if (!mobileMenu.contains(e.target) && !hamburger.contains(e.target)) {
      closeMobile();
    }
  }
});

// Lazy-highlight active nav section on load
updateProgress();

// ── Mobile accordion for Products / Powders ──────────────────────────────────
function toggleMobSection(el) {
  el.classList.toggle('open');
  const sub = el.nextElementSibling;
  if (sub && sub.classList.contains('mob-sub-links')) {
    sub.classList.toggle('open');
  }
}