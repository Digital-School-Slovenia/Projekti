# Učni list – 32 – Projekt – Mini Wolfenstein

To je projektni sklop. Delaj po korakih, po vsakem koraku zaženi program in preveri, ali nova funkcionalnost res deluje, preden nadaljuješ.

## Cilj

Iz 2D mreže naredi lažni 3D pogled s pomočjo žarkov.

## Korak 1: Uvozi knjižnice in odpri okno

```python
import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Wolfenstein")
clock = pygame.time.Clock()
```

## Korak 2: Dodaj barve

```python
WHITE = (245, 245, 245)
BLACK = (10, 10, 10)
GRAY = (90, 90, 90)
BLUE = (80, 140, 220)
GREEN = (80, 200, 100)
YELLOW = (230, 220, 90)
```

## Korak 3: Dodaj mapo

```python
MAP_DATA = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1],
    [1,0,0,1,0,1,0,1],
    [1,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,2,1],
    [1,1,1,1,1,1,1,1],
]

TILE_SIZE = 64
MAP_ROWS = len(MAP_DATA)
MAP_COLS = len(MAP_DATA[0])
```

## Korak 4: Dodaj igralca

```python
player_x = 1.5 * TILE_SIZE
player_y = 1.5 * TILE_SIZE
player_angle = 0

MOVE_SPEED = 2.8
ROT_SPEED = 0.04
PLAYER_RADIUS = 10
```

## Korak 5: Dodaj pomožni funkciji

```python
def get_map_cell(world_x, world_y):
    col = int(world_x // TILE_SIZE)
    row = int(world_y // TILE_SIZE)

    if row < 0 or row >= MAP_ROWS or col < 0 or col >= MAP_COLS:
        return 1
    return MAP_DATA[row][col]


def is_wall(world_x, world_y):
    return get_map_cell(world_x, world_y) == 1
```

## Korak 6: Dodaj minimapo

```python
def draw_map_topdown():
    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            value = MAP_DATA[row][col]
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            color = BLACK
            if value == 1:
                color = GRAY
            elif value == 2:
                color = GREEN

            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE), 1)

    pygame.draw.circle(screen, YELLOW, (int(player_x), int(player_y)), PLAYER_RADIUS)
    end_x = player_x + math.cos(player_angle) * 30
    end_y = player_y + math.sin(player_angle) * 30
    pygame.draw.line(screen, YELLOW, (player_x, player_y), (end_x, end_y), 3)
```

## Korak 7: Dodaj raycasting

```python
FOV = math.pi / 3
NUM_RAYS = 240
MAX_DEPTH = 800
SCALE = WIDTH / NUM_RAYS


def cast_rays():
    start_angle = player_angle - FOV / 2

    for ray in range(NUM_RAYS):
        ray_angle = start_angle + (ray / NUM_RAYS) * FOV

        for depth in range(1, MAX_DEPTH, 2):
            target_x = player_x + math.cos(ray_angle) * depth
            target_y = player_y + math.sin(ray_angle) * depth

            if is_wall(target_x, target_y):
                corrected_depth = depth * math.cos(player_angle - ray_angle)
                wall_height = min(HEIGHT, 30000 / max(corrected_depth, 1))
                shade = max(40, 255 - depth // 3)
                color = (shade, shade, shade)
                pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - wall_height // 2, SCALE + 1, wall_height))
                break
```

## Korak 8: Dodaj glavno zanko

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_angle -= ROT_SPEED
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_angle += ROT_SPEED

    move_step = 0
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        move_step = MOVE_SPEED
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        move_step = -MOVE_SPEED

    next_x = player_x + math.cos(player_angle) * move_step
    next_y = player_y + math.sin(player_angle) * move_step

    if not is_wall(next_x, next_y):
        player_x = next_x
        player_y = next_y

    screen.fill((20, 20, 30))
    pygame.draw.rect(screen, (70, 120, 180), (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(screen, (50, 40, 30), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    cast_rays()
    draw_map_topdown()

    pygame.display.flip()
    clock.tick(60)
```
