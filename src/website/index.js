
const prevBtn = document.querySelector("div.prev-arrow");
const nextBtn = document.querySelector("div.next-arrow");
const sectionContainer = document.querySelector("div.carousel-sections");
const vis1 = document.getElementById("vis-1");
const vis2 = document.getElementById("vis-2");
const vis3 = document.getElementById("vis-3");
prevBtn.onclick = prev;
nextBtn.onclick = next;

var currentIndex = 0;
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
  resetCard();
  render();
}

function next() {
  if (currentIndex === slides.length - 1) return;
  currentIndex += 1;
  resetCard();
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

  

  [vis1, vis2, vis3].forEach((vis, idx) => {
    vis.onclick = () => {
      window.location.href = `pages/vis-${idx + 1}.html`;
    };
  });


  render();
}

init();

var isText = false;
var infoButton = document.getElementById("info-button");
var cards = [vis1, vis2, vis3];

infoButton.addEventListener('click', () => {
  updateCard();
});

function resetCard() {
  cards[currentIndex].classList.remove('text-displayed');
  cards[currentIndex].innerHTML = "";

}
function updateCard() {
  isText = cards[currentIndex].classList.contains("text-displayed");
  if (isText) {
    cards[currentIndex].classList.remove('text-displayed');
    cards[currentIndex].innerHTML = "";

  } else {
    cards[currentIndex].classList.add('text-displayed');
    cards[currentIndex].innerHTML = texts[currentIndex];

  }
}



var texts = { 0: `<div class="title">Italy's victory in Euro 2020 was driven by a combination of solid defense, strategic gameplay, and effective attack, as evidenced by their impressive statistics.</div>
    
    <div class="section-title">Key Statistics</div>
    <ul class="key-stats">
        <li class="content"><b>Total Attempts (128):</b> Italy's aggressive offensive strategy led to 128 total attempts on goal, putting constant pressure on opposing defenses.</li>
        <li class="content"><b>Attempts on Target (36):</b> With 36 shots on target, Italy consistently created quality scoring chances.</li>
        <li class="content"><b>Goals (13):</b> Scoring 13 goals, Italy's key players like Immobile, Chiesa, and Insigne effectively converted opportunities.</li>
        <li class="content"><b>Pass Accuracy (86.86%):</b> High pass accuracy ensured effective ball control and build-up play, allowing Italy to dominate the midfield.</li>
        <li class="content"><b>Avg Possession (%) (57.2%):</b> Dominating possession at 57.2% allowed Italy to control game tempo and impose their tactics.</li>
        <li class="content"><b>Goals Saved (9):</b> Donnarumma's 9 crucial saves were vital in maintaining a strong defense.</li>
        <li class="content"><b>Goals Conceded (4):</b> Conceding only 4 goals, Italy's robust defense, led by Bonucci and Chiellini, was a key factor in their success.</li>
        <li class="content"><b>Assists (11):</b> The 11 assists highlight Italy's teamwork and unselfish play, crucial for their attacking success.</li>
    </ul>

    <div class="section-title">Conclusion</div>
    <div class="content">Italy's balanced approach, combining effective offense, solid defense, and strategic control, set them apart from other teams and led them to win Euro 2020.</div>`,
  1:  ` <p class="title">Visualization 2 (Lineup-chart) :</p>

    <p class="highlight">Why This Lineup Stands Out</p>
    <p class="content">This lineup stands out from other teams in Euro 2020 due to its perfect balance of experience, youth, and tactical flexibility. The 4-3-3 formation provided a solid defensive base while allowing for dynamic attacking transitions. Unlike more rigid setups, Italy's 4-3-3 often morphed into different shapes depending on the phase of play, such as a 3-2-5 in attack or a 4-5-1 in defense, making them unpredictable and difficult to break down.</p>
    <p class="content">The versatility of players like Insigne and Chiesa, who could interchange positions and roles seamlessly, added an extra layer of complexity for opponents. Additionally, the midfield trio's ability to control the game, combined with the defensive robustness of Bonucci and Chiellini, ensured that Italy could both protect leads and mount effective counterattacks.</p>
    <p class="content">Overall, Italy's strategic use of the 4-3-3 formation, coupled with the unique qualities of their players, set them apart as the most well-rounded and tactically astute team in the tournament, ultimately leading them to lift the Euro 2020 trophy.</p>`,
  2: `
    <p class="title">Visualization 3 (tournament-chart) :</p>
    <p class="content">Italy's triumph in Euro 2020 was driven by consistent performances, strategic gameplay, and key contributions from experienced and emerging players.</p>

    <p class="highlight">Group Stage</p>
    <p class="content"><b>1. Strong Start:</b> Italy began with a 3-0 win against Turkey, setting a positive tone.</p>
    <p class="content"><b>2. Dominant Play:</b> Another 3-0 win over Switzerland showcased their attacking and defensive strength.</p>
    <p class="content"><b>3. Consistency:</b> A 1-0 victory over Wales secured maximum points, demonstrating effective game management.</p>

    <p class="highlight">Knockout Stages</p>
    <p class="content"><b>1. Resilience:</b> Italy overcame Austria 2-1 in extra time, showing depth and determination.</p>
    <p class="content"><b>2. Tactical Mastery:</b> They defeated Belgium 2-1 with disciplined tactics and key performances from players like Insigne and Barella.</p>
    <p class="content"><b>3. Mental Toughness:</b> Italy held their nerve against Spain, winning 4-2 in a penalty shootout after a 1-1 draw.</p>

    <p class="highlight">Final</p>
    <p class="content"><b>1. Team Spirit and Experience:</b> In the final against England, Italy's experience and team spirit were crucial. After a 1-1 draw, they won 3-2 in the penalty shootout, with key contributions from Bonucci and Donnarumma.</p>

    <p class="content">Italy's strategic excellence, teamwork, and ability to perform under pressure made them worthy Euro 2020 champions.</p>
  `
  }