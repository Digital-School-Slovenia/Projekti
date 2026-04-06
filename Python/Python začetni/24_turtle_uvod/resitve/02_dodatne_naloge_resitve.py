"""Resitve dodatnih nalog - 24 Turtle uvod."""

import turtle


def narisi_kvadrat(stranica, barva):
    turtle.color(barva)
    for _ in range(4):
        turtle.forward(stranica)
        turtle.left(90)


def narisi_trikotnik(stranica, barva):
    turtle.color(barva)
    for _ in range(3):
        turtle.forward(stranica)
        turtle.left(120)


def narisi_hisko():
    narisi_kvadrat(80, "blue")
    turtle.left(45)
    narisi_trikotnik(80, "red")


if __name__ == "__main__":
    turtle.speed(6)
    narisi_hisko()
    turtle.done()