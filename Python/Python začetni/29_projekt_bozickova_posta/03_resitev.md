# Rešitev – 29 – Projekt – Božičkova pošta

## Kaj pokaži najprej

Pokaži najprej eno stvar: Božiček lovi padajoče predmete.

Vse ostalo je nadgradnja.

## Minimum, ki mora delovati

- premik levo/desno,
- ustvarjanje predmetov,
- trk,
- točke in življenja.

## Ključni del rešitve

```python
if rect.colliderect(santa_rect):
    if email["type"] == "good":
        stevilo_tock += 1
    else:
        stevilo_zivljenj -= 1
    emails.remove(email)
    continue
```

## Tipične napake

- `emails.remove(email)` manjka,
- vsi emaili so iste vrste,
- Božiček gre iz zaslona,
- življenje pade pod 0 in igra še vedno teče.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
