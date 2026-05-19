<?php
    require_once('config/config.php'); // povezava do baze
    require('functions/functionModule.php'); // funkcije

    // preverimo ali je bil sploh poslan id h nam 
    if (!isset($_GET['id'])) {
        die("Ni ID");
    }

    $id = intval($_GET['id']);

    $customer = get_customer_by_id($id);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit user (<?= $_GET['id'] ?>) </title>
    <link rel="stylesheet" href="style/style.css">
</head>
<body>
    <form action="update.php?id=<?php echo htmlspecialchars($_GET['id']); ?>" method="post">
        <input type="text" name="customerName" value="<?php echo htmlspecialchars($customer['customerName']); ?>">
        <input type="text" name="contactFirstName" value="<?php echo htmlspecialchars($customer['contactFirstName']); ?>">
        <input type="text" name="contactLastName" value="<?php echo htmlspecialchars($customer['contactLastName']); ?>">
        <input type="text" name="city" value="<?php echo htmlspecialchars($customer['city']); ?>">
        <input type="text" name="phone" value="<?php echo htmlspecialchars($customer['phone']); ?>">
        <button type="submit">Update</button>
    </form>
</body>
</html>