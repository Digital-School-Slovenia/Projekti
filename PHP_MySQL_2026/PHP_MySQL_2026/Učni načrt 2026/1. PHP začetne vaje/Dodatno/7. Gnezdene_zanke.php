<?php

// ==================================================
// VGNEZDENE ZANKE
// ==================================================
// Vgnezdena zanka pomeni,
// da imamo eno zanko znotraj druge.
//
// Najpogosteje uporabljamo:
// FOR zanko znotraj FOR zanke.
//
// Kako deluje:
// 1. Zunanja zanka se izvede enkrat.
// 2. Notranja zanka se izvede v celoti.
// 3. Nato se zunanja zanka premakne naprej.
// 4. Postopek se ponavlja.



// ==================================================
// PRIMER VGNEZDENE FOR ZANKE
// ==================================================

for ($i = 1; $i <= 3; $i++) {

    echo "Vrstica $i <br>";

    for ($j = 1; $j <= 3; $j++) {

        echo "Stolpec $j <br>";

    }

    echo "<br>";

}



// ==================================================
// IZPIS ZVEZDIC
// ==================================================
// Primer uporabe vgnezdenih zank.

for ($i = 1; $i <= 5; $i++) {

    for ($j = 1; $j <= $i; $j++) {

        echo "* ";

    }

    echo "<br>";

}

?>