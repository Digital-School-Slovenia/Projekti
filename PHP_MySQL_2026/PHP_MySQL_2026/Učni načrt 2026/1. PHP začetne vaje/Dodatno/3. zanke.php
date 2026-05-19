<?php

// ==================================================
// KAJ SO ZANKE?
// ==================================================
// Zanke uporabljamo, ko želimo isti del kode
// izvesti večkrat.
//
// Namesto ponavljanja iste kode uporabimo zanko,
// ki ponavlja izvajanje, dokler je pogoj true.



// ==================================================
// WHILE ZANKA
// ==================================================
// WHILE izvaja kodo, dokler je pogoj resničen.

$number = 1;

while ($number <= 5) {

    echo "Število: $number <br>";

    $number++;

}



// ==================================================
// DO WHILE ZANKA
// ==================================================
// DO WHILE najprej izvede kodo enkrat,
// nato preveri pogoj.

$number = 1;

do {

    echo "Število: $number <br>";

    $number++;

} while ($number <= 5);



// ==================================================
// FOR ZANKA
// ==================================================
// FOR uporabljamo, kadar vemo,
// kolikokrat želimo ponoviti kodo.

for ($i = 1; $i <= 5; $i++) {

    echo "Število: $i <br>";

}



// ==================================================
// FOREACH ZANKA
// ==================================================
// FOREACH uporabljamo za delo s polji (arrays).
// Zanka gre skozi vsak element v polju.

$colors = array("Red", "Blue", "Green");

foreach ($colors as $color) {

    echo "$color <br>";

}

?>