# Rešitev / učiteljske usmeritve – 27 – Projekt – Lov na kovance

## Kako vodiš to uro

- jedro mora hitro zaživeti: okno, igralec, premik,
- kovanci pridejo takoj za tem,
- rezultat in restart sta zadnja koraka, ne prva.

## Minimalno jedro

```python
player = pygame.Rect(400, 400, 50, 50)
speed = 5
coins = [pygame.Rect(120, 120, 20, 20), pygame.Rect(300, 200, 20, 20)]
score = 0
```

## Učiteljski checkpointi

1. Rdeč kvadrat se premika.
2. Ob dotiku kovanca ta izgine ali se rezultat spremeni.
3. Učenec zna demonstrirati vsaj eno uspešno rundo pobiranja.

## Tipične napake

- pozabljeno brisanje zaslona (`fill`),
- objekt se nariše, a se ne posodablja,
- trk se preverja nad napačnim objektom,
- rezultat se resetira v napačnem delu zanke.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
