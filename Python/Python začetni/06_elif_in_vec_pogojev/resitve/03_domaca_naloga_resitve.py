"""Resitve domace naloge - 06 Elif in vec pogojev."""

def del_dneva(ura):
    if ura < 6:
        return "noc"
    elif ura < 12:
        return "jutro"
    elif ura < 18:
        return "popoldne"
    return "vecer"


def starostna_skupina(starost):
    if starost < 13:
        return "otrok"
    elif starost < 18:
        return "najstnik"
    elif starost < 65:
        return "odrasel"
    return "starejsi"


print("Naloga 1")
print(del_dneva(15))

print("\nNaloga 2")
print(starostna_skupina(16))

print("\nNaloga 3")
semafor = "rumena"
if semafor == "zelena":
    print("Pojdi.")
elif semafor == "rumena":
    print("Pripravi se in pocakaj.")
else:
    print("Stoj.")

print("\nNaloga 4")
print("Pri vec pogojih pomaga, da gremo od najbolj ozkih primerov proti bolj splosnim.")