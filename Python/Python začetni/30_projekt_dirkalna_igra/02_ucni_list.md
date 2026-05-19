# Učni list – 30 – Projekt – Dirkalna igra

To je projektni sklop. Delaj po korakih, po vsakem koraku zaženi program in preveri, ali nova funkcionalnost res deluje, preden nadaljuješ.

## Cilj

Naredi preprosto dirkalno igro, kjer igralec vozi avto po cesti in se izogiba oviram.

## Korak 1: Osnovna datoteka

Ustvari `dirkalna_igra.py` in vanjo prilepi:

```python
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dirkalna igra")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)
```

## Korak 2: Dodaj barve in cesto

Pod osnovo dodaj:

```python
GRASS = (40, 140, 40)
ROAD = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 50, 50)
BLUE = (50, 120, 220)
YELLOW = (240, 220, 70)

ROAD_X = 100
ROAD_WIDTH = 300
```

## Korak 3: Dodaj igralca

Pod cesto dodaj:

```python
player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 7
```

## Korak 4: Dodaj oviro

Pod igralca dodaj:

```python
obstacle_width = 50
obstacle_height = 90
obstacle_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width)
obstacle_y = -120
obstacle_speed = 6

game_over = False
score = 0
```

## Korak 5: Dodaj glavno zanko in premikanje

Na konec programa dodaj:

```python
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        if player_x < ROAD_X:
            player_x = ROAD_X
        if player_x > ROAD_X + ROAD_WIDTH - player_width:
            player_x = ROAD_X + ROAD_WIDTH - player_width
```

## Korak 6: Dodaj premik ovire in score

Pod omejitev igralca dodaj:

```python
        obstacle_y += obstacle_speed

        if obstacle_y > HEIGHT:
            obstacle_y = -120
            obstacle_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width)
            score += 1
```

## Korak 7: Dodaj trk

Pod premik ovire dodaj:

```python
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

        if player_rect.colliderect(obstacle_rect):
            game_over = True
```

## Korak 8: Dodaj risanje

Na konec zanke dodaj:

```python
    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    for y in range(0, HEIGHT, 50):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 30))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    score_text = font.render(f"Točke: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = big_font.render("KONEC IGRE", True, YELLOW)
        screen.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))

    pygame.display.flip()

pygame.quit()
```
