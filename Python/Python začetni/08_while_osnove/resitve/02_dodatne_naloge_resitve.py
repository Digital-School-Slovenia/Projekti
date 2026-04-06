"""Resitve dodatnih nalog - 08 While osnove."""

print("Naloga 1")
stevec = 1
while stevec <= 5:
    print(stevec)
    stevec += 1

print("\nNaloga 2")
odstevanje = 5
while odstevanje >= 1:
    print(odstevanje)
    odstevanje -= 1

print("\nNaloga 3")
vsota = 0
stevilo = 1
while stevilo <= 4:
    vsota += stevilo
    stevilo += 1
print(f"Vsota stevil od 1 do 4 je {vsota}.")

print("\nNaloga 4")
poskusi = ["1234", "geslo", "python"]
indeks = 0
while indeks < len(poskusi):
    if poskusi[indeks] == "python":
        print("Geslo je pravilno.")
        break
    indeks += 1