"""Rešitve učnega lista – 09 – Zanka `while` – delavnica problemov in seštevalnikov."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

racun = 0.0
st_izdelkov = 0

while st_izdelkov < 5:
    cena_izdelka = float(input("Cena izdelka: "))
    racun = racun + cena_izdelka
    st_izdelkov = st_izdelkov + 1

print(f"Račun je bil: {racun:.2f} €")
