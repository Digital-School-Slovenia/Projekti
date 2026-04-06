"""Rešitve učnega lista – 10 – Zanka `for` in `range`."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

for i in range(1, 6):
    print(f"Korak {i}")

stevilo = int(input("Za katero število želiš poštevanko? "))
for i in range(1, 11):
    print(f"{stevilo} x {i} = {stevilo * i}")

vsota = 0
for i in range(1, 101):
    vsota += i
print(f"Vsota števil od 1 do 100 je {vsota}.")
