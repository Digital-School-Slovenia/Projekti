# Učiteljska referenčna rešitev – 24 Turtle uvod
# Namen: učiteljska orientacija pri razlagi ključnih gradnikov sklopa.

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
