# Referenčni primer – 05 If osnove

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

starost = int(input("Vpiši svojo starost: "))

if starost >= 18:
    print("Lahko voziš avto!")
    print("JUHU!")
else:
    print("Ne smeš še voziti avta.")
    print("ŠKODA!")

ime = input("Vpiši ime: ")
if ime == "Brina":
    print("Legendica!")
else:
    print("Nisi Brina, a si vseeno kul 😀")
