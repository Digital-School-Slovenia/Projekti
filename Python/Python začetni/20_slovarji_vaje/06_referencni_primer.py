# Referenčni primer – 20 Slovarji vaje

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
