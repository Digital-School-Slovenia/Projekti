<?php
require_once('config/config.php');

$id = $_GET['id'];

// pridobi podatke iz POST metode
$customerName = $_POST['customerName'];
$contactFirstName = $_POST['contactFirstName'];
$contactLastName  = $_POST['contactLastName'];
$city = $_POST['city'];
$phone = $_POST['phone'];

$stms = $pdo->prepare("
    UPDATE customers SET 
        customerName = :customerName,
        contactFirstName = :contactFirstName,
        contactLastName= :contactLastName,
        city = :city,
        phone = :phone
    WHERE customerNumber = :customerNumber
");

$stms->execute([
    'customerName' => $customerName,
    'contactFirstName' => $contactFirstName,
    'contactLastName' => $contactLastName,
    'city' => $city,
    'phone' => $phone,
    'customerNumber' => $_GET['id']
]);

header("Location: index.php");
exit;