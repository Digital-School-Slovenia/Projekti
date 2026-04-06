"""Resitve domace naloge - 21 Socialno omrezje in slovarji."""

uporabniki = [
    {"ime": "nina", "geslo": "nina123", "sledilci": 45, "opis": "risem stripe"},
    {"ime": "tim", "geslo": "tim321", "sledilci": 91, "opis": "igram kitaro"},
]


def registriraj(ime, geslo, opis):
    nov_uporabnik = {"ime": ime, "geslo": geslo, "sledilci": 0, "opis": opis}
    uporabniki.append(nov_uporabnik)
    return nov_uporabnik


def posodobi_opis(ime, nov_opis):
    for uporabnik in uporabniki:
        if uporabnik["ime"] == ime:
            uporabnik["opis"] = nov_opis
            return uporabnik
    return None


def najdi_uporabnika(ime):
    for uporabnik in uporabniki:
        if uporabnik["ime"] == ime:
            return uporabnik
    return None


print(registriraj("eva", "eva999", "ucim se Python"))
print(posodobi_opis("tim", "igram kitaro in programiram"))
print(najdi_uporabnika("nina"))
print("Pri tej nalogi pomaga, da uporabnika vedno obravnavam kot en slovar v seznamu slovarjev.")