# Učni list – 27 – Projekt – Lov na kovance

## Cilj

Naredi igro, v kateri se igralec premika po zaslonu, pobira kovance in nabira točke.

## Korak 1: Ustvari novo datoteko in odpri okno

Ustvari datoteko `lov_na_kovance.py` in vanjo prilepi:

```python
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lov na kovance")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

### Kaj dela ta del?

- Ustvari `pygame` okno.
- Omogoči zapiranje z gumbom `X`.

## Korak 2: Dodaj uro in ozadje

Pod `pygame.display.set_caption(...)` dodaj:

```python
clock = pygame.time.Clock()
BG_COLOR = (30, 30, 60)
```

Na konec zanke dodaj:

```python
    screen.fill(BG_COLOR)
    pygame.display.update()
    clock.tick(60)
```

### Kaj dela ta del?

- `clock.tick(60)` omeji igro na 60 FPS.
- `fill` pobriše star frame.

## Korak 3: Dodaj igralca

Pred `while True:` dodaj:

```python
PLAYER_COLOR = (200, 50, 50)
PLAYER_SIZE = 50
player = pygame.Rect(400, 400, PLAYER_SIZE, PLAYER_SIZE)
speed = 5
```

V draw del, med `screen.fill(...)` in `pygame.display.update()`, dodaj:

```python
    pygame.draw.rect(screen, PLAYER_COLOR, player)
```

### Kaj dela ta del?

- `player` je rdeč kvadrat.
- `speed` določa hitrost premika.

## Korak 4: Dodaj premikanje igralca

Pod `for event in pygame.event.get(): ...` dodaj:

```python
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
```

### Kaj dela ta del?

- Bere puščice.
- Premika igralca.
- Poskrbi, da igralec ne pobegne iz okna.

## Korak 5: Dodaj kovance

Pred `while True:` dodaj:

```python
COIN_COLOR = (255, 220, 0)
coins = [
    pygame.Rect(100 - 10, 100 - 10, 20, 20),
    pygame.Rect(300 - 10, 200 - 10, 20, 20),
    pygame.Rect(500 - 10, 150 - 10, 20, 20),
    pygame.Rect(700 - 10, 250 - 10, 20, 20),
]
```

V draw del dodaj:

```python
    for coin in coins:
        pygame.draw.circle(screen, COIN_COLOR, coin.center, 10)
```

### Kaj dela ta del?

- `coins` je seznam kovancev.
- Vsak kovanec narišemo kot rumen krog.

## Korak 6: Dodaj score in pobiranje kovancev

Pred `while True:` dodaj:

```python
score = 0
font = pygame.font.SysFont(None, 36)
TEXT_COLOR = (255, 255, 255)
```

Po premiku igralca dodaj:

```python
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
```

V draw del dodaj:

```python
    text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))
```

### Kaj dela ta del?

- Ob dotiku kovanca se ta odstrani.
- `score` se poveča za 1.

## Korak 7: Dodaj zmago

Pred `while True:` dodaj:

```python
big_font = pygame.font.SysFont(None, 56)
game_won = False
```

Po pobiranju kovancev dodaj:

```python
    if len(coins) == 0:
        game_won = True
```

V draw del dodaj:

```python
    if game_won:
        win_text = big_font.render("Zmaga!", True, TEXT_COLOR)
        info = font.render("R = nova igra, ESC = izhod", True, TEXT_COLOR)
        screen.blit(win_text, win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
```

### Kaj dela ta del?

- Ko pobereš vse kovance, se pokaže zaslon za zmago.

## Korak 8: Dodaj restart in izhod

V del za dogodke dodaj:

```python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_r:
                player.x, player.y = 400, 400
                coins = [
                    pygame.Rect(100 - 10, 100 - 10, 20, 20),
                    pygame.Rect(300 - 10, 200 - 10, 20, 20),
                    pygame.Rect(500 - 10, 150 - 10, 20, 20),
                    pygame.Rect(700 - 10, 250 - 10, 20, 20),
                ]
                score = 0
                game_won = False
```

### Kaj dela ta del?

- `ESC` zapre igro.
- `R` vrne začetno stanje.
