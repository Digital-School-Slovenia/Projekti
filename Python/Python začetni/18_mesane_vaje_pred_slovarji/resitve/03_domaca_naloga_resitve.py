"""Resitve domace naloge - 18 Mesane vaje pred slovarji."""


def stevilo_samoglasnikov(besedilo):
    samoglasniki = "aeiou"
    return sum(1 for znak in besedilo.lower() if znak in samoglasniki)


def povprecje_brez_nicel(seznam):
    filtrirani = [stevilo for stevilo in seznam if stevilo != 0]
    return sum(filtrirani) / len(filtrirani)


def sodi_stevci(seznam):
    return [stevilo for stevilo in seznam if stevilo % 2 == 0]


print(stevilo_samoglasnikov("Racunalnik"))
print(f"Povprecje brez nicel: {povprecje_brez_nicel([0, 5, 7, 0, 8]):.2f}")
print(sodi_stevci([1, 2, 3, 4, 5, 6]))

print(
    "V mesanih vajah je pomembno, da prepoznam, ali bolj potrebujem if, zanko ali funkcijo."
)
