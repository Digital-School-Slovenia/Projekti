# Referenčni primer – 20 Slovarji vaje

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
