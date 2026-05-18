<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style/style.css">

    <?php
    require_once('config/config.php');
    require('functions/functionModule.php')
    ?>

    <style>
        .deleteButton {
            background-color: red;
            color: white;
        }

        .editButton {
            background-color: orange;
            color: white;
        }

        .profileButton {
            background-color: blue;
            color: white;
        }
    </style>
</head>

<body>
    <nav>
        <a href="add.php"><button>Add new customer</button></a>
    </nav>
    <table>
        <thead>
            <th>CustName</th>
            <th>FirstName</th>
            <th>LastName</th>
            <th>City</th>
            <th>Phone</th>
            <th>Actions</th>
            <th></th>
            <th></th>
        </thead>
        <tbody>
            <?php
            $customers = get_all_customers();
            foreach ($customers as $customer) {
                echo "<tr>";
                echo "<td>" . htmlspecialchars($customer['customerNumber']) . "</td>";
                echo "<td>" . htmlspecialchars($customer['contactFirstName']) . "</td>";
                echo "<td>" . htmlspecialchars($customer['contactLastName']) . "</td>";
                echo "<td>" . htmlspecialchars($customer['city']) . "</td>";
                echo "<td>" . htmlspecialchars($customer['phone']) . "</td>";
                echo "<td>" . "<a href='edit.php?id=" . htmlspecialchars($customer['customerNumber']) . "'><button class='editButton'>Edit</button></a>" . "</td>";
                echo "<td>" . "<a href='delete.php?id=" . htmlspecialchars($customer['customerNumber']) . "'><button class='deleteButton'>Delete</button></a>" . "</td>";
                echo "<td>" . "<a href='profile.php?id=" . htmlspecialchars($customer['customerNumber']) . "'><button class='profileButton'>Profile</button></a>" . "</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>

</html>