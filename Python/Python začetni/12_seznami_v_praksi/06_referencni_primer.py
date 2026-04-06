# Referenčni primer – 12 Seznami v praksi

kosarica = []

while True:
    izdelek = input("Dodaj izdelek (ali 'konec'): ").strip()
    if izdelek.lower() == 'konec':
        break
    kosarica.append(izdelek)

print("\nV košarici imaš:")
for i, izdelek in enumerate(kosarica, start=1):
    print(f"{i}. {izdelek}")
