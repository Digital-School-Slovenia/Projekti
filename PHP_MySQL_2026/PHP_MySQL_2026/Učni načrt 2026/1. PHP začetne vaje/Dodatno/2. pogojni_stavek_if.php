<?php

// ==================================================
// IF STAVEK
// ==================================================
// IF uporabimo, kadar želimo izvesti kodo samo,
// če je pogoj resničen (true).

$number = 10;

if ($number > 5) {

    echo "Število je večje od 5.<br>";

}



// ==================================================
// IF ELSE
// ==================================================
// IF ELSE uporabimo, kadar želimo eno kodo izvesti,
// če je pogoj true, drugo pa če je false.

$age = 16;

if ($age >= 18) {

    echo "Polnoleten si.<br>";

} else {

    echo "Nisi polnoleten.<br>";

}



// ==================================================
// IF ELSEIF ELSE
// ==================================================
// ELSEIF uporabimo, kadar imamo več različnih pogojev.

$grade = 4;

if ($grade == 5) {

    echo "Odlično!<br>";

} elseif ($grade == 4) {

    echo "Prav dobro!<br>";

} elseif ($grade == 3) {

    echo "Dobro.<br>";

} else {

    echo "Poskusi ponovno.<br>";

}



// ==================================================
// SWITCH
// ==================================================
// SWITCH uporabimo, kadar preverjamo veliko različnih
// vrednosti iste spremenljivke.

$day = 2;

switch ($day) {

    case 1:
        echo "Ponedeljek";
        break;

    case 2:
        echo "Torek";
        break;

    case 3:
        echo "Sreda";
        break;

    default:
        echo "Neznan dan";
}

?>