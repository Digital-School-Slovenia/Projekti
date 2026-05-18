<?php

// ==================================================
// LOKALNE SPREMENLJIVKE
// ==================================================
// Lokalna spremenljivka je ustvarjena znotraj funkcije
// in jo lahko uporabljamo samo tam.

function primerLokalne() {

    $ime = "Marko";

    echo $ime;

}

primerLokalne();

echo "<br>";



// ==================================================
// GLOBALNE SPREMENLJIVKE
// ==================================================
// Globalna spremenljivka je ustvarjena zunaj funkcije.
// Znotraj funkcije jo uporabimo z besedo global.

$stevilo = 10;

function primerGlobalne() {

    global $stevilo;

    echo $stevilo;

}

primerGlobalne();

echo "<br>";



// ==================================================
// STATIČNE SPREMENLJIVKE
// ==================================================
// Statična spremenljivka ohrani svojo vrednost
// tudi po koncu funkcije.

function stevec() {

    static $x = 0;

    echo $x;

    $x++;

    echo "<br>";

}

stevec();
stevec();
stevec();

?>