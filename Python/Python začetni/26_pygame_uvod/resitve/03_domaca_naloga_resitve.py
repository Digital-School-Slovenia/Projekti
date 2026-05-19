"""Rešitve domače naloge – 26 – Pygame – uvod, okno, risanje in premikanje."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.


def ustvari_okno():
    return {"sirina": 600, "visina": 400, "naslov": "Moja prva igra"}


def pobarvaj_ozadje(barva):
    return f"Zaslon pobarvamo z barvo {barva}."


def narisi_pravokotnik(x, y, sirina, visina, barva):
    return {
        "x": x,
        "y": y,
        "sirina": sirina,
        "visina": visina,
        "barva": barva,
    }


print("Naloga 1")
okno = ustvari_okno()
print(f"Okno: {okno['sirina']} x {okno['visina']}, naslov = {okno['naslov']}")

print("\\nNaloga 2")
print(pobarvaj_ozadje((20, 40, 90)))

print("\\nNaloga 3")
pravokotnik = narisi_pravokotnik(120, 150, 80, 50, (220, 90, 90))
print(pravokotnik)

print("\\nNaloga 4")
print("Najtežji del pri pygame je razumeti glavno zanko in stalno osveževanje zaslona.")
