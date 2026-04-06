"""Rešitve učnega lista – 21 – Slovarji v praksi – socialno omrežje."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

seznam_uporabnikov = [
    {"uime": "ana", "ugeslo": "ana123", "sledilci": 120, "spol": "Ž"},  # 0
    {"uime": "miha", "ugeslo": "miha123", "sledilci": 80},  # 1
    {"uime": "luka", "ugeslo": "luka123", "sledilci": 300, "spol": "M"},  # 2
    {"uime": "eva", "ugeslo": "eva123", "sledilci": 45},  # 3
]


# Naloga 1 <<<< Funkcija izpiše ime in st. sledilcev.
def izpisi_profil(uporabnik):
    print(f"Uporabniško ime je: {uporabnik['uime']}")
    print(f"Št. sledilcev: {uporabnik['sledilci']}")


# Naloga 2 <<<< Funkcija preveri, ce se geslo ujema z vpisanim geslom.
def preveri_geslo(uporabnik, vpisani_geslo):
    if uporabnik["ugeslo"] == vpisani_geslo:
        print("Prijava uspešna ✅")
    else:
        print("Napačno geslo ❌")


# Naloga 4  <<<< Funkcija izpise vse uporabnike iz seznama.
def izpisi_uporabnike(seznam_uporabnikov):
    for uporabnik in seznam_uporabnikov:
        izpisi_profil(uporabnik)
        print("------")  # Malo vizuala, da se lažje loči uporabnike
