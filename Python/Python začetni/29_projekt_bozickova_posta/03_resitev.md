# Rešitev / učiteljske usmeritve – 29 – Projekt – Božičkova pošta

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `moija_prva_igra.py`

```python
import pygame
import sys # To knj. bomo imeli, da zakljucimo izvajanje

# Ustvarimo in pricnemo uporabljati okolje pygame
pygame.init()

WIDTH = 800 # sirina
HEIGHT = 500 # visina

# Zacetna pozicija igralca
x = WIDTH // 2 - 15
y = HEIGHT // 2 - 15
speed = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Naša prva igra") # Naslov okna


while True:
    # Preverimo kateri dogodki so se zgodili
    for event in pygame.event.get():
        
        # Preverimo ce je bil pritisnjen X.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Uporabimo knjiznico, da se zapre okno pygame
    
    # --- KODO ZA PREMIKANJE
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x = x - speed
    if keys[pygame.K_RIGHT]:
        x = x + speed
    
            
    # ========
    screen.fill((0, 0, 255)) # (R, G, B)
    pygame.draw.rect(screen,(225, 211, 0), (100, 100, 60, 30)) # OBJEKT 1
    pygame.draw.rect(screen, (83, 232, 205), (x, y, 30, 30)) # IGRALEC

    pygame.display.update()
```

### Izsek iz `santa_game.py`

```python
import pygame
from random import randint


SIRINA_ZASLONA = 800
VISINA_ZASLONA = 500

def main():
    pygame.init()
    pygame.display.set_caption("IME IGRE")
    
    # Nastavitve zaslona, ure in pisave
    ZASLON = pygame.display.set_mode((SIRINA_ZASLONA, VISINA_ZASLONA))
    URA = pygame.time.Clock()
    PISAVA = pygame.font.SysFont(None, 32)


    # Položaj in dimenzije lika
    santa_x = SIRINA_ZASLONA // 2
    santa_y = VISINA_ZASLONA - 60
    santa_w = 50 # Sirina lika
    santa_h = 40 # Visina lika


    # Seznam za padanje predmetov
    emails = []
    stevilo_tock = 0
    stevilo_zivljenj = 3
    
    # Določitev začetka igre
    nadaljuj_igro = True
    while nadaljuj_igro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nadaljuj_igro = False

        # Premikanje lika
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            santa_x -= 6
        if keys[pygame.K_RIGHT]:
            santa_x += 6

        # Omejitev gibanja lika znotraj zaslona
        santa_x = max(0, min(SIRINA_ZASLONA - santa_w, santa_x))

        
        # Dodajanje novih predmetov
        if randint(1, 25) == 1:
            email = {
                "x": randint(0, 770), # naključna x pozicija
                "y": -30, # začetna y pozicija (vedno nad zaslonom)
                "speed": randint(3, 6), # hitrost padanja
                "type": "spam" if randint(1, 4) == 1 else "good" # 25% možnost za spam
            }
            emails.append(email)


        # Ozadje in risanje lika ter predmetov
        ZASLON.fill((100, 100, 100))

        # Risanje lika
        santa_rect = pygame.Rect(santa_x, santa_y, santa_w, santa_h)
        pygame.draw.rect(ZASLON, (220, 40, 40), santa_rect)

        # Posodabljanje in risanje predmetov
        for email in emails[:]:
            
            # Posodobi pozicijo y (pade navzdol)
            email["y"] += email["speed"]
            # Ustvari pravokotnik za predmet
            rect = pygame.Rect(email["x"], email["y"], 20, 20)

            # Preverimo ali se je predmet dotaknil bozicnega lika.
            if rect.colliderect(santa_rect):
                if email["type"] == "good":
                    stevilo_tock += 1
                else:
                    stevilo_zivljenj -= 1
                emails.remove(email)
                continue
            
            # Določimo barvo glede na tip predmeta
            color = (0, 200, 100) if email["type"] == "good" else (255, 120, 0)
            pygame.draw.rect(ZASLON, color, rect)

        text = PISAVA.render(f"Točke: {stevilo_tock}   Življenj: {stevilo_zivljenj}", True, (255, 255, 255))
        ZASLON.blit(text, (10, 10))

        # Preverimo ce nimamo vec zivljenj
```

## Tipične napake

- manjkajoč `:` pri pogojih ali funkcijah,
- napačna zamaknitev bloka kode,
- pozabljena pretvorba `input()` v `int()` ali `float()`,
- napačno ime spremenljivke,
- učenec ne zažene programa po vsakem manjšem koraku.

## Minimalni kriterij uspeha

- učenec zaključi obvezno jedro sklopa in ga zna demonstrirati,
- učenec zna povedati, kje v kodi je bilo treba kaj popraviti,
- vsaj enkrat samostojno uporabi testiranje med delom.

## Učiteljski checkpointi

1. 🧱 KORAK 1 — Odpri okno
2. Ustvari okno velikosti **800 × 500**
3. Uporabi **seznam**, v katerem shranjuješ emaile

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
