"""Rešitve učnega lista – 13 – Nizi in oblikovanje izpisa."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

ime = input("Ime: ").strip()
priimek = input("Priimek: ").strip()
starost = int(input("Starost: "))

polno_ime = ime.title() + " " + priimek.title()
uporabnisko_ime = (ime[:1] + priimek).lower()

print(f"Pozdravljen, {polno_ime}!")
print(f"Čez 5 let boš star {starost + 5} let.")
print(f"Predlagano uporabniško ime: {uporabnisko_ime}")
print(f"Dolžina imena '{polno_ime}' je {len(polno_ime)} znakov.")
