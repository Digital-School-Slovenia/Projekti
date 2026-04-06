# Rešitev – 33 – Projekt – Dodge the Meteors

## Kaj pokaži najprej

Jedro je zelo jasno:

- ladja,
- meteorji,
- trk.

Score je lep, ampak ni glavni problem.

## Ključni del rešitve

```python
if event.type == SPAWN_EVENT:
    mw = random.randint(25, 60)
    mh = random.randint(25, 60)
    mx = random.randint(0, WIDTH - mw)
    my = -mh
    meteors.append(pygame.Rect(mx, my, mw, mh))
```

in

```python
for m in meteors:
    if player.colliderect(m):
        running = False
```

## Tipične napake

- meteorji se ne odstranjujejo,
- `SPAWN_EVENT` ni nastavljen,
- ladja gre iz zaslona,
- `score` raste prehitro ali nikoli.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
