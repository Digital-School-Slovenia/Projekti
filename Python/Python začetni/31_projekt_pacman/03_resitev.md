# Rešitev / učiteljske usmeritve – 31 – Projekt – Pac-Man stil: labirint in zbiranje točk

## Kako vodiš to uro

- glavna ideja je mreža,
- ne pusti, da učenci izgubijo `(row, col)` proti `(x, y)`,
- najprej zidovi in gibanje, šele nato sovražnik.

## Ključni referenčni koncept

```python
x = col * CELL_SIZE
y = row * CELL_SIZE
```

## Učiteljski checkpointi

1. Labirint se izriše pravilno.
2. Igralec se ne more premakniti skozi zid.
3. Pika ali točka izgine, ko jo igralec pobere.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
