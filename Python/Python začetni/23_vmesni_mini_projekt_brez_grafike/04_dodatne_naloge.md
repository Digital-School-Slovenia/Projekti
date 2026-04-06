# Dodatne naloge – 23 – Vmesni mini projekt brez grafike

### Naloga 1
Dodaj izpis števila vseh predmetov v inventarju.

**Namig:** Uporabi `len(inventar)`.

### Naloga 2
Poskrbi, da se isti predmet ne more dodati dvakrat.

**Namig:** Pred `append()` preveri `if predmet in inventar:`.

### Naloga 3
Namesto iskanja po imenu omogoči brisanje po številki.

**Namig:** Uporabnik lahko vnese številko, ti pa jo pretvoriš z `int()`.

### Naloga 4
Razbij program na več funkcij: `dodaj_predmet()`, `izpisi_inventar()`, `odstrani_predmet()`.

### Naloga 5
Predmete shrani kot slovarje, npr. ime + tip predmeta.

**Namig:** Primer slovarja: `{"ime": "mec", "tip": "orozje"}`.

### Naloga 6
Dodaj iskanje predmeta.

Primer:
- uporabnik vnese del imena,
- program izpiše vse zadetke.

### Naloga 7
Dodaj začetne podatke, da inventar ni vedno prazen.

Primer:
```python
inventar = ["mec", "kljuc", "jabolko"]
```

### Naloga 8
Dodaj možnost `4 - pocisti inventar`, ki izbriše vse predmete.

**Namig:** Uporabi `inventar.clear()`.

### Naloga 9
Dodaj lepši izpis, na primer:

```python
print(f"V inventarju je {len(inventar)} predmetov.")
```
