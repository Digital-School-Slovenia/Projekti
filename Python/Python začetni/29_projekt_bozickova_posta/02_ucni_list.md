# Učni list – 29 – Projekt – Božičkova pošta

## Cilj

Pomagaj Božičku ujeti dobre emaile in se izogniti spamu.

## Korak 1: Odpri okno

Ustvari datoteko `bozickova_posta.py` in vanjo prilepi:

```python
import pygame
from random import randint

SIRINA_ZASLONA = 800
VISINA_ZASLONA = 500

def main():
    pygame.init()
    pygame.display.set_caption("Božičkova pošta")

    ZASLON = pygame.display.set_mode((SIRINA_ZASLONA, VISINA_ZASLONA))
    URA = pygame.time.Clock()
    PISAVA = pygame.font.SysFont(None, 32)
```

## Korak 2: Dodaj Božička

Pod nastavitve zaslona dodaj:

```python
    santa_x = SIRINA_ZASLONA // 2
    santa_y = VISINA_ZASLONA - 60
    santa_w = 50
    santa_h = 40
```

V glavni zanki bomo iz tega naredili `Rect`.

## Korak 3: Dodaj začetne sezname in števce

Pod Božička dodaj:

```python
    emails = []
    stevilo_tock = 0
    stevilo_zivljenj = 3
```

## Korak 4: Dodaj glavno zanko

Pod začetne podatke dodaj:

```python
    nadaljuj_igro = True
    while nadaljuj_igro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nadaljuj_igro = False
```

## Korak 5: Dodaj premikanje Božička

V glavni zanki dodaj:

```python
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            santa_x -= 6
        if keys[pygame.K_RIGHT]:
            santa_x += 6

        santa_x = max(0, min(SIRINA_ZASLONA - santa_w, santa_x))
```

## Korak 6: Dodaj nove emaile

V glavni zanki, po premikanju, dodaj:

```python
        if randint(1, 25) == 1:
            email = {
                "x": randint(0, 770),
                "y": -30,
                "speed": randint(3, 6),
                "type": "spam" if randint(1, 4) == 1 else "good"
            }
            emails.append(email)
```

## Korak 7: Dodaj risanje Božička

V zanki dodaj draw del:

```python
        ZASLON.fill((100, 100, 100))

        santa_rect = pygame.Rect(santa_x, santa_y, santa_w, santa_h)
        pygame.draw.rect(ZASLON, (220, 40, 40), santa_rect)
```

## Korak 8: Posodobi in nariši emaile

Pod risanje Božička dodaj:

```python
        for email in emails[:]:
            email["y"] += email["speed"]
            rect = pygame.Rect(email["x"], email["y"], 20, 20)

            if rect.colliderect(santa_rect):
                if email["type"] == "good":
                    stevilo_tock += 1
                else:
                    stevilo_zivljenj -= 1
                emails.remove(email)
                continue

            color = (0, 200, 100) if email["type"] == "good" else (255, 120, 0)
            pygame.draw.rect(ZASLON, color, rect)
```

## Korak 9: Dodaj HUD in konec igre

Pod email loop dodaj:

```python
        text = PISAVA.render(f"Točke: {stevilo_tock}   Življenj: {stevilo_zivljenj}", True, (255, 255, 255))
        ZASLON.blit(text, (10, 10))

        if stevilo_zivljenj <= 0:
            nadaljuj_igro = False

        pygame.display.flip()
        URA.tick(60)

    pygame.quit()

main()
```

### Kaj dela ta del?

- izpiše točke in življenja,
- konča igro, ko zmanjka življenj.
