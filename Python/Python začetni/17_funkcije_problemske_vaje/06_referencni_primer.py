# Referenčni primer – 17 Funkcije problemske vaje

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.


def je_palindrom(beseda):
    beseda = beseda.lower().replace(" ", "")
    return beseda == beseda[::-1]


def st_prestopov(meja, podatki):
    stevec = 0
    for vrednost in podatki:
        if vrednost > meja:
            stevec += 1
    return stevec


print(je_palindrom("Kajak"))
print(st_prestopov(10, [4, 12, 9, 18, 3, 11]))
