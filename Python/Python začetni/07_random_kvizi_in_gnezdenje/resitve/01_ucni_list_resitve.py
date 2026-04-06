"""Rešitve učnega lista – 07 – Random, mini kvizi in odločanje v praksi."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

from random import randint

a = randint(1, 12)
b = randint(1, 12)
rezultat = a * b
vnos = int(input(f"Koliko je {a} * {b}: "))

if vnos == rezultat:
    print("Odgovor je pravilen!")
    tezavnost = input("Želiš težji primer? (da/ne) ").lower()
    if tezavnost == "da":
        c = randint(10, 20)
        d = randint(10, 20)
        print(f"Bonus: koliko je {c} + {d}? ")
    else:
        print("Super, ostaniva pri osnovah.")
else:
    print(f"Žal si se zmotil, pravilno je {rezultat}.")
