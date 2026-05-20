

const spans = Array.from(document.querySelectorAll('span'));
console.log(spans);
const cas = [2800, 1600, 2400, 1400, 2200, 2800, 3000, 2400, 1800, 2000, 2400, 1600, 2000, 1200, 1000, 1400, 2800, 1600, 2400, 1400, 2200, 2800, 3000, 2400, 1800, 2000, 2400, 1600, 2000, 1200, 1000, 1400, 2400, 1800, 2000, 2400, 1600, 2000];

const color = "#fca2c1"
let i = 0

function applyColor (el, color) {
    el.classList.add('highlight');
    el.style.color = color;
}
function clearColor(el) {
    el.classList.remove('highlight');
    el.style.color = '';
}
function next() {
    spans.forEach(clearColor);
    const idx = i % spans.length;
    applyColor(spans[idx], color);
    i++;
    setTimeout(next, cas[idx % cas.length]);
    console.log(spans[idx]);

}
next();