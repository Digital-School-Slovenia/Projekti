"""Resitve dodatnih nalog - 09 While delavnica."""

print("Naloga 1")
prihranki = [5, 4, 6, 3]
cilj = 15
znesek = 0
indeks = 0
while znesek < cilj and indeks < len(prihranki):
    znesek += prihranki[indeks]
    indeks += 1
print(f"Privarcevan znesek: {znesek} EUR")

print("\nNaloga 2")
artikli = [2.5, 3.2, 1.8, 4.1]
skupaj = 0
indeks = 0
while indeks < len(artikli):
    skupaj += artikli[indeks]
    indeks += 1
print(f"Skupni znesek nakupa je {skupaj:.2f} EUR.")

print("\nNaloga 3")
gesla = ["abc", "123", "varno"]
indeks = 0
while indeks < len(gesla):
    if gesla[indeks] == "varno":
        print(f"Pravilno geslo po {indeks + 1}. poskusu.")
        break
    indeks += 1