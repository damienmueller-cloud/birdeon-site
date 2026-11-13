/* Birdeon preview interactions */
(function () {
  const body = document.body;
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll("[data-drop]").forEach(function (drop) {
    const btn = drop.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      const isOpen = drop.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  });

  document.addEventListener("click", function (e) {
    document.querySelectorAll("[data-drop].is-open").forEach(function (drop) {
      if (!drop.contains(e.target)) {
        drop.classList.remove("is-open");
        const btn = drop.querySelector("button");
        if (btn) btn.setAttribute("aria-expanded", "false");
      }
    });
  });

  const modal = document.getElementById("notify-modal");
  function openModal(productName) {
    if (!modal) return;
    const title = modal.querySelector("[data-notify-title]");
    const field = modal.querySelector("[data-notify-product]");
    if (title) {
      title.textContent = productName
        ? "Notify me about " + productName
        : "Notify me when Birdeon is available";
    }
    if (field) field.value = productName || "Birdeon launch list";
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    const input = modal.querySelector('input[type="email"]');
    if (input) input.focus();
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
  }
  document.querySelectorAll("[data-open-notify]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      openModal(btn.getAttribute("data-open-notify") || "");
    });
  });
  if (modal) {
    modal.querySelectorAll("[data-close-modal]").forEach(function (el) {
      el.addEventListener("click", closeModal);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeModal();
    });
  }

  /* Visual-only forms: no backend, no network request. */
  document.querySelectorAll("[data-visual-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const success = form.parentElement.querySelector(".form-success") || form.querySelector(".form-success");
      form.reset();
      if (success) {
        success.classList.add("is-visible");
        success.setAttribute("tabindex", "-1");
        success.focus();
      }
      window.setTimeout(closeModal, 1400);
    });
  });

  const mainImg = document.querySelector("[data-gallery-main]");
  if (mainImg) {
    document.querySelectorAll("[data-thumb]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        const src = btn.getAttribute("data-src");
        const srcset = btn.getAttribute("data-srcset");
        const alt = btn.getAttribute("data-alt") || "";
        const webp = btn.getAttribute("data-webp");
        const source = document.querySelector("[data-gallery-webp]");
        if (webp && source) source.setAttribute("srcset", webp);
        if (srcset) mainImg.setAttribute("srcset", srcset);
        if (src) mainImg.setAttribute("src", src);
        mainImg.setAttribute("alt", alt);
        document.querySelectorAll("[data-thumb]").forEach(function (b) {
          b.classList.toggle("is-active", b === btn);
        });
      });
    });
  }
})();
