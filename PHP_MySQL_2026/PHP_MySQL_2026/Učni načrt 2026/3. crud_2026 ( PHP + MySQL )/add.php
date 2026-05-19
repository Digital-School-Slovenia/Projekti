<!-- Add Customer Form -->
<?php
require_once('config/config.php'); // povezava do baze
require('functions/functionModule.php'); // funkcije

if (isset($_POST['customerNumber'], 
$_POST['customerName'], 
$_POST['contactFirstName'], 
$_POST['contactLastName'], 
$_POST['city'],  
$_POST['addressLine1'], 
$_POST['country'], 
$_POST['phone'])) {

    add_customer(
        $_POST['customerNumber'], 
        $_POST['customerName'],
        $_POST['contactFirstName'], 
        $_POST['contactLastName'], 
        $_POST['city'], 
        $_POST['addressLine1'], 
        $_POST['country'], 
        $_POST['phone']
    );

    echo "Customer added!";
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style/style.css">
</head>
<body>
    <form action="" method="POST">
    <label for="customerNumber">Customer Number:</label>
    <input type="text" id="customerNumber" name="customerNumber" required>

    <label for="customerName">Customer Name:</label>
    <input type="text" id="customerName" name="customerName" required>

    <label for="contactFirstName">Contact First Name:</label>
    <input type="text" id="contactFirstName" name="contactFirstName" required>

    <label for="contactLastName">Contact Last Name:</label>
    <input type="text" id="contactLastName" name="contactLastName" required>

    <label for="city">City:</label>
    <input type="text" id="city" name="city" required>

    <label for="addressLine1">Address Line 1:</label>
    <input type="text" id="addressLine1" name="addressLine1" required>

    <label for="country">Country:</label>
    <input type="text" id="country" name="country" required>

    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone" required>

    <input type="submit" value="Add Customer">
</form>
</body>
</html>

