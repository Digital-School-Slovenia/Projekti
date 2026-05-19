"""Rešitve učnega lista – 12 – Seznami v praksi, `for` zanke in mini inventarji."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

kosarica = []

while True:
    izdelek = input("Dodaj izdelek (ali 'konec'): ").strip()
    if izdelek.lower() == "konec":
        break
    kosarica.append(izdelek)

print("\nV košarici imaš:")
for i, izdelek in enumerate(kosarica, start=1):
    print(f"{i}. {izdelek}")
