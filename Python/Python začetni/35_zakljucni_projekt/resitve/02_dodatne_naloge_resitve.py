"""Rešitve dodatnih nalog – 35 – Zaključni projekt."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

projekt = {
    "ime": "Lov na zvezde",
    "mehanika": ["premikanje", "zbiranje predmetov", "sovrazniki"],
    "robustnost": ["restart", "zaslon game over", "potrditev zmage"],
    "hud": ["score", "zivljenja", "cas"],
}


def pocisti_imena():
    stara_imena = ["x1", "y1", "sp1"]
    nova_imena = ["player_x", "player_y", "player_speed"]
    return list(zip(stara_imena, nova_imena))


def meni_za_sosolca():
    return ["ENTER - zacetek", "R - restart", "ESC - izhod"]


print(projekt)
print(pocisti_imena())
print(meni_za_sosolca())
