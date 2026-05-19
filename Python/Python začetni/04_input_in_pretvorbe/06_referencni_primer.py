# Referenčni primer – 04 Input in pretvorbe
# Pazi: input() vrne niz, zato je pri številih potrebna pretvorba.

tvoje_ime = input("Vnesi tvoje ime: ")
print(f"Živjo, {tvoje_ime}!")

tvoja_starost = input("Vnesi svojo starost: ")
tvoja_starost = int(tvoja_starost)
print(f"Čez 10 let boš star {tvoja_starost + 10}")

tvoja_najljubsa_hrana = input("Vnesi svojo najljubso hrano: ")
print(f"Tvoja najljubša hrana je: {tvoja_najljubsa_hrana}")

tvoj_najljubsi_ucitelj = input("Vnesi ime svojega najljubšega učitelja: ")
print(f"Tvoj najljubši učitelj je: {tvoj_najljubsi_ucitelj}")
