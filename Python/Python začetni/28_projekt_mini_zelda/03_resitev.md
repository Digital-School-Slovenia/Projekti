# Rešitev – 28 – Projekt – Mini Zelda

## Kaj pokaži najprej

Ne pokaži takoj celotne pošasti. Pokaži po vrsti:

1. gibanje igralca,
2. kamero,
3. pobiranje kovancev,
4. sovražnika,
5. napad.

## Minimum, ki mora delovati

- igralec se giblje,
- zaslon sledi igralcu,
- score se poveča,
- vsaj en sovražnik se premika,
- `SPACE` sproži napad.

## Ključni deli rešitve

### Kamera

```python
camera_x = player["x"] - WIDTH // 2 + player["size"] // 2
camera_y = player["y"] - HEIGHT // 2 + player["size"] // 2
```

### Pretvorba iz sveta na zaslon

```python
def world_to_screen(wx, wy, camera_x, camera_y):
    return int(wx - camera_x), int(wy - camera_y)
```

### Pobiranje kovancev

```python
for coin in collectibles[:]:
    coin_rect = pygame.Rect(coin["x"], coin["y"], coin["size"], coin["size"])
    if player_rect.colliderect(coin_rect):
        collectibles.remove(coin)
        player["score"] += 1
```

## Tipične napake

- Učenec meša koordinate sveta in zaslona.
- Riše objekte neposredno z `world_x`, `world_y`.
- Pozabi normalizirati diagonalno gibanje.
- `attack_rect` ostane večno viden.
- `player_rect` se ne osvežuje po premiku.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py` – glavna rešitev.
- `07_nadgradnja.py` – dodatne nadgradnje.
