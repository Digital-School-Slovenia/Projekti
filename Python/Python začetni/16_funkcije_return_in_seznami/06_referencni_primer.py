# Referenčni primer – 16 Funkcije, return in seznami

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.


def povprecje(seznam):
    if not seznam:
        return 0
    return sum(seznam) / len(seznam)


def filtriraj_pozitivna(seznam):
    rezultat = []
    for stevilo in seznam:
        if stevilo > 0:
            rezultat.append(stevilo)
    return rezultat


ocene = [5, 4, 5, 3, 4]
print("Povprečje:", povprecje(ocene))
print("Pozitivna števila:", filtriraj_pozitivna([-2, 5, 0, 7, -1, 3]))
