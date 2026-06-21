const navbar = document.getElementById("navbar");
const hamburger = document.getElementById("hamburger");
const mobileMenu = document.getElementById("mobileMenu");
const progressBar = document.getElementById("progress-bar");
const backTop = document.getElementById("backTop");
const inquiryForm = document.getElementById("inquiryForm");
const formMsg = document.getElementById("formMsg");
const whatsappNumber = "917499770195";

function updateNav() {
  if (!navbar) return;
  navbar.classList.toggle("scrolled", window.scrollY > 40);
}

function updateProgress() {
  if (!progressBar) return;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  const percent = total > 0 ? (window.scrollY / total) * 100 : 0;
  progressBar.style.width = `${percent}%`;
}

function closeMobileMenu() {
  if (!mobileMenu || !hamburger || !navbar) return;
  mobileMenu.classList.remove("open");
  navbar.classList.remove("open");
  hamburger.setAttribute("aria-expanded", "false");
}

function openCategory(category) {
  document.querySelectorAll(".category-tab").forEach((tab) => {
    tab.classList.toggle("active", tab.dataset.category === category);
  });

  document.querySelectorAll(".product-panel").forEach((panel) => {
    panel.classList.toggle("active", panel.dataset.panel === category);
  });

  document.getElementById("products")?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function setInquiryCategory(category) {
  const select = document.getElementById("productCategory");
  const message = document.getElementById("message");

  if (select) {
    select.value = category;
  }

  if (message && !message.value.trim()) {
    message.value = `I want to request a product from ${category}. Please share availability, quality details, quantity options and sampling process.`;
  }

  document.getElementById("contact")?.scrollIntoView({ behavior: "smooth", block: "start" });
}

window.addEventListener("scroll", () => {
  updateNav();
  updateProgress();
  if (backTop) backTop.classList.toggle("visible", window.scrollY > 500);
}, { passive: true });

if (hamburger && mobileMenu && navbar) {
  hamburger.addEventListener("click", () => {
    const isOpen = mobileMenu.classList.toggle("open");
    navbar.classList.toggle("open", isOpen);
    hamburger.setAttribute("aria-expanded", String(isOpen));
  });

  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMobileMenu);
  });
}

document.addEventListener("click", (event) => {
  if (!mobileMenu || !hamburger || !mobileMenu.classList.contains("open")) return;
  if (!mobileMenu.contains(event.target) && !hamburger.contains(event.target)) {
    closeMobileMenu();
  }
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add("visible");
  });
}, { threshold: 0.14 });

document.querySelectorAll(".reveal").forEach((element) => {
  revealObserver.observe(element);
});

document.querySelectorAll(".category-tab").forEach((tab) => {
  tab.addEventListener("click", () => openCategory(tab.dataset.category));
});

document.querySelectorAll("[data-category-link]").forEach((link) => {
  link.addEventListener("click", () => openCategory(link.dataset.categoryLink));
});

document.querySelectorAll(".see-all-btn").forEach((button) => {
  button.addEventListener("click", () => {
    const panel = button.closest(".product-panel");
    if (!panel) return;
    const expanded = panel.classList.toggle("expanded");
    button.textContent = expanded ? "Show Less" : "See All";
  });
});

document.querySelectorAll(".request-btn").forEach((button) => {
  button.addEventListener("click", () => setInquiryCategory(button.dataset.request));
});

if (backTop) {
  backTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

if (inquiryForm) {
  inquiryForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.getElementById("name")?.value.trim() || "";
    const email = document.getElementById("email")?.value.trim() || "";
    const phone = document.getElementById("phone")?.value.trim() || "";
    const category = document.getElementById("productCategory")?.value || "";
    const message = document.getElementById("message")?.value.trim() || "";

    const whatsappMessage = [
      "New Vagmi Exim Product Inquiry",
      "",
      `Name: ${name}`,
      `Email: ${email}`,
      `Phone: ${phone}`,
      `Product Category: ${category}`,
      "",
      "Message:",
      message
    ].join("\n");

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(whatsappMessage)}`;
    window.open(url, "_blank", "noopener");

    if (formMsg) {
      formMsg.textContent = "Opening WhatsApp with your inquiry...";
    }
  });
}

updateNav();
updateProgress();
