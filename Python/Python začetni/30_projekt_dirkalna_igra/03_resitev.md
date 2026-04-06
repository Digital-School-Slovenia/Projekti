# Rešitev / učiteljske usmeritve – 30 – Projekt – Dirkalna igra

## Kako vodiš to uro

- učenci morajo najprej normalno voziti po cesti,
- ena ovira je dovolj za jedro,
- vse ostalo so nadgradnje.

## Minimalni referenčni okvir

```python
if keys[pygame.K_LEFT]:
    player_x -= player_speed
if keys[pygame.K_RIGHT]:
    player_x += player_speed

obstacle_y += obstacle_speed
```

## Učiteljski checkpointi

1. Avto se premika levo/desno.
2. Ovira pada.
3. Trk se zazna in igra reagira.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
- `07_nadgradnja_kovanci_in_gorivo.py`
