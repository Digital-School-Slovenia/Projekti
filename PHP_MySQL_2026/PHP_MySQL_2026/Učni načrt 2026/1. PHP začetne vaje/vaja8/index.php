<?php
// Obrazec za prijavo uporabnika
?>

<!DOCTYPE html>
<html>
<head>
    <title>Prijava</title>
</head>
<body>

<h2>Prijava</h2>

<form action="welcome.php" method="POST">

    <label>Uporabniško ime:</label><br>
    <input type="text" name="username"><br><br>

    <label>Geslo:</label><br>
    <input type="password" name="password"><br><br>

    <input type="submit" value="Prijava">

</form>

</body>
</html>