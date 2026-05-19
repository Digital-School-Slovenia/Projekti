"""Rešitve učnega lista – 18 – Velika delavnica vaj – mešane naloge pred slovarji."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

# 1) Mini kalkulator
st1 = float(input("Prvo število: "))
st2 = float(input("Drugo število: "))
operacija = input("Operacija (+, -, *, /): ")

if operacija == "+":
    print(st1 + st2)
elif operacija == "-":
    print(st1 - st2)
elif operacija == "*":
    print(st1 * st2)
elif operacija == "/":
    if st2 != 0:
        print(st1 / st2)
    else:
        print("Z 0 ne gre.")
else:
    print("Neznana operacija.")
