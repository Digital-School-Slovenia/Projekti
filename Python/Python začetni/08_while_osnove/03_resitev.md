# Rešitev – 08 – Zanka `while` – osnove ponavljanja

Tukaj je jedro rešitve za sklop **08 – Zanka `while` – osnove ponavljanja**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

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

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- November 2025.
- 🧮 Naloga 1: Štetje do 10
- Program naj **ponavlja vprašanje**:

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
