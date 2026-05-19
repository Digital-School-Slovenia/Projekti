<?php
// Ustvarite PHP skript, ki izračuna površino kroga. 
// Skript naj uporabnika pozove k polmeru kroga z uporabo funkcije readline() 
// in nato to vrednost uporabi za izračun površine. Formula za površino kroga je: A = pi * r^2.

$polmer = readline("Vnesi polmer kroga: ");

$povrsina = pi() * $polmer * $polmer;

echo "Površina kroga je: " . $povrsina;

?>