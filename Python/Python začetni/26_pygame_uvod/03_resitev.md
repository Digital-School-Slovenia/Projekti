# Rešitev / učiteljske usmeritve – 26 – Pygame – uvod, okno, risanje in premikanje

## Kako vodiš to uro

- najprej okno, nato risanje, nato premikanje,
- ne skači takoj v 'pravo igro',
- po vsakem checkpointu naj vsi pokažejo, da program še dela.

## Minimalna referenčna rešitev

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

## Učiteljski checkpointi

1. Okno se odpre in zapre pravilno.
2. Nekaj je dejansko narisano na zaslonu.
3. Objekt se premika in ne uide z ekrana.

## Python datoteke v tej mapi

- `06_osnovna_struktura.py`
- `07_premik_kvadrata.py`
