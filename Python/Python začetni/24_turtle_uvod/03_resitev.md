# Rešitev – 24 – Turtle – uvod v risanje s funkcijami

Tukaj je jedro rešitve za sklop **24 – Turtle – uvod v risanje s funkcijami**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
import turtle

zaslon = turtle.Screen()
zaslon.title("Turtle – uvod")
t = turtle.Turtle()
t.speed(6)

def kvadrat(stranica):
    for _ in range(4):
        t.forward(stranica)
        t.right(90)

def trikotnik(stranica):
    for _ in range(3):
        t.forward(stranica)
        t.left(120)

kvadrat(80)
t.penup()
t.goto(140, 0)
t.pendown()
trikotnik(100)

turtle.done()
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- `t` je **želva**, ki riše
- Vse ukaze pišemo kot `t.ukaz()`
- `t.left()` / `t.right()`

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
