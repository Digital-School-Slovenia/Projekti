<?php

/*
Ustvari funkcijo, ki bo prejela neko število (naključno izbrano – lahko ga določiš sam ali učitelj) in preverila:
če je število popolnoma deljivo z 2, naj funkcija izpiše, da je sodo število;
če ni deljivo z 2, naj izpiše, da je liho število.
*/

// definiramo funkcijo
function preveriStevilo($stevilo) {

    if ($stevilo % 2 == 0) {
        echo "$stevilo je sodo število.";
    } else {
        echo "$stevilo je liho število.";
    }

}

// klic funkcije
preveriStevilo(7);

?>