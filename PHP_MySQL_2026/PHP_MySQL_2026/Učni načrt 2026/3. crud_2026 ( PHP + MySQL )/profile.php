<?php
require_once('config/config.php'); // povezava do baze
require('functions/functionModule.php'); // funkcije

// preverimo ali je bil sploh poslan id h nam 
if (!isset($_GET['id'])) {
    die("Ni ID");
}

$id = $_GET['id'];
$customer = get_customer_by_id($id);
$order = get_customer_orders($id);
$payments = get_customer_payments($id);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="style/style.css">
    <link rel="stylesheet" href="style/style.css">
</head>

<body>

    <div class="container">
        <h2>Customer Profile</h2>

        <section>
            <div class="row">
                <span class="label">Customer Number:</span>
                <?= $customer['customerNumber'] ?>
            </div>

            <div class="row">
                <span class="label">Customer Name:</span>
                <?= $customer['customerName'] ?>
            </div>

            <div class="row">
                <span class="label">Phone:</span>
                <?= $customer['phone'] ?>
            </div>

            <div class="row">
                <span class="label">Address:</span>
                <?= $customer['addressLine1'] ?>
            </div>

            <div class="row">
                <span class="label">City:</span>
                <?= $customer['city'] ?>
            </div>

            <div class="row">
                <span class="label">Postal code:</span>
                <?= $customer['postalCode'] ?>
            </div>

            <div class="row">
                <span class="label">Country:</span>
                <?= $customer['country'] ?>
            </div>

            <div class="row">
                <span class="label">Credit Limit:</span>
                <?= $customer['creditLimit'] ?>
            </div>
        </section>

        <a href="edit.php?id=<?php echo $id ?>">Edit</a>
        <a href="delete.php?id=<?= $id ?>">Delete</a>
    </div>

    <div class="container">
        <h2>Orders</h2>

        <?php foreach ($order as $order) : ?>
            <hr>
            <div class="row">
                <span class="label">Order number:</span>
                <?= $order['orderNumber'] ?>
            </div>
            <div class="row">
                <span class="label">Order date:</span>
                <?= date_to_user_format($order['orderDate']) ?>
            </div>
            <div class="row">
                <span class="label">Order status:</span>
                <?= $order['status'] ?>
            </div>
            <div class="row">
                <span class="label">Order comments:</span>
                <?= $order['comments'] ?>
            </div>
            <hr>
        <?php endforeach; ?>

    </div>

    <div class="container">
        <h2>Payments</h2>

        <?php foreach ($payments as $payment) : ?>
            <hr>
            <div class="row">
                <span class="label">Check Number:</span>
                <?= $payment['checkNumber'] ?>
            </div>
            <div class="row">
                <span class="label">Payment Date:</span>
                <?= date_to_user_format($payment['paymentDate']) ?>
            </div>
            <div class="row">
                <span class="label">Amount:</span>
                <?= $payment['amount'] ?>
            </div>
            <hr>
        <?php endforeach; ?>

    </div>
</body>

</html>