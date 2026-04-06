# Rešitev / učiteljske usmeritve – 32 – Projekt – Mini Wolfenstein

## Kako vodiš to uro

- najprej 2D logika, potem lažni 3D,
- učenci morajo razumeti mapo in stene, ne samo gledati stolpce,
- minimapa je zelo koristna pri razlagi.

## Ključni referenčni koncept

```python
def is_wall(world_x, world_y):
    col = int(world_x // TILE_SIZE)
    row = int(world_y // TILE_SIZE)
    return MAP_DATA[row][col] == 1
```

## Učiteljski checkpointi

1. Igralec se premika po mapi.
2. Stene delujejo kot ovira.
3. Na zaslonu se izriše osnovni 3D pogled.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
- `07_resitev_z_misko.py`
