# Rešitev / učiteljske usmeritve – 21 – Slovarji v praksi – socialno omrežje

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `01_slovarji.py`

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

### Izsek iz `02_prva-.py`

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

## Tipične napake

- manjkajoč `:` pri pogojih ali funkcijah,
- napačna zamaknitev bloka kode,
- pozabljena pretvorba `input()` v `int()` ali `float()`,
- napačno ime spremenljivke,
- učenec ne zažene programa po vsakem manjšem koraku.

## Minimalni kriterij uspeha

- učenec zaključi obvezno jedro sklopa in ga zna demonstrirati,
- učenec zna povedati, kje v kodi je bilo treba kaj popraviti,
- vsaj enkrat samostojno uporabi testiranje med delom.

## Učiteljski checkpointi

1. 🟢 Naloga 1: Uporabniški profil
2. izpiše uporabniško ime uporabnika
3. izpiše rezultat

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
