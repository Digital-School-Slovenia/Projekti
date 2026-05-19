<?php

// ==================================================
// KAJ JE ARRAY?
// ==================================================
// Array (polje) shrani več vrednosti v eno spremenljivko.
//
// Namesto veliko posameznih spremenljivk uporabimo array.
//
// Indeksi v PHP se začnejo pri 0.



// ==================================================
// INDEXED ARRAY
// ==================================================
// Indexed array uporablja številčne indekse.

$colors = array("Red", "Blue", "Green");

// Izpis elementov

echo $colors[0];

echo "<br>";

echo $colors[1];

echo "<br>";



// ==================================================
// ASSOCIATIVE ARRAY
// ==================================================
// Associative array uporablja poimenovane ključe.

$student = array(
    "name" => "Marko",
    "age" => 20,
    "city" => "Ljubljana"
);

// Izpis vrednosti

echo $student["name"];

echo "<br>";

echo $student["city"];

echo "<br>";



// ==================================================
// MULTIDIMENSIONAL ARRAY
// ==================================================
// Multidimensional array vsebuje druge arraye.

$phones = array(

    array("Iphone 14", 20),
    array("Samsung S23", 15),
    array("Xiaomi 13", 10)

);

// Izpis podatkov

echo $phones[0][0];

echo "<br>";

echo $phones[1][1];

?>