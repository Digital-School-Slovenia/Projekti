"""Resitve dodatnih nalog - 21 Socialno omrezje in slovarji."""

uporabniki = [
    {"ime": "ana", "geslo": "abc123", "sledilci": 120, "opis": "rada programira"},
    {"ime": "bor", "geslo": "geslo456", "sledilci": 85, "opis": "rad igra kosarko"},
]


def poisci_uporabnika(ime):
    for uporabnik in uporabniki:
        if uporabnik["ime"] == ime:
            return uporabnik
    return None


def prijava(ime, geslo):
    uporabnik = poisci_uporabnika(ime)
    if uporabnik and uporabnik["geslo"] == geslo:
        return True
    return False


def dodaj_uporabnika(ime, geslo, opis):
    uporabniki.append({"ime": ime, "geslo": geslo, "sledilci": 0, "opis": opis})


def priljubljeni(min_sledilcev):
    return [uporabnik for uporabnik in uporabniki if uporabnik["sledilci"] >= min_sledilcev]


print(prijava("ana", "abc123"))
dodaj_uporabnika("cene", "nova789", "nov clan omrezja")
print(priljubljeni(100))