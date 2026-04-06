# Rešitev – 18 – Velika delavnica vaj – mešane naloge pred slovarji

Tukaj je jedro rešitve za sklop **18 – Velika delavnica vaj – mešane naloge pred slovarji**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
def pozdrav_uporabnik(uporabnisko_ime):
    """
    Funkcija sprejme ime in izpise ime.
    Ce je ime krajse od 4 znakov izpise opozorilo
    """
    
    # Izpisemo ime
    print(f"Pozdravljen, {uporabnisko_ime}")
    
    # Preverimo ali je ime krajse od 4 znakov.
    if len(uporabnisko_ime) < 4:
        print("Uporabniško ime je krajše od 4 znakov")

def status_uporabnika(st_sledilcev):
    
    if st_sledilcev > 1000:
        print("Influencer 😎")
    elif 100 <= st_sledilcev <= 1000:
        print("Aktiven uporabnik 👍")
    else:
        print("Začetnik 👶")
        
        
        
objave = ["selfie", "kosilo", "maček", "sončni zahod"]     
def izpisi_objave(objave):
    
    for ob in objave:
        print(f"Objava: {ob}")
    
    st_objav = len(objave)
    print(f"St. objav: {st_objav}")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- `int` → cela števila (`5`, `10`)
- `float` → decimalna števila (`3.14`)
- Koda je bolj pregledna

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_mesane_referencne_naloge.py`
