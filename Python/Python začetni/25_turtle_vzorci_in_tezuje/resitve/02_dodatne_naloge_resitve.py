"""Resitve dodatnih nalog - 25 Turtle vzorci in tezuje."""

import turtle


def koncentricni_kvadrati(zacetek, koliko):
    for indeks in range(koliko):
        stranica = zacetek + indeks * 15
        for _ in range(4):
            turtle.forward(stranica)
            turtle.left(90)
        turtle.penup()
        turtle.goto(-stranica / 2, -stranica / 2)
        turtle.pendown()


def zvezda(stranica):
    for _ in range(5):
        turtle.forward(stranica)
        turtle.right(144)


if __name__ == "__main__":
    turtle.speed(0)
    koncentricni_kvadrati(40, 4)
    turtle.penup()
    turtle.goto(120, 0)
    turtle.pendown()
    zvezda(90)
    turtle.done()