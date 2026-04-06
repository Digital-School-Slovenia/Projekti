# Rešitve domače naloge – 15 Funkcije prvi koraki


def pozdrav(ime):
    return f"Hej, {ime}!"


def kvadrat(stevilo):
    return stevilo**2


def v_sekunde(minute):
    if minute < 0:
        return "Minute ne morejo biti negativne."
    return minute * 60


if __name__ == "__main__":
    print("Naloga 1")
    print(pozdrav("Matej"))

    print("\nNaloga 2")
    print(kvadrat(9))

    print("\nNaloga 3")
    print(v_sekunde(12))
    print(v_sekunde(-3))

    # Naloga 4 – primer kratkega odgovora:
    # Ustavil sem se pri preverjanju negativnih minut in sem težavo rešil z if stavkom.
