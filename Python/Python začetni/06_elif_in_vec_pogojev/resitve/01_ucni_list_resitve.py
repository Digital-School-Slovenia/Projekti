"""Rešitve učnega lista – 06 – `elif`, `else` in več možnosti odločanja."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

ocena = int(input("Vpiši oceno od 1 do 5: "))

if ocena == 5:
    print("Odlično!")
elif ocena == 4:
    print("Zelo dobro!")
elif ocena == 3:
    print("Dobro.")
elif ocena == 2:
    print("Dovolj.")
elif ocena == 1:
    print("Popravljaj.")
else:
    print("To ni veljavna ocena.")

vreme = input("Kakšno je vreme (sonce/dež/sneg)? ").lower()
if vreme == "sonce":
    print("Gremo ven.")
elif vreme == "dež":
    print("Vzemi dežnik.")
elif vreme == "sneg":
    print("Čas za kepanje.")
else:
    print("Danes je očitno vreme eksperimentalna poezija.")
