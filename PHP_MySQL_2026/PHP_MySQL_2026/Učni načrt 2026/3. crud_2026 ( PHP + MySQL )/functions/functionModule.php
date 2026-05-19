<?php
function get_all_customers()
{
    global $pdo;
    $stmt = $pdo->query("SELECT * FROM customers");
    return $stmt->fetchAll();
}

function get_customer_by_id($customerNumber): array
{
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM customers WHERE customerNumber = :customerNumber");
    $stmt->execute(['customerNumber' => $customerNumber]);
    return $stmt->fetch() ?: [];
}

function delete_customer($customerNumber): bool
{
    global $pdo;

    try {
        $pdo->beginTransaction();

        $stmt = $pdo->prepare("
            DELETE payments
            FROM payments
            JOIN customers ON payments.customerNumber = customers.customerNumber
            WHERE customers.customerNumber = :customerNumber
        ");
        $stmt->execute(['customerNumber' => $customerNumber]);

        // 1️⃣ Delete orderdetails
        $stmt = $pdo->prepare("
            DELETE od
            FROM orderdetails od
            JOIN orders o ON od.orderNumber = o.orderNumber
            WHERE o.customerNumber = :customerNumber
        ");
        $stmt->execute(['customerNumber' => $customerNumber]);

        // 2️⃣ Delete orders
        $stmt = $pdo->prepare("
            DELETE FROM orders
            WHERE customerNumber = :customerNumber
        ");
        $stmt->execute(['customerNumber' => $customerNumber]);

        // 3️⃣ Delete customer
        $stmt = $pdo->prepare("
            DELETE FROM customers
            WHERE customerNumber = :customerNumber
        ");
        $stmt->execute(['customerNumber' => $customerNumber]);

        $pdo->commit();
        return true;
    } catch (PDOException $e) {
        $pdo->rollBack();
        echo $e->getMessage();
        return false;
    }
}

function add_customer($customerNumber, $customerName, $contactFirstName, $contactLastName, $city, $addressLine1, $country, $phone){
    global $pdo;
    // V prvi oklepaj dajemo polja iz tabela v katera želimo vnesti podatek
    // V drugi oklepaj pa dajemo dejanske vrednosti (beri SPREMENLJIVKE/PARAMETRI)
    $stmt = $pdo->prepare("
    INSERT INTO customers
    (customerNumber, customerName, contactFirstName, contactLastName, city, addressLine1, country, phone)
    VALUES
    (:customerNumber, :customerName, :contactFirstName, :contactLastName, :city, :addressLine1, :country, :phone)
    ");

    return $stmt->execute([
        'customerNumber' => $customerNumber,
        'customerName' => $customerName,
        'contactFirstName' => $contactFirstName,
        'contactLastName' => $contactLastName,
        'city' => $city,
        'addressLine1' => $addressLine1,
        'country' => $country,
        'phone' => $phone
    ]);
}

function get_customer_orders($customerNumber): array
{
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM orders WHERE customerNumber = :customerNumber");
    $stmt->execute(['customerNumber' => $customerNumber]);
    return $stmt->fetchAll() ?: [];
}

function get_customer_payments($customerNumber): array
{
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM payments WHERE customerNumber = :customerNumber");
    $stmt->execute(['customerNumber' => $customerNumber]);
    return $stmt->fetchAll() ?: [];
}

function date_to_user_format($date){
    //return date('d:m:Y', strtotime($date));

    if (empty($date)) {
        return '';
    }
    try {
        $d = new DateTime($date);
        return $d->format('d:m:Y');
    } catch (Exception $e) {
        return $e;
    }
}