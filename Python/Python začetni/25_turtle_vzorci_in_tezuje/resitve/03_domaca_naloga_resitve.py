"""Resitve domace naloge - 25 Turtle vzorci in tezuje."""

import turtle


def spirala(koraki, rast):
    dolzina = 10
    for _ in range(koraki):
        turtle.forward(dolzina)
        turtle.left(90)
        dolzina += rast


if __name__ == "__main__":
    turtle.speed(0)
    turtle.color("purple")
    spirala(20, 5)
    turtle.done()

print("Pri vzorcih pomaga, da v zanki postopoma spreminjam dolzino ali kot.")