"""Resitve dodatnih nalog - 16 Funkcije, return in seznami."""

def najmanjsi(a, b, c):
    return min(a, b, c)


def povprecje_seznama(seznam):
    return sum(seznam) / len(seznam)


def stevilo_pojavitev(seznam, iskani):
    return seznam.count(iskani)


def polnoletni(starosti):
    return [starost for starost in starosti if starost >= 18]


print(najmanjsi(7, 3, 9))
print(f"Povprecje: {povprecje_seznama([2, 4, 6, 8]):.2f}")
print(stevilo_pojavitev([1, 2, 2, 3, 2], 2))
print(polnoletni([14, 18, 21, 16, 30]))