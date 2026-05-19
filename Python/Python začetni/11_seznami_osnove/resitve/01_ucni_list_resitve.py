"""Rešitve učnega lista – 11 – Seznami – osnove in izpis z zankami."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.

playlist = []
for i in range(5):
    pesem = input("Kako se imenuje pesem: ")
    playlist.append(pesem)

print("\nTvoja playlist:")
for pesem in playlist:
    print("-", pesem)
