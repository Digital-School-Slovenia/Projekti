<?php

/* Z uporabo FOR zank ( NESTED (gnezdimo)) nariši celo smrekco*/

for ($i = 1; $i < 5; $i++) {
    for ($j = $i; $j <= 5; $j++) {
        echo "&nbsp;"; // prazno mesto
    }
    for ($j = 1; $j <= $i; $j++) {

        echo " * ";
    }
    echo "<br />";
}
?>