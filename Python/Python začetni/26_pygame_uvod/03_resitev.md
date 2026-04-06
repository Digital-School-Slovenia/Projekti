# Rešitev – 26 – Pygame – uvod, okno, risanje in premikanje

Tukaj je jedro rešitve za sklop **26 – Pygame – uvod, okno, risanje in premikanje**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Najprej okno, nato risanje, nato premikanje
- Ne skači takoj v 'pravo igro'
- Po vsakem kratek pregledu naj vsi pokažejo, da program še dela.

## Primer rešitve

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Moja prva igra")
clock = pygame.time.Clock()

x, y = 300, 200
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    x = max(0, min(800 - 50, x))

    screen.fill((0, 0, 100))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 40))
    pygame.display.update()
    clock.tick(60)
```

## Kaj mora do konca ure delovati

- Okno se odpre in zapre pravilno.
- Nekaj je dejansko narisano na zaslonu.
- Objekt se premika in ne uide z ekrana.

## Hitri pregled med uro

- Okno se odpre in zapre pravilno.
- Nekaj je dejansko narisano na zaslonu.
- Objekt se premika in ne uide z ekrana.

## Tipične napake

- Pozabljena dvopičja ali oklepaji.
- Napačna zamaknitev kode.
- Napačno ime spremenljivke ali funkcije.
- Program ni pognan po zadnji spremembi.

## Datoteke v tej mapi

- `06_osnovna_struktura.py`
- `07_premik_kvadrata.py`
