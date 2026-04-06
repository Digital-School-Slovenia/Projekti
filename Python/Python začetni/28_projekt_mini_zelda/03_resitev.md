# Rešitev / učiteljske usmeritve – 28 – Projekt – Mini Zelda

## Kako vodiš to uro

- projekt ostane cel, ampak ritem mora biti oster,
- najprej igralec in svet, potem predmeti, nato nevarnosti,
- kamera je pomembna ideja, ne samo 'lep trik'.

## Ključni referenčni koncept

```python
def world_to_screen(wx, wy, camera_x, camera_y):
    return int(wx - camera_x), int(wy - camera_y)
```

## Učiteljski checkpointi

1. Igralec obstaja in se premika.
2. V svetu je vsaj en zbirateljski predmet ali sovražnik.
3. Učenec zna razložiti razliko med koordinatami sveta in zaslona.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
- `07_nadgradnja.py`
