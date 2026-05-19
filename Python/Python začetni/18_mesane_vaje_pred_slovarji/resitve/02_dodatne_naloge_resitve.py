"""Rešitve dodatnih nalog – 18 – Velika delavnica vaj – mešane naloge pred slovarji."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

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
