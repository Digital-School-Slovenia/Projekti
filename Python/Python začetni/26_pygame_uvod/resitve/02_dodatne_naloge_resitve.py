"""Rešitve dodatnih nalog – 26 – Pygame – uvod, okno, risanje in premikanje."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

okno = {"sirina": 800, "visina": 500, "naslov": "Pygame – dodatne naloge"}
ozadje = (30, 30, 60)
igralec = {"x": 100, "y": 120, "sirina": 50, "visina": 50, "hitrost": 5}
tarca = {"x": 320, "y": 210, "polmer": 18}
tocke = 0


def ustvari_okno(nastavitve):
    return f"Okno {nastavitve['sirina']} x {nastavitve['visina']} z naslovom '{nastavitve['naslov']}'"


def obdela_dogodek(vrsta_dogodka):
    return vrsta_dogodka != "QUIT"


def barva_ozadja(barva):
    return f"Ozadje pobarvamo z barvo {barva}."


def narisi_pravokotnik(stanje):
    return f"Pravokotnik narišemo na ({stanje['x']}, {stanje['y']}) velikosti {stanje['sirina']} x {stanje['visina']}."


def narisi_krog(predmet):
    return f"Krog narišemo na ({predmet['x']}, {predmet['y']}) s polmerom {predmet['polmer']}."


def premakni_igralca(stanje, smer):
    if smer == "levo":
        stanje["x"] -= stanje["hitrost"]
    elif smer == "desno":
        stanje["x"] += stanje["hitrost"]
    elif smer == "gor":
        stanje["y"] -= stanje["hitrost"]
    elif smer == "dol":
        stanje["y"] += stanje["hitrost"]
    return stanje


def omeji_na_zaslon(stanje, nastavitve):
    stanje["x"] = max(0, min(stanje["x"], nastavitve["sirina"] - stanje["sirina"]))
    stanje["y"] = max(0, min(stanje["y"], nastavitve["visina"] - stanje["visina"]))
    return stanje


def je_trk(prvi, drugi):
    return (
        prvi["x"] < drugi["x"] + drugi["polmer"]
        and prvi["x"] + prvi["sirina"] > drugi["x"] - drugi["polmer"]
        and prvi["y"] < drugi["y"] + drugi["polmer"]
        and prvi["y"] + prvi["visina"] > drugi["y"] - drugi["polmer"]
    )


def hud(vrednost_tock):
    return f"Besedilo HUD: Točke = {vrednost_tock}"


print("Naloga 1")
print(ustvari_okno(okno))

print("\\nNaloga 2")
print(f"Ali igra teče naprej po dogodku QUIT? {obdela_dogodek('QUIT')}")

print("\\nNaloga 3")
print(barva_ozadja(ozadje))

print("\\nNaloga 4")
print(narisi_pravokotnik(igralec))
print(narisi_krog(tarca))

print("\\nNaloga 5")
premakni_igralca(igralec, "desno")
premakni_igralca(igralec, "dol")
print(igralec)

print("\\nNaloga 6")
igralec["x"] = 999
igralec["y"] = -20
print(omeji_na_zaslon(igralec, okno))

print("\\nNaloga 7")
print(f"Trk s tarco: {je_trk(igralec, tarca)}")

print("\\nNaloga 8")
if je_trk(igralec, tarca):
    tocke += 1
print(hud(tocke))

print("\\nNaloga 9")
print("V pygame bi tukaj dodali izpis besedila z ukazom font.render(...).")

print("\\nNaloga 10")
print("Vrstni red glavne zanke je: dogodki -> premik -> omejitev -> trki -> risanje.")
