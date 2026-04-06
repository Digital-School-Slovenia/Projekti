# Rešitev – 23 – Vmesni mini projekt brez grafike

Danes je cilj jasen: do konca ure mora delovati **Inventar avanturista**.

## Kaj pokaži najprej

Pokaži samo to:
- seznam `inventar = []`,
- funkcijo za meni,
- glavno zanko,
- eno delujočo možnost.

Ne kažeš petih nadgradenj na začetku. Najprej jedro.

## Jedro rešitve

```python
def izpisi_meni():
    print("\n--- INVENTAR AVANTURISTA ---")
    print("1 - dodaj predmet")
    print("2 - pokaži inventar")
    print("3 - odstrani predmet")
    print("0 - konec")

inventar = []

while True:
    izpisi_meni()
    izbira = input("Izbira: ").strip()

    if izbira == "1":
        predmet = input("Vnesi predmet: ").strip()
        if predmet != "":
            inventar.append(predmet)
            print("Predmet je dodan.")
        else:
            print("Prazen vnos ni dovoljen.")

    elif izbira == "2":
        print("\n--- INVENTAR ---")
        if len(inventar) == 0:
            print("Inventar je prazen.")
        else:
            for i, predmet in enumerate(inventar, start=1):
                print(f"{i}. {predmet}")

    elif izbira == "3":
        predmet = input("Kateri predmet zelis odstraniti? ").strip()
        if predmet in inventar:
            inventar.remove(predmet)
            print("Predmet je odstranjen.")
        else:
            print("Tega predmeta ni v inventarju.")

    elif izbira == "0":
        print("Konec programa.")
        break

    else:
        print("Neveljavna izbira.")
```

## Kaj mora do konca ure delovati

- Program se zažene brez napake.
- Meni se izpiše večkrat.
- Uporabnik lahko doda predmet.
- Uporabnik lahko vidi inventar.
- Uporabnik lahko odstrani predmet.
- Program se zna zaključiti.

## Kaj pokaži hitrejšim

- funkcije `dodaj_predmet()`, `izpisi_inventar()`, `odstrani_predmet()`,
- zaščito pred podvojenimi vnosi,
- seznam slovarjev, npr. `{"ime": "mec", "tip": "orozje"}`.

## Tipične napake

- `elif` je napačno zamaknjen,
- učenec piše `inventar.remove()` brez argumenta,
- uporablja `==` namesto `=` pri dodelitvi,
- pozabi `.strip()`,
- testira samo srečen primer in ne preveri praznega inventarja.

## Hitri pregled med uro

Preveri samo to:
- Ali ima učenec datoteko, ki se zažene?
- Ali ena možnost že deluje?
- Ali zna učenec pokazati cel tok: dodaj → pokaži → odstrani?

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
