# CRUD Projekt – PHP + MySQL

Ta projekt predstavlja praktično CRUD aplikacijo, izdelano s pomočjo:
- PHP
- MySQL
- HTML
- CSS

Projekt se iz ure v uro nadgrajuje in raste.  
Vsaka nova vaja doda novo funkcionalnost, zato učenci postopoma sestavljajo celotno aplikacijo.

---

# Kaj je CRUD?

CRUD pomeni štiri osnovne operacije nad podatki:

| Črka | Pomen | Opis |
|---|---|---|
| C | Create | dodajanje novih podatkov |
| R | Read | prikaz podatkov |
| U | Update | urejanje podatkov |
| D | Delete | brisanje podatkov |

CRUD aplikacije so osnova skoraj vseh modernih spletnih aplikacij:
- socialna omrežja,
- spletne trgovine,
- administracijski sistemi,
- blogi,
- prijavni sistemi,
- dashboard sistemi.

---

# Namen projekta

Glavni namen projekta je:
- povezati znanje PHP-ja in SQL-a,
- razumeti delo z bazami podatkov,
- pokazati praktično uporabo programiranja,
- razvijati logično razmišljanje,
- razumeti komunikacijo med aplikacijo in podatkovno bazo.

Projekt učencem pokaže:
- zakaj uporabljamo PHP,
- kako PHP komunicira z MySQL bazo,
- kako shranjujemo podatke,
- kako prikazujemo podatke uporabniku,
- kako urejamo in brišemo podatke.

---

# Kaj se učenci naučijo?

S projektom učenci vadijo:
- delo s formami,
- POST in GET metode,
- delo z bazami podatkov,
- SQL poizvedbe,
- povezovanje PHP-ja in MySQL-a,
- organizacijo projektov,
- delo z datotekami,
- funkcije,
- validacijo podatkov,
- osnovno strukturo pravih spletnih aplikacij.

---

# Struktura projekta

## config/
Mapa vsebuje konfiguracijo projekta.

### config.php
Datoteka vsebuje:
- povezavo z MySQL bazo,
- nastavitve za dostop do baze,
- osnovno konfiguracijo aplikacije.

---

## functions/
Mapa vsebuje funkcije projekta.

### functionModule.php
Datoteka vsebuje:
- pomožne funkcije,
- funkcije za delo z bazo,
- ponovno uporabljeno logiko projekta.

Namen:
- manj podvajanja kode,
- bolj pregledna struktura,
- lažje vzdrževanje projekta.

---

## style/
Mapa vsebuje CSS datoteke.

### style.css
Datoteka skrbi za:
- izgled aplikacije,
- oblikovanje tabel,
- obrazcev,
- gumbov,
- postavitve strani.

---

# Glavne datoteke projekta

## index.php
Glavna stran aplikacije.

Naloge:
- prikaz podatkov iz baze,
- pregled vseh zapisov,
- povezave za urejanje in brisanje.

---

## add.php
Stran za dodajanje novih podatkov.

Uporablja:
- HTML formo,
- POST metodo,
- SQL INSERT.

---

## edit.php
Stran za urejanje obstoječih podatkov.

Uporablja:
- GET parameter za ID,
- prikaz obstoječih podatkov,
- obrazec za urejanje.

---

## update.php
Datoteka posodobi podatke v bazi.

Uporablja:
- POST metodo,
- SQL UPDATE.

---

## delete.php
Datoteka izbriše zapis iz baze.

Uporablja:
- GET parameter,
- SQL DELETE.

---

## profile.php
Prikaz posameznega zapisa oziroma podrobnosti uporabnika.

---

# Prednosti takega projekta

Projekt učencem pokaže:
- kako izgleda prava aplikacija,
- kako sodelujeta frontend in backend,
- kako pomembna je organizacija kode,
- kako delujejo baze podatkov v praksi.

Prav tako učenci spoznajo:
- modularno programiranje,
- ločevanje logike in izgleda,
- pomen funkcij,
- pomen strukturiranja projektov.

---

# Cilj projekta

Končni cilj projekta je:
- izdelati delujočo CRUD aplikacijo,
- razumeti osnove backend razvoja,
- pripraviti učence na bolj kompleksne projekte,
- pokazati realno uporabo PHP-ja in SQL-a.

Projekt predstavlja prvi korak proti:
- naprednim PHP aplikacijam,
- MVC strukturi,
- objektno usmerjenemu programiranju,
- modernim spletnim aplikacijam.