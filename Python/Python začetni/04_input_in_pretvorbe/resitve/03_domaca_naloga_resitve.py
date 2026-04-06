"""Resitve domace naloge - 04 Input in pretvorbe."""

def predstavi_osebo(ime_besedilo, starost_besedilo):
    starost = int(starost_besedilo)
    return f"{ime_besedilo} je star {starost} let."


def pretvori_visino(cm_besedilo):
    centimetri = int(cm_besedilo)
    metri = centimetri / 100
    return metri


print("Naloga 1")
print(predstavi_osebo("Nina", "15"))

print("\nNaloga 2")
print(f"Visina 172 cm je {pretvori_visino('172'):.2f} m.")

print("\nNaloga 3")
print(f"Cez dve leti bo oseba stara {int('15') + 2} let.")

razmislek = "Pri pretvorbah je pomembno, da vhod iz input() spremenim v int ali float, preden racunam."
print("\nNaloga 4")
print(razmislek)