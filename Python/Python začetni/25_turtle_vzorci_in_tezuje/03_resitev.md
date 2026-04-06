# Rešitev – 25 – Turtle – zahtevnejši vzorci in problemsko risanje

Tukaj je jedro rešitve za sklop **25 – Turtle – zahtevnejši vzorci in problemsko risanje**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
import turtle

zaslon = turtle.Screen()
zaslon.title("Turtle – vzorci")
t = turtle.Turtle()
t.speed(0)

for i in range(60):
    t.forward(5 + i * 3)
    t.left(91)

t.penup()
t.goto(-180, -120)
t.pendown()

for _ in range(36):
    t.circle(80)
    t.left(10)

turtle.done()
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Nariši hiško iz kvadrata in strehe.
- Nariši tri vedno večje kvadrate.
- Nariši spiralo.

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
