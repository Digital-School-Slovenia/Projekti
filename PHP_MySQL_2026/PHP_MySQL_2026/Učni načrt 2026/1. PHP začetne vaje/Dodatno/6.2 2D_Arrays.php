<?php

// ==================================================
// MULTIDIMENZIONALNI ARRAY
// ==================================================
// Multidimenzionalni array je polje,
// ki vsebuje druga polja.
//
// Pogosto ga uporabljamo kot tabelo ali matriko.
//
// Za dostop do elementa potrebujemo:
// - prvi indeks = vrstica
// - drugi indeks = stolpec



// ==================================================
// PRIMER MULTIDIMENZIONALNEGA ARRAYA
// ==================================================

$students = array(

    array("Marko", 20, "Ljubljana"),
    array("Ana", 19, "Maribor"),
    array("Luka", 21, "Celje")

);



// ==================================================
// IZPIS POSAMEZNIH ELEMENTOV
// ==================================================

// Marko

echo $students[0][0];

echo "<br>";


// 19

echo $students[1][1];

echo "<br>";


// Celje

echo $students[2][2];

echo "<br>";



// ==================================================
// IZPIS CELOTNE TABELE Z ZANKO
// ==================================================

for ($i = 0; $i < count($students); $i++) {

    for ($j = 0; $j < count($students[$i]); $j++) {

        echo $students[$i][$j] . " ";

    }

    echo "<br>";

}

?>