# SQL Začetne Poizvedbe 🚀

Praktični SQL primeri za začetnike — od osnovnih `SELECT` poizvedb do `JOIN`, agregacij in CRUD operacij.

---

# 📚 Kazalo

* [O projektu](#-o-projektu)
* [Osnovne poizvedbe](#-1-osnovne-poizvedbe-select--where)
* [Filtriranje in razvrščanje](#-2-filtriranje-in-razvrščanje)
* [JOIN operacije](#-3-osnovni-joini)
* [Agregacije](#-4-osnovne-agregacije)
* [Realni SQL scenariji](#-5-realni-scenariji)
* [CRUD operacije](#-6-crud-operacije)
* [Transakcije](#-7-transakcije)
* [Didaktični nasveti](#-didaktični-nasveti)

---

# 📖 O projektu

Ta repozitorij vsebuje praktične SQL primere za začetnike.

Primeri vključujejo:

* osnovne `SELECT` poizvedbe,
* filtriranje podatkov,
* razvrščanje rezultatov,
* `JOIN` operacije,
* agregacijske funkcije,
* `INSERT`, `UPDATE`, `DELETE`,
* realne poslovne scenarije,
* osnove transakcij.

Projekt je primeren za:

* začetnike v SQL,
* backend razvijalce,
* pripravo na zaposlitve,
* študente računalništva,
* učenje relacijskih baz podatkov.

---

# 🟢 1. Osnovne poizvedbe (SELECT & WHERE)

## 1️⃣ Seznam strank

Izpiši ime stranke, mesto in državo vseh strank.

```sql
SELECT customerName, country, city
FROM customers
ORDER BY country ASC;
```

---

## 2️⃣ Stranke iz določene države

Izpiši vse stranke iz Francije.

```sql
SELECT customerName, city, phone
FROM customers
WHERE country = 'France';
```

---

## 3️⃣ Zaposleni

Izpiši ime in priimek zaposlenih.

```sql
SELECT contactFirstName, contactLastName
FROM customers
WHERE salesRepEmployeeNumber = 1504;
```

---

## 4️⃣ Izdelki

Izpiši vse izdelke.

```sql
SELECT productName, buyPrice, quantityInStock
FROM products;
```

---

## 5️⃣ Izdelki z nizko zalogo

Izdelki z manj kot 100 kosov na zalogi.

```sql
SELECT productName, quantityInStock
FROM products
WHERE quantityInStock < 100;
```

---

# 🟡 2. Filtriranje in razvrščanje

## 6️⃣ Najdražji izdelki

Top 5 najdražjih izdelkov.

```sql
SELECT productName, buyPrice
FROM products
ORDER BY buyPrice DESC
LIMIT 5;
```

---

## 7️⃣ Naročila

Izpiši vsa naročila.

```sql
SELECT orderNumber, orderDate, status
FROM orders;
```

---

## 8️⃣ Odprta naročila

Naročila, ki niso zaključena.

```sql
SELECT orderNumber, orderDate, status
FROM orders
WHERE status != 'Shipped';
```

---

## 9️⃣ Plačila

Plačila večja od 10.000.

```sql
SELECT *
FROM payments
WHERE amount > 10000
ORDER BY amount DESC;
```

---

# 🟠 3. Osnovni JOINI

## 🔟 Naročila in stranke

```sql
SELECT o.orderNumber,
       o.orderDate,
       c.customerName
FROM orders o
JOIN customers c
ON o.customerNumber = c.customerNumber;
```

---

## 1️⃣1️⃣ Naročila določene stranke

```sql
SELECT o.*
FROM orders o
JOIN customers c
ON o.customerNumber = c.customerNumber
WHERE c.customerName = 'Atelier graphique';
```

---

## 1️⃣2️⃣ Podrobnosti naročila

```sql
SELECT p.productName,
       od.quantityOrdered,
       od.priceEach
FROM orderdetails od
JOIN products p
ON od.productCode = p.productCode
WHERE od.orderNumber = 10100;
```

---

# 🟣 4. Osnovne agregacije

## 1️⃣3️⃣ Število strank po državah

```sql
SELECT country,
       COUNT(customerNumber)
FROM customers
GROUP BY country;
```

---

## 1️⃣4️⃣ Skupno število naročil

```sql
SELECT COUNT(orderNumber)
FROM orders;
```

---

## 1️⃣5️⃣ Skupna vrednost naročila

```sql
SELECT SUM(quantityOrdered * priceEach)
FROM orderdetails
WHERE orderNumber = 10100;
```

---

## 1️⃣6️⃣ Najbolje prodajani izdelki

```sql
SELECT p.productName,
       SUM(od.quantityOrdered) AS skupaj_prodano
FROM products p
JOIN orderdetails od
ON p.productCode = od.productCode
GROUP BY p.productName
ORDER BY skupaj_prodano DESC;
```

---

# 🔵 5. Realni scenariji

## 1️⃣7️⃣ Najboljša stranka

```sql
SELECT c.customerName,
       COUNT(o.orderNumber) AS stevilo_narocil
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
GROUP BY c.customerName
ORDER BY stevilo_narocil DESC
LIMIT 1;
```

---

## 1️⃣8️⃣ Promet po strankah

```sql
SELECT c.customerName,
       SUM(od.priceEach * od.quantityOrdered) AS skupni_promet
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY skupni_promet DESC;
```

---

## 1️⃣9️⃣ Zaposleni in stranke

```sql
SELECT c.customerName AS customer_name,
       e.firstName AS employee_name
FROM customers c
JOIN employees e
ON c.salesRepEmployeeNumber = e.employeeNumber;
```

---

## 2️⃣0️⃣ Izdelki brez prodaje

```sql
SELECT p.productCode,
       p.productName
FROM products p
WHERE NOT EXISTS (
    SELECT 1
    FROM orderdetails od
    WHERE od.productCode = p.productCode
);
```

---

# 🟢 6. CRUD Operacije

# ➕ INSERT

## Dodaj novo stranko

```sql
INSERT INTO customers (
    customerNumber,
    customerName,
    contactFirstName,
    contactLastName,
    phone,
    addressLine1,
    city,
    state,
    postalCode,
    country,
    salesRepEmployeeNumber
)
VALUES (
    999,
    'Test Customer',
    'Test',
    'User',
    '+386 41 123 321',
    'Titova ulica 71',
    'Ljubljana',
    'Ljubljana',
    '1000',
    'Slovenia',
    1370
);
```

---

## Dodaj nov izdelek

```sql
INSERT INTO products (
    productCode,
    productName,
    productLine,
    productScale,
    productVendor,
    productDescription,
    quantityInStock,
    buyPrice,
    MSRP
)
VALUES (
    213,
    'SQL Mug',
    'Classic Cars',
    '1:10',
    'OpenAI',
    'Learning SQL Mug',
    50,
    9.99,
    19.99
);
```

---

# ✏️ UPDATE

## Posodobi podatke stranke

```sql
UPDATE customers
SET customerName = 'Test Customer d.o.o.',
    creditLimit = 199.50
WHERE customerNumber = 999;
```

---

## Podražitev izdelkov

```sql
UPDATE products
SET buyPrice = buyPrice * 1.1
WHERE productLine = 'Classic Cars';
```

---

# ❌ DELETE

## Brisanje testne stranke

```sql
DELETE FROM customers
WHERE customerNumber = 999;
```

---

## Brisanje neaktivnih izdelkov

```sql
DELETE FROM products p
WHERE p.quantityInStock = 0
AND NOT EXISTS (
    SELECT 1
    FROM orderdetails od
    WHERE od.productCode = p.productCode
);
```

---

# 🔒 7. Transakcije

```sql
START TRANSACTION;

-- INSERT / UPDATE

ROLLBACK;
```

---

## COMMIT vs ROLLBACK

| Ukaz     | Pomen                   |
| -------- | ----------------------- |
| COMMIT   | trajno shrani spremembe |
| ROLLBACK | razveljavi spremembe    |

---

# 🧠 Didaktični nasveti

✅ Vsaka naloga ima realen poslovni primer
✅ Razumevanje posledic `DELETE` operacij
✅ Učenje FK odvisnosti
✅ Spodbujanje uporabe `SELECT` pred `UPDATE` in `DELETE`
✅ Primeri primerni za začetnike

---

# 🛠️ Tehnologije

* SQL
* MySQL
* Relacijske baze podatkov

---

# 📂 Struktura projekta

```bash
sql-zacetne-poizvedbe/
│
├── README.md
├── examples/
├── joins/
├── aggregates/
├── crud/
└── transactions/
```

---

# 🚀 Kako uporabljati

1. Importiraj testno bazo.
2. Odpri MySQL Workbench ali phpMyAdmin.
3. Kopiraj SQL poizvedbo.
4. Zaženi poizvedbo.
5. Analiziraj rezultate.

---

# 📘 Namen projekta

Projekt je namenjen učenju SQL skozi praktične primere in realne scenarije.

Primeri pokrivajo:

* SELECT
* WHERE
* ORDER BY
* GROUP BY
* JOIN
* INSERT
* UPDATE
* DELETE
* TRANSAKCIJE

---