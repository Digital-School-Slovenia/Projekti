<?php

// ==================================================
// ARRAY FUNKCIJE V PHP
// ==================================================
// PHP vsebuje veliko funkcij za delo z arrayi.

$numbers = array(10, 20, 30, 40);



// ==================================================
// COUNT()
// ==================================================
// count() prešteje koliko elementov je v arrayu.

echo count($numbers);

echo "<br>";



// ==================================================
// END()
// ==================================================
// end() vrne zadnji element arraya.

echo end($numbers);

echo "<br>";



// ==================================================
// ARRAY_PUSH()
// ==================================================
// array_push() doda element na konec arraya.

array_push($numbers, 50);

print_r($numbers);

echo "<br>";



// ==================================================
// ARRAY_POP()
// ==================================================
// array_pop() odstrani zadnji element arraya.

array_pop($numbers);

print_r($numbers);

echo "<br>";



// ==================================================
// ARRAY_UNSHIFT()
// ==================================================
// array_unshift() doda element na začetek arraya.

array_unshift($numbers, 5);

print_r($numbers);

echo "<br>";



// ==================================================
// ARRAY_SHIFT()
// ==================================================
// array_shift() odstrani prvi element arraya.

array_shift($numbers);

print_r($numbers);

echo "<br>";



// ==================================================
// ARRAY_SLICE()
// ==================================================
// array_slice() vrne del arraya.

$newArray = array_slice($numbers, 1, 2);

print_r($newArray);

echo "<br>";



// ==================================================
// ARRAY_SUM()
// ==================================================
// array_sum() vrne vsoto vseh števil v arrayu.

echo array_sum($numbers);

?>