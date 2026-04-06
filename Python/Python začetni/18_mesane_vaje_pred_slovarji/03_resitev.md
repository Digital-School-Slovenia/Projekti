# Rešitev / učiteljske usmeritve – 18 – Velika delavnica vaj – mešane naloge pred slovarji

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `01_naloga.py`

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

1. `int` → cela števila (`5`, `10`)
2. `float` → decimalna števila (`3.14`)
3. koda je bolj pregledna

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_mesane_referencne_naloge.py`
