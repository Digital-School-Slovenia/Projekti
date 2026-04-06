# Učni list – 33 – Projekt – Dodge the Meteors

To je projektni sklop. Delaj po korakih, po vsakem koraku zaženi program in preveri, ali nova funkcionalnost res deluje, preden nadaljuješ.

## Cilj

Premikaj ladjo levo/desno in se izogibaj meteorjem. Vsaka sekunda preživetja naj prinese točko.

## Korak 1: Začetna datoteka

Ustvari `dodge_the_meteors.py` in vanjo prilepi:

```python
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Meteors")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
```

## Korak 2: Dodaj ladjo

```python
player_w, player_h = 60, 30
player = pygame.Rect(WIDTH // 2 - player_w // 2, HEIGHT - 60, player_w, player_h)
player_speed = 7
```

## Korak 3: Dodaj meteorje in timer

```python
meteors = []
meteor_speed_min = 4
meteor_speed_max = 8

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 600)

score = 0
frame_count = 0
```

## Korak 4: Dodaj glavno zanko

```python
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

## Korak 5: Dodaj spawn meteorjev

V event loop dodaj:

```python
        if event.type == SPAWN_EVENT:
            mw = random.randint(25, 60)
            mh = random.randint(25, 60)
            mx = random.randint(0, WIDTH - mw)
            my = -mh
            meteors.append(pygame.Rect(mx, my, mw, mh))
```

## Korak 6: Dodaj premikanje ladje

Pod event loop dodaj:

```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
```

## Korak 7: Dodaj posodobitev meteorjev in score

Pod premikanje igralca dodaj:

```python
    for m in meteors:
        m.y += random.randint(meteor_speed_min, meteor_speed_max)

    meteors = [m for m in meteors if m.top < HEIGHT + 50]

    frame_count += 1
    if frame_count >= 60:
        score += 1
        frame_count = 0
```

## Korak 8: Dodaj trk

Pod score dodaj:

```python
    for m in meteors:
        if player.colliderect(m):
            running = False
```

## Korak 9: Dodaj risanje

Pod logiko dodaj:

```python
    screen.fill((10, 10, 30))

    pygame.draw.rect(screen, (50, 200, 255), player)

    for m in meteors:
        pygame.draw.rect(screen, (180, 120, 80), m)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
```

## Korak 10: Dodaj game over zaslon

Pod zanko dodaj:

```python
screen.fill((0, 0, 0))
go1 = font.render("GAME OVER", True, (255, 80, 80))
go2 = font.render(f"Final score: {score}", True, (255, 255, 255))
screen.blit(go1, (WIDTH//2 - go1.get_width()//2, HEIGHT//2 - 40))
screen.blit(go2, (WIDTH//2 - go2.get_width()//2, HEIGHT//2 + 10))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
```
