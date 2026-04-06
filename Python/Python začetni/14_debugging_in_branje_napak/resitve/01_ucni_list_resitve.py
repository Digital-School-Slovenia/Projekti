"""Rešitve učnega lista – 14 – Debugging in branje napak."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# 1) TypeError: vnos pretvorimo v stevilo, preden sestevamo.
starost = int(input("Koliko si star? "))
print(starost + 10)

# 2) SyntaxError: zanki manjka dvopicje.
for i in range(5):
    print(i)

# 3) NameError: uporabimo pravilno ime spremenljivke.
stevilo_tock = 10
print(stevilo_tock)

# 4) Logic error: vsoto sproti povecujemo.
vsota = 0
for i in range(1, 6):
    vsota += i
print("Vsota je:", vsota)
