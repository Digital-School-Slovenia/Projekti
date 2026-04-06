# Referenčni primer – 04 Input in pretvorbe
# Pazi: input() vrne niz, zato je pri številih potrebna pretvorba.

tvoje_ime = input("Vnesi tvoje ime: ")
print(f"Živijo, {tvoje_ime}")

tvoja_starost = input("Vnesi svojo starost: ")
tvoja_starost = int(tvoja_starost)
print(f"Čez 10 let boš star {tvoja_starost + 10}")

tvoja_najljubsa_hrana = input("Vnesi svojo najljubso hrano: ")
print(f"Tvoja naljubsa hrana je: {tvoja_najljubsa_hrana}")

tvoj_naljubsi_ucitelj = input("Vnesi ime svojega najljubsega ucitelja:")
print(f"Tvoj naljubsi ucitelj: {tvoj_naljubsi_ucitelj}")