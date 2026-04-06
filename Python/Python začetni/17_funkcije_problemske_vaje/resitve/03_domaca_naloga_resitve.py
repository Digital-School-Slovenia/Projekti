"""Resitve domace naloge - 17 Funkcije problemske vaje."""

def daljsi_niz(prvi, drugi):
    return prvi if len(prvi) >= len(drugi) else drugi


def primerjaj_seznama(prvi, drugi):
    return prvi == drugi


def pravilni_zapis(ime, priimek):
    return f"{priimek.title()}, {ime.title()}"


print(daljsi_niz("miza", "program"))
print(primerjaj_seznama([1, 2, 3], [1, 2, 3]))
print(pravilni_zapis("ana", "novak"))

print("Pri teh nalogah pomaga, da problem razbijem na majhne funkcije z enim jasnim ciljem.")