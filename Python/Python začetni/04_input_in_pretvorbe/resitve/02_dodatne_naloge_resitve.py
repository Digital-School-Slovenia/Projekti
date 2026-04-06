"""Resitve dodatnih nalog - 04 Input in pretvorbe."""

def starost_cez_pet_let(starost_besedilo):
    starost = int(starost_besedilo)
    return starost + 5


def povprecje_treh(a_besedilo, b_besedilo, c_besedilo):
    a = float(a_besedilo)
    b = float(b_besedilo)
    c = float(c_besedilo)
    return (a + b + c) / 3


def pasja_leta(cloveska_leta_besedilo):
    cloveska_leta = int(cloveska_leta_besedilo)
    return cloveska_leta * 7


print("Naloga 1")
print(starost_cez_pet_let("14"))

print("\nNaloga 2")
print(f"Povprecje je {povprecje_treh('4.5', '5', '3.5'):.2f}.")

print("\nNaloga 3")
print(f"V pasjih letih je to {pasja_leta('6')}.")