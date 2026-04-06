# Rešitev – 27 – Projekt – Lov na kovance

## Kaj pokaži najprej

Najprej pokaži minimum:

1. okno,
2. igralec,
3. premikanje,
4. kovanci,
5. score.

Zmaga in restart sta zadnja koraka.

## Če zmanjkuje časa

Do konca ure naj obvezno deluje:

- premik igralca,
- vsaj 4 kovanci,
- pobiranje kovancev,
- izpis rezultata.

Če to deluje, je jedro narejeno.

## Ključni del rešitve

```python
for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score += 1
```

To je srce projekta. Če ta del ne dela, igra ni več "lov na kovance", ampak samo sprehajanje kvadrata.

## Tipične napake

- `fill` manjka, zato ostajajo sledi.
- Učenec riše kovance, ne preveri pa trka.
- `coins.remove(...)` dela na napačnem seznamu.
- `score = 0` je po nesreči v glavni zanki in se stalno resetira.
- `game_won` se nikoli ne nastavi na `True`.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py` – celotna delujoča rešitev.

## Kaj preveri med uro

- se igralec premika,
- ostaja v oknu,
- vsaj en kovanec izgine ob dotiku,
- rezultat raste,
- učenec zna pokazati, kje se preverja trk.
