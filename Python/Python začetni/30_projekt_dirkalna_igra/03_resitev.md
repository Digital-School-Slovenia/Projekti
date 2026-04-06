# Rešitev – 30 – Projekt – Dirkalna igra

## Kaj pokaži najprej

Najprej mora biti jasna mehanika:

- cesta,
- avto,
- ovira,
- trk.

Score je bonus, ne jedro.

## Ključni del rešitve

```python
if obstacle_y > HEIGHT:
    obstacle_y = -120
    obstacle_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width)
    score += 1
```

in

```python
if player_rect.colliderect(obstacle_rect):
    game_over = True
```

## Tipične napake

- igralec gre iz ceste,
- ovira se po respawnu pojavi izven ceste,
- `score` se ne poveča,
- `game_over` se izpiše, igra pa še vedno normalno teče.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
- `07_nadgradnja_kovanci_in_gorivo.py`
