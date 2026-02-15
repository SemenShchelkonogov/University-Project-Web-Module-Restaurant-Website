document.addEventListener("DOMContentLoaded", () => {
    const images = [
      "/static/img/gallery1.png",
      "/static/img/gallery2.png",
      "/static/img/gallery3.png",
      "/static/img/gallery4.png"
    ];
  
    const imgEl = document.getElementById("galleryImage");
    const dotsWrap = document.getElementById("galleryDots");
    const prevBtn = document.querySelector(".gallery-btn.prev");
    const nextBtn = document.querySelector(".gallery-btn.next");
  
    if (!imgEl || !dotsWrap || !prevBtn || !nextBtn) return;
  
    let current = 0;
    let isAnimating = false;
    const FADE_MS = 350; 
  
    function renderDots() {
      dotsWrap.innerHTML = "";
      images.forEach((_, i) => {
        const dot = document.createElement("button");
        dot.type = "button";
        dot.className = "gallery-dot" + (i === current ? " active" : "");
        dot.addEventListener("click", () => {
          if (i === current) return;
          current = i;
          update();
        });
        dotsWrap.appendChild(dot);
      });
    }
  
    function update() {
      if (isAnimating) return;
      isAnimating = true;
  
      // fade out
      imgEl.classList.add("fade-out");
  
      setTimeout(() => {
        imgEl.src = images[current];
        renderDots();
  
        // fade in
        imgEl.onload = () => {
          imgEl.classList.remove("fade-out");
  
          // time of animation
          setTimeout(() => {
            isAnimating = false;
          }, FADE_MS);
        };
      }, FADE_MS);
    }
  
    prevBtn.addEventListener("click", () => {
      current = (current - 1 + images.length) % images.length;
      update();
    });
  
    nextBtn.addEventListener("click", () => {
      current = (current + 1) % images.length;
      update();
    });
  
    // for phone
    let startX = 0;
    imgEl.addEventListener("touchstart", (e) => {
      startX = e.touches[0].clientX;
    });
  
    imgEl.addEventListener("touchend", (e) => {
      const endX = e.changedTouches[0].clientX;
      const diff = endX - startX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) prevBtn.click();
        else nextBtn.click();
      }
    });
  
    // first rendering without blinking
    imgEl.src = images[current];
    renderDots();
  });


  document.addEventListener("DOMContentLoaded", () => {
    const menuImg = document.getElementById("menuHeroImage");
    const dotsWrap = document.getElementById("menuDots");
    if (!menuImg || !dotsWrap) return;
  
    const images = [
        "/static/img/caviar.jpg",
        "/static/img/crab.jpg",
        "/static/img/stroganoff.jpg",
        "/static/img/pelmeni.jpg",
        "/static/img/black_cod.jpg",
        "/static/img/ribeye.jpg"
      ];
  
    let current = 0;
  
    function renderDots() {
      dotsWrap.innerHTML = "";
      images.forEach((_, i) => {
        const dot = document.createElement("button");
        dot.type = "button";
        dot.className = "menu-dot" + (i === current ? " active" : "");
        dot.addEventListener("click", () => goTo(i));
        dotsWrap.appendChild(dot);
      });
    }
  
    function goTo(i){
      current = i;
      menuImg.classList.add("fade-out");
      setTimeout(() => {
        menuImg.src = images[current];
        menuImg.classList.remove("fade-out");
        renderDots();
      }, 220);
    }
  
    // arrows
    const prev = document.querySelector(".menu-arrow.prev");
    const next = document.querySelector(".menu-arrow.next");
  
    if (prev) prev.addEventListener("click", () => goTo((current - 1 + images.length) % images.length));
    if (next) next.addEventListener("click", () => goTo((current + 1) % images.length));
  
    renderDots();
  });
  
  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("bookingForm");
    const success = document.getElementById("bookingSuccess");
    if (!form || !success) return;
  
    form.addEventListener("submit", (e) => {
      e.preventDefault();
  
      // reset form fields
      form.reset();
  
      // show success message
      success.style.display = "block";
  
      // optional: auto-hide after a few seconds
      setTimeout(() => {
        success.style.display = "none";
      }, 6000);
    });
  });

  document.addEventListener("DOMContentLoaded", () => {
    const sub = document.querySelector(".dropdown-sub");
    const btn = document.querySelector(".dropdown-sub-btn");
    if (!sub || !btn) return;
  
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      sub.classList.toggle("open");
      const expanded = sub.classList.contains("open");
      btn.setAttribute("aria-expanded", expanded ? "true" : "false");
    });
  
    document.addEventListener("click", () => {
      sub.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    });
  });
  