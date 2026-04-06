# Rešitev – 31 – Projekt – Pac-Man labirint

## Kaj pokaži najprej

Pokaži razliko med:

- mrežo `(row, col)`,
- zaslonom `(x, y)`.

To je glavni koncept te ure.

## Minimum, ki mora delovati

- zidovi,
- igralec,
- premik po poljih,
- pobiranje pik,
- score.

Sovražnik je bonus, če zmanjkuje časa.

## Ključni del rešitve

```python
if maze[new_row][new_col] != "#":
    player_row = new_row
    player_col = new_col
```

in

```python
x = col * CELL_SIZE
y = row * CELL_SIZE
```

## Tipične napake

- zamenjava `row/col` in `x/y`,
- igralec gre skozi zid,
- pika ostane vidna tudi po pobiranju,
- sovražnik se premakne v zid.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
