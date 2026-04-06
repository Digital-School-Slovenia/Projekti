# Učni list – 28 – Projekt – Mini Zelda

To je projektni sklop. Delaj po korakih, po vsakem koraku zaženi program in preveri, ali nova funkcionalnost res deluje, preden nadaljuješ.

## Cilj

Naredi preprosto top-down igro: igralec se giblje po svetu, pobira kovance, izgublja življenja in lahko napade sovražnika.

## Korak 1: Pripravi ogrodje

Ustvari datoteko `mini_zelda.py` in vanjo prilepi:

```python
import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 960, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Zelda")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

WHITE = (245, 245, 245)
BLACK = (25, 25, 25)
BLUE = (70, 120, 255)
RED = (220, 80, 80)
GREEN = (70, 200, 100)
YELLOW = (240, 210, 70)
GRAY = (70, 70, 70)
DARK_BG = (35, 35, 45)
```

## Korak 2: Dodaj igralca

Pod ogrodje dodaj:

```python
player = {
    "x": 0.0,
    "y": 0.0,
    "size": 40,
    "speed": 4,
    "hp": 5,
    "score": 0,
    "dir_x": 0,
    "dir_y": 1,
}
```

### Kaj dela ta del?

Igralca hranimo v slovarju. Tako imamo vse podatke na enem mestu.

## Korak 3: Dodaj sezname za predmete

Pod igralca dodaj:

```python
collectibles = []
enemies = []
attack_timer = 0
attack_rect = pygame.Rect(0, 0, 0, 0)
```

## Korak 4: Dodaj nekaj kovancev in sovražnikov

Pod sezname dodaj:

```python
for _ in range(12):
    collectibles.append({
        "x": random.randint(-800, 800),
        "y": random.randint(-600, 600),
        "size": 18,
    })

for _ in range(4):
    enemies.append({
        "x": random.randint(-700, 700),
        "y": random.randint(-500, 500),
        "size": 34,
        "speed": 1.2,
    })
```

## Korak 5: Dodaj funkcijo za pretvorbo koordinat

Pod začetne podatke dodaj:

```python
def world_to_screen(wx, wy, camera_x, camera_y):
    return int(wx - camera_x), int(wy - camera_y)
```

### Kaj dela ta del?

Objekti obstajajo v svetu, kamera pa pove, kateri del sveta trenutno vidimo.

## Korak 6: Dodaj glavno zanko

Na konec programa dodaj:

```python
running = True
game_over = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            attack_timer = 10

    keys = pygame.key.get_pressed()

    if not game_over:
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
            player["dir_x"], player["dir_y"] = -1, 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
            player["dir_x"], player["dir_y"] = 1, 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
            player["dir_x"], player["dir_y"] = 0, -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
            player["dir_x"], player["dir_y"] = 0, 1

        if dx != 0 or dy != 0:
            length = math.hypot(dx, dy)
            dx = dx / length * player["speed"]
            dy = dy / length * player["speed"]

        player["x"] += dx
        player["y"] += dy
```

## Korak 7: Dodaj pobiranje kovancev

Pod premik igralca dodaj:

```python
        player_rect = pygame.Rect(int(player["x"]), int(player["y"]), player["size"], player["size"])

        for coin in collectibles[:]:
            coin_rect = pygame.Rect(coin["x"], coin["y"], coin["size"], coin["size"])
            if player_rect.colliderect(coin_rect):
                collectibles.remove(coin)
                player["score"] += 1
```

## Korak 8: Dodaj sovražnike

Pod pobiranje kovancev dodaj:

```python
        for enemy in enemies:
            if enemy["x"] < player["x"]:
                enemy["x"] += enemy["speed"]
            if enemy["x"] > player["x"]:
                enemy["x"] -= enemy["speed"]
            if enemy["y"] < player["y"]:
                enemy["y"] += enemy["speed"]
            if enemy["y"] > player["y"]:
                enemy["y"] -= enemy["speed"]

            enemy_rect = pygame.Rect(int(enemy["x"]), int(enemy["y"]), enemy["size"], enemy["size"])
            if player_rect.colliderect(enemy_rect):
                player["hp"] -= 1
                enemy["x"] += random.randint(-120, 120)
                enemy["y"] += random.randint(-120, 120)
                if player["hp"] <= 0:
                    game_over = True
```

## Korak 9: Dodaj napad

Pod del za sovražnike dodaj:

```python
        if attack_timer > 0:
            attack_timer -= 1
            attack_rect = pygame.Rect(
                int(player["x"] + player["dir_x"] * 40),
                int(player["y"] + player["dir_y"] * 40),
                30,
                30,
            )

            for enemy in enemies[:]:
                enemy_rect = pygame.Rect(int(enemy["x"]), int(enemy["y"]), enemy["size"], enemy["size"])
                if attack_rect.colliderect(enemy_rect):
                    enemies.remove(enemy)
        else:
            attack_rect = pygame.Rect(0, 0, 0, 0)
```

## Korak 10: Dodaj kamero in risanje

Pod logiko dodaj:

```python
    camera_x = player["x"] - WIDTH // 2 + player["size"] // 2
    camera_y = player["y"] - HEIGHT // 2 + player["size"] // 2

    screen.fill(DARK_BG)

    for x in range(-2000, 2001, 80):
        sx1, sy1 = world_to_screen(x, -2000, camera_x, camera_y)
        sx2, sy2 = world_to_screen(x, 2000, camera_x, camera_y)
        pygame.draw.line(screen, GRAY, (sx1, sy1), (sx2, sy2))

    for y in range(-2000, 2001, 80):
        sx1, sy1 = world_to_screen(-2000, y, camera_x, camera_y)
        sx2, sy2 = world_to_screen(2000, y, camera_x, camera_y)
        pygame.draw.line(screen, GRAY, (sx1, sy1), (sx2, sy2))

    for coin in collectibles:
        sx, sy = world_to_screen(coin["x"], coin["y"], camera_x, camera_y)
        pygame.draw.rect(screen, YELLOW, (sx, sy, coin["size"], coin["size"]))

    for enemy in enemies:
        sx, sy = world_to_screen(enemy["x"], enemy["y"], camera_x, camera_y)
        pygame.draw.rect(screen, RED, (sx, sy, enemy["size"], enemy["size"]))

    px, py = world_to_screen(player["x"], player["y"], camera_x, camera_y)
    pygame.draw.rect(screen, BLUE, (px, py, player["size"], player["size"]))

    if attack_timer > 0:
        ax, ay = world_to_screen(attack_rect.x, attack_rect.y, camera_x, camera_y)
        pygame.draw.rect(screen, WHITE, (ax, ay, attack_rect.width, attack_rect.height))

    hud = font.render(f"HP: {player['hp']}   Score: {player['score']}", True, WHITE)
    screen.blit(hud, (12, 12))

    if game_over:
        over = font.render("GAME OVER", True, WHITE)
        screen.blit(over, (WIDTH // 2 - 70, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
```

### Kaj dela ta del?

- kamera sledi igralcu,
- riše kovance, sovražnike in igralca,
- izpiše `HP` in `score`.
