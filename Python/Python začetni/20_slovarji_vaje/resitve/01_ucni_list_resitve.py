"""Rešitve učnega lista – 20 – Slovarji – vaje, zanke in seznam slovarjev."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

film = {
    "naslov": "Matrix",
    "leto": 1999,
    "ocena": 9.0,
}

print(f"Film: {film['naslov']}")
print(f"Leto: {film['leto']}")
print(f"Ocena: {film['ocena']}")

film["zanr"] = "sci-fi"
print("Posodobljen slovar:", film)
