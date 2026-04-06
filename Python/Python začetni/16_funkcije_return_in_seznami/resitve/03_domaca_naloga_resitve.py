"""Resitve domace naloge - 16 Funkcije, return in seznami."""

def najcenejsi(cene):
    return min(cene)


def odrasli(starosti):
    return [starost for starost in starosti if starost >= 18]


def povisi(ocene):
    nove_ocene = []
    for ocena in ocene:
        nova_ocena = ocena + 1
        if nova_ocena > 10:
            nova_ocena = 10
        nove_ocene.append(nova_ocena)
    return nove_ocene


print(f"Najcenejsi izdelek stane {najcenejsi([3.4, 2.1, 5.0, 1.9])} EUR.")
print(odrasli([12, 17, 18, 21, 15]))
print(povisi([6, 8, 9, 10]))

print("Najbolj pomembno pri funkcijah je, da funkcija vrne rezultat in da jo lahko potem ponovno uporabim.")