<?php

/*Ustvari nov PHP program z imenom sestevanje.php.
Program naj uporabnika vpraša:
Vnesi število: 
Uporabi funkcijo fgets(STDIN) za branje vnosa in trim() za odstranitev odvečnih presledkov ali znakov za novo vrstico.
Z uporabo zanke for izračunaj vsoto vseh števil od 1 do vnesenega števila.
Na koncu izpiši rezultat, npr.:
Vsota števil od 1 do 5 je 15.
*/


echo "Vnesi število: ";

// fgets(STDIN) prebere uporabnikov vnos iz tipkovnice.
// Ko uporabnik pritisne ENTER, se zraven shrani še znak za novo vrstico (\n).
$stevilo = trim(fgets(STDIN));

$vsota = 0;

for ($i = 1; $i <= $stevilo; $i++) {
    $vsota = $vsota + $i;
}

echo "Vsota števil od 1 do $stevilo je $vsota.";

?>
