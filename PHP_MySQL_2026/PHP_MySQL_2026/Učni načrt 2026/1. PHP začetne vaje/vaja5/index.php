<?php

/*Napišite funkcijo PHP, ki kot vhod sprejme polje nizov in vrne novo polje, ki vsebuje samo edinstvene nize, tj. odstrani vse podvojene nize. Za filtriranje podvojenih nizov uporabite vgrajene funkcije za polja, kot je array_unique, ali zanko skozi polje.
PRED: Array ( [0] => apple [1] => banana [2] => apple [3] => orange [4] => banana )
PO: Array ( [0] => apple [1] => banana [3] => orange )
*/

function odstraniPodvojene($polje) {

    return array_unique($polje);

}

$sadje = array("apple", "banana", "apple", "orange", "banana");

echo "PRED:\n";
print_r($sadje);

$novoPolje = odstraniPodvojene($sadje);

echo "\nPO:\n";
print_r($novoPolje);

?>