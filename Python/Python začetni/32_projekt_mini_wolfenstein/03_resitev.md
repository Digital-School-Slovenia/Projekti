# Rešitev – 32 – Projekt – Mini Wolfenstein

## Kaj pokaži najprej

Ne začni s teorijo raycastinga za 20 minut. Najprej pokaži:

- 2D mapo,
- igralca,
- premik,
- potem žarke,
- potem 3D stolpce.

## Minimum, ki mora delovati

- igralec se ne zaletava skozi zid,
- minimapa je pravilna,
- vsaj osnovni 3D pogled deluje.

## Ključni del rešitve

```python
target_x = player_x + math.cos(ray_angle) * depth
target_y = player_y + math.sin(ray_angle) * depth

if is_wall(target_x, target_y):
    corrected_depth = depth * math.cos(player_angle - ray_angle)
```

To je srce projekta.

## Tipične napake

- brez `corrected_depth` je slika čudno ukrivljena,
- igralec gre skozi zid,
- žarki nikoli ne zadenejo stene,
- minimapa in 3D pogled si ne ustrezata.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
- `07_resitev_z_misko.py`
