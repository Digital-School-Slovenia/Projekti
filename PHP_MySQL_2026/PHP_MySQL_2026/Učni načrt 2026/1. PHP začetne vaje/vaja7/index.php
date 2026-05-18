<?php

// Ustvari dvodimenzionalno polje s podatki o telefonih.
// Vsaka vrstica predstavlja en telefon.
// S pomočjo zank izpiši podatke v HTML tabeli.

$phones = array(
    array("Iphone 14", 20, 10),
    array("Iphone 13", 20, 20),
    array("Iphone 12", 20, 25),
    array("Iphone 11", 25, 40)
);

echo "<table border='1'>";

echo "<tr>";
echo "<th>Phones</th>";
echo "<th>In stock</th>";
echo "<th>Sold</th>";
echo "</tr>";

for ($i = 0; $i < count($phones); $i++) {

    echo "<tr>";

    for ($j = 0; $j < count($phones[$i]); $j++) {

        echo "<td>" . $phones[$i][$j] . "</td>";

    }

    echo "</tr>";
}

echo "</table>";

?>