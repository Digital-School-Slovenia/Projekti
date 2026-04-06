"""Resitve dodatnih nalog - 18 Mesane vaje pred slovarji."""

def statistika(seznam):
    return min(seznam), max(seznam), sum(seznam) / len(seznam)


def samo_samoglasniki(besedilo):
    dovoljeni = "aeiou"
    return "".join(znak for znak in besedilo.lower() if znak in dovoljeni)


def pozitivna_stevila(seznam):
    return [stevilo for stevilo in seznam if stevilo > 0]


stevila = [7, -2, 14, 3, -1, 9]
minimum, maksimum, povprecje = statistika(stevila)
print(f"Minimum: {minimum}, maksimum: {maksimum}, povprecje: {povprecje:.2f}")
print(samo_samoglasniki("Programiranje"))
print(pozitivna_stevila(stevila))