// Spremenljivke za shranjevanje podatkov
let count = 0;  // trenutno število piškotov
let step = 1;   // koliko piškotov dobimo na klik

// Povezava s HTML elementom za prikaz rezultata
const score_display = document.getElementById("count");



// Funkcija, ki se sproži ob kliku na piškot
function cookie_click() {
    count = count + step; // prištejemo trenutni korak
    score_display.innerHTML = count; // zapišemo novo vrednost v HTML
}








// Funkcija za nakup prve nadgradnje
function buy_1() {
    if (count >= 10) {
        count = count - 10; // odštejemo ceno nadgradnje
        step = step + 1;    // povečamo moč klika
        score_display.innerHTML = count; // posodobimo napis na strani
        alert("Nadgradnja kupljena! Zdaj dobiš več piškotov na klik.");
    } else {
        alert("Nimaš dovolj piškotov! Potrebuješ jih vsaj 10.");
    }
}