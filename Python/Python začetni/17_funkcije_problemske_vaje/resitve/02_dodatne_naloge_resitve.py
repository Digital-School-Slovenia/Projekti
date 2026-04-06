"""Resitve dodatnih nalog - 17 Funkcije problemske vaje."""

def vecji(a, b):
    return a if a > b else b


def je_sodo(stevilo):
    return stevilo % 2 == 0


def je_palindrom(beseda):
    beseda = beseda.lower()
    return beseda == beseda[::-1]


def prestej_crko(besedilo, crka):
    return besedilo.lower().count(crka.lower())


def odstrani_dvojnike(seznam):
    rezultat = []
    for element in seznam:
        if element not in rezultat:
            rezultat.append(element)
    return rezultat


print(vecji(12, 5))
print(je_sodo(18))
print(je_palindrom("Kajak"))
print(prestej_crko("Programiranje", "r"))
print(odstrani_dvojnike([1, 2, 2, 3, 1, 4]))