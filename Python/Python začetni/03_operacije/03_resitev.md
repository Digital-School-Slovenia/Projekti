# Rešitev / učiteljske usmeritve – 03 – Osnovne operacije in računanje s programom

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `02_osnovne_operacije.py`

```python
stevilo_pic = 4
cena_pice = 10.5
print(f"Pice stanejo: {stevilo_pic * cena_pice} €.")


starost_psa = 4
pasja_leta = starost_psa * 7
print(f"Moj pes ima: {pasja_leta} let.")

denar = 100
cena_cokolade = 2.5
print(f"Kupim lahko: {denar // cena_cokolade} čokolad.")
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

1. Izpiše tvoje ime.
2. Izpiše tvojo najljubšo hrano.
3. Ustvari spremenljivko `najljubsi_predmet` in jo izpiši v stavku.

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
