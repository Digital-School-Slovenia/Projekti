# Rešitev / učiteljske usmeritve – 09 – Zanka `while` – delavnica problemov in seštevalnikov

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `01_zanke.py`

```python
# 
# # 1. način (brez spremenljivke)
# while input("Ali je pes dobil hrano?: ").lower() != 'da':
#     print("🐶 WOOF! Daj mi jesti!")
# print("🐶 Končno! *munch munch* 😋")
# 
# 
# 
# # 2. način (s spremenljivko)
# while True:
#     odgovor = input("Ali je pes dobil hrano?: ").lower()
#     if odgovor == 'da':
#         print("🐶 Končno! *munch munch* 😋")
#         break
#     else:
#         print("🐶 WOOF! Daj mi jesti!")
#         
#         
#


racun = 0 # Predstavlja skupno vrednost racuna
st_izdelkov = 0 # Predstavlja st. vnesenih izdelkov

while st_izdelkov < 5:
    # Vnesemo ceno trenutnega izdelka
    cena_izdelka = input("Cena izdelka: ")
    # Vnos uporabnika spremenimo v stevilko
    cena_izdelka = float(cena_izdelka)
    # Pristejemo ceno izdelka na racun
    racun = racun + cena_izdelka
    # Povecamo stevilo vnesenih izdelkov za + 1
    st_izdelkov = st_izdelkov + 1

print(f"Racun je bil: {racun}")
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

1. november 2025.
2. 🧮 Naloga 1: Štetje do 10
3. Program naj **ponavlja vprašanje**:

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
