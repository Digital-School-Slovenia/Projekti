# Rešitev – 21 – Slovarji v praksi – socialno omrežje

Tukaj je jedro rešitve za sklop **21 – Slovarji v praksi – socialno omrežje**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

### Primer 1

```python
# -- SEZNAM --
oseba_seznam = [
    "Matej",
    "Mencin",
    "matejma",
    "skrivnost",
    "matejmatik@email.si"
]

# -- SLOVAR --
oseba_slovar = {
    "ime": "Matej",
    "priimek": "Mencin",
    "uime": "matejma",
    "ugeslo": "skrivnost",
    "email": "matejmatik@email.si"
}
```

### Primer 2

```python
seznam_uporabnikov = [
    {"uime": "ana", "ugeslo": "ana123", "sledilci": 120, "spol": "Ž"}, # 0
    {"uime": "miha", "ugeslo": "miha123", "sledilci": 80}, # 1
    {"uime": "luka", "ugeslo": "luka123", "sledilci": 300, "spol": "M"}, # 2
    {"uime": "eva", "ugeslo": "eva123", "sledilci": 45}, # 3
]

# Naloga 1 <<<< Funkcija izpiše ime in st. sledilcev.
def izpisi_profil(uporabnik): 
    print(f"Uporabniško ime je: {uporabnik['uime']}")
    print(f"Št. sledilcev: {uporabnik['sledilci']}")
    
# Naloga 2 <<<< Funkcija preveri, ce se geslo ujema z vpisanim geslom.
def preveri_geslo(uporabnik, vpisani_geslo): 
    if uporabnik["ugeslo"] == vpisani_geslo:
        print("Prijava uspešna ✅")
    else:
        print("Napačno geslo ❌")

# Naloga 4  <<<< Funkcija izpise vse uporabnike iz seznama.
def izpisi_uporabnike(seznam_uporabnikov): 
    for uporabnik in seznam_uporabnikov:
        izpisi_profil(uporabnik) # <--- Lahko uporabimo kar funkcijo "izpisi_profil", ki nam ravno izpise ime in st. sledilcev
        print("------") # Malo vizuala, da se lažje loči uporabnike
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- 🟢 Naloga 1: Uporabniški profil
- Izpiše uporabniško ime uporabnika
- Izpiše rezultat

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
