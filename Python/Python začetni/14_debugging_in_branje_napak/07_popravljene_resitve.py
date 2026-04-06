# Popravljene rešitve – 14 Debugging

# 1) TypeError -> pretvorba v int
starost = int(input("Koliko si star? "))
print(starost + 10)

# 2) SyntaxError -> manjkal je dvopičje
for i in range(5):
    print(i)

# 3) NameError -> napačno ime spremenljivke
stevilo_tock = 10
print(stevilo_tock)

# 4) Logic error -> vsoto moramo seštevati
vsota = 0
for i in range(1, 6):
    vsota += i
print("Vsota je:", vsota)
