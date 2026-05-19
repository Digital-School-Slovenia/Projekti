"""Rešitve domače naloge – 24 – Turtle – uvod v risanje s funkcijami."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

import turtle


def inicialka_m(velikost):
    for smer in [90, -135, 135, -135, 90]:
        turtle.forward(velikost)
        turtle.right(smer)


if __name__ == "__main__":
    turtle.speed(5)
    turtle.color("green")
    inicialka_m(40)
    turtle.done()

print("Turtle uporablja ukaze forward, left in right, zato lahko z njimi sestavim skoraj vsako preprosto obliko.")
