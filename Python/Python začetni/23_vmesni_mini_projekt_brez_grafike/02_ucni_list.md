# Učni list – 23 – Vmesni mini projekt brez grafike

Danes izdelaš mini projekt **Inventar avanturista**.

Program naj omogoča:
- dodajanje predmeta,
- izpis vseh predmetov,
- brisanje predmeta,
- izhod iz programa.

## Korak 1: Ustvari začetno datoteko in seznam inventarja
Ustvari datoteko `inventar.py`.

Na začetek napiši:

```python
inventar = []
```

### Kaj dela ta del?
- `inventar` je seznam, v katerega boš shranjeval predmete.
- Na začetku je seznam prazen.

## Korak 2: Dodaj funkcijo za izpis menija
Pod seznam dodaj:

```python
def izpisi_meni():
    print("\n--- INVENTAR AVANTURISTA ---")
    print("1 - dodaj predmet")
    print("2 - pokaži inventar")
    print("3 - odstrani predmet")
    print("0 - konec")
```

### Kaj dela ta del?
- Funkcija izpiše meni.
- Kasneje jo boš klical v glavni zanki.
- Tako ni treba istih `print()` vrstic pisati večkrat.

## Korak 3: Dodaj glavno zanko programa
Pod funkcijo dodaj:

```python
while True:
    izpisi_meni()
    izbira = input("Izbira: ").strip()

    if izbira == "0":
        print("Konec programa.")
        break
```

### Kaj dela ta del?
- Program teče v neskončni zanki.
- Vsakič izpiše meni in prebere izbiro uporabnika.
- Če uporabnik vnese `0`, se program konča.

## Korak 4: Dodaj možnost za dodajanje predmeta
V zanko dodaj:

```python
    elif izbira == "1":
        predmet = input("Vnesi predmet: ").strip()
        if predmet != "":
            inventar.append(predmet)
            print("Predmet je dodan.")
        else:
            print("Prazen vnos ni dovoljen.")
```

### Kaj dela ta del?
- Uporabnik vnese ime predmeta.
- Če vnos ni prazen, ga program doda v seznam.
- Če je vnos prazen, program opozori uporabnika.

## Korak 5: Dodaj izpis inventarja
Pod prejšnji del dodaj:

```python
    elif izbira == "2":
        print("\n--- INVENTAR ---")
        if len(inventar) == 0:
            print("Inventar je prazen.")
        else:
            for i, predmet in enumerate(inventar, start=1):
                print(f"{i}. {predmet}")
```

### Kaj dela ta del?
- Če je inventar prazen, program to pove.
- Če inventar ni prazen, izpiše vse predmete po vrsti.
- `enumerate(..., start=1)` doda številke 1, 2, 3 ...

## Korak 6: Dodaj odstranjevanje predmeta
Pod izpis dodaj:

```python
    elif izbira == "3":
        predmet = input("Kateri predmet zelis odstraniti? ").strip()
        if predmet in inventar:
            inventar.remove(predmet)
            print("Predmet je odstranjen.")
        else:
            print("Tega predmeta ni v inventarju.")
```

### Kaj dela ta del?
- Uporabnik vnese ime predmeta.
- Če je predmet v seznamu, ga program izbriše.
- Če predmeta ni, program izpiše opozorilo.

## Korak 7: Dodaj še neveljavno izbiro
Na konec verige `if` dodaj:

```python
    else:
        print("Neveljavna izbira.")
```

### Kaj dela ta del?
- Če uporabnik vnese nekaj napačnega, program ne pade.
- Namesto napake dobi opozorilo in meni se pokaže znova.

## Korak 8: Preizkusi celoten program
Preveri vsaj ta primer:

1. dodaj `meč`
2. dodaj `ključ`
3. pokaži inventar
4. odstrani `ključ`
5. znova pokaži inventar
6. zaključi program

### Kaj mora zdaj delovati?
- meni,
- dodajanje,
- izpis,
- brisanje,
- izhod.

## Korak 9: Dodaj eno nadgradnjo
Izberi eno:

- izpiši število vseh predmetov,
- ne dovoli podvojenih predmetov,
- dodaj funkcijo `dodaj_predmet()`,
- dodaj funkcijo `izpisi_inventar()`,
- razdeli predmete na vrste.
