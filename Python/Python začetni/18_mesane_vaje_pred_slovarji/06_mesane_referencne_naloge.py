# Referenčni primer – 18 Mešane vaje

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
