<?php

// ==================================================
// KAJ SO FUNKCIJE?
// ==================================================
// Funkcije so deli kode, ki izvajajo določen namen.
//
// Funkcije lahko:
// - sprejemajo parametre
// - vračajo vrednosti
//
// Prednosti funkcij:
// - manj podvajanja kode
// - bolj pregledna koda
// - lažje reševanje problemov
// - ponovna uporaba kode



// ==================================================
// VGRAJENE FUNKCIJE (BUILT-IN)
// ==================================================
// To so funkcije, ki že obstajajo v PHP-ju.

// strlen() vrne dolžino besedila

$text = "Digital School";

echo strlen($text);

echo "<br>";


// strtoupper() pretvori besedilo v velike črke

echo strtoupper($text);

echo "<br>";



// ==================================================
// UPORABNIŠKO DEFINIRANE FUNKCIJE
// ==================================================
// Funkcije lahko ustvarimo tudi sami
// z uporabo besede function.

function pozdrav() {

    echo "Pozdravljen!";

}

pozdrav();

echo "<br>";



// ==================================================
// FUNKCIJA S PARAMETROM
// ==================================================
// Parameter je vrednost, ki jo pošljemo funkciji.

function izpisiIme($ime) {

    echo "Moje ime je $ime";

}

izpisiIme("Marko");

echo "<br>";



// ==================================================
// FUNKCIJA, KI VRAČA VREDNOST
// ==================================================
// return vrne rezultat funkcije.

function sestej($a, $b) {

    return $a + $b;

}

$rezultat = sestej(5, 3);

echo $rezultat;

?>