# Referenčna rešitev – 25 Turtle vzorci in težje naloge
# Namen: demonstracijska rešitev za razlago ključnih gradnikov sklopa.

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
