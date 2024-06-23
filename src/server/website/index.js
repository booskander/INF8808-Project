
const prevBtn = document.querySelector("div.prev-arrow");
const nextBtn = document.querySelector("div.next-arrow");
const sectionContainer = document.querySelector("div.carousel-sections");

prevBtn.onclick = prev;
nextBtn.onclick = next;

let currentIndex = 1;
let slides = [];
let dots = [];

function render() {
  let offset = 0;
  slides.forEach((slide, index) => {
    if (index < currentIndex) {
      offset += slide.offsetWidth;
    }
  });

  sectionContainer.style.transform = `translateX(-${offset}px)`;
  dots.forEach((dot, index) => {
    index === currentIndex
      ? dot.classList.add("active")
      : dot.classList.remove("active");
  });
}

function prev() {
  if (currentIndex <= 0) return;
  currentIndex -= 1;
  render();
}

function next() {
  if (currentIndex === slides.length - 1) return;
  currentIndex += 1;
  render();
}

function goto(newIndex) {
  if (newIndex < 0 || newIndex > slides.length - 1) return;
  currentIndex = newIndex;
  render();
}

function init() {
  const newSlides = document.querySelectorAll("div.carousel-sections > div");
  slides = newSlides;

  const newDots = document.querySelectorAll("div.carousel-dots > div");
  newDots.forEach((dot, index) => {
    dot.onclick = () => goto(index);
  });
  dots = newDots;

  const vis1 = document.getElementById("vis-1");
  const vis2 = document.getElementById("vis-2");
  const vis3 = document.getElementById("vis-3");
  

  [vis1, vis2, vis3].forEach((vis, idx) => {
    vis.onclick = () => {
      window.location.href = `pages/vis-${idx + 1}.html`;
    };
  });


  render();
}

init();
