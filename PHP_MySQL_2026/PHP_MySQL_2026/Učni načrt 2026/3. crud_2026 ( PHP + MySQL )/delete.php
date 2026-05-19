<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        require_once('config/config.php');
        require('functions/functionModule.php');

        if (isset($_GET['id'])) {
            $customerId = $_GET['id'];
            // Call the function to delete the customer
            if (delete_customer($customerId)) {
                echo "Form submitted successfully!";
            } else {
                echo "Error deleting customer";
            }
        }

        header("Location: index.php");
    exit;
    ?>
</body>
</html>
