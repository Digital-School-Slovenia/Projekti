"""Rešitve učnega lista – 27 – Projekt – Lov na kovance."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

import pygame
import sys
import random

# -----------------------------
# Inicializacija Pygame
# -----------------------------
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lov na kovance")

# Ura za omejitev FPS (da igra teče enakomerno)
clock = pygame.time.Clock()

# Pisavi
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 56)

# Barve
BG_COLOR = (30, 30, 60)
PLAYER_COLOR = (200, 50, 50)
COIN_COLOR = (255, 220, 0)
TEXT_COLOR = (255, 255, 255)

# -----------------------------
# Nastavitve igralca
# -----------------------------
PLAYER_SIZE = 50
player = pygame.Rect(400, 400, PLAYER_SIZE, PLAYER_SIZE)
speed = 5


# -----------------------------
# Funkcija za reset igre
# -----------------------------
def reset_game():
    """Ponastavi položaj igralca, kovance in rezultat."""
    global player, coins, score, game_won

    # Igralca postavimo na začetni položaj
    player.x = 400
    player.y = 400

    # Kovance predstavljamo kot RECT-e (lažje za kolizijo)
    # Kovanec je kvadratek 20x20, rišemo pa ga kot krog
    coin_positions = []
    coins = []
    for i in range(10):  # Dodamo še nekaj naključnih kovancev
        x = random.randint(20, WIDTH - 20)
        y = random.randint(20, HEIGHT - 20)
        coin_positions.append((x, y))

        coins.append(pygame.Rect(x - 10, y - 10, 20, 20))  # Dodamo še v seznam kovancev

    score = 0
    game_won = False


# Začetni zagon podatkov
coins = []
score = 0
game_won = False
reset_game()

# -----------------------------
# Glavna zanka igre
# -----------------------------
while True:
    # -------------------------
    # 1) Obdelava dogodkov
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # # Če je tipka pritisnjena
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         pygame.quit()
        #         sys.exit()

        #     # Restart igre po zmagi (ali kadarkoli, če želiš)
        #     if event.key == pygame.K_r:
        #         reset_game()

    # -------------------------
    # 2) Branje tipk in premik
    # -------------------------
    keys = pygame.key.get_pressed()

    # Premik omogočimo samo, če igra še ni končana
    if not game_won:
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        # Igralca omejimo znotraj okna
        # (da ne gre čez rob)
        if player.left < 0:
            player.left = 0
        if player.right > WIDTH:
            player.right = WIDTH
        if player.top < 0:
            player.top = 0
        if player.bottom > HEIGHT:
            player.bottom = HEIGHT

    # -------------------------
    # 3) Logika (kolizije)
    # -------------------------
    # Iteriramo čez KOPIJO seznama (coins[:]),
    # ker med iteracijo kovance odstranjujemo.
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Če ni več kovancev, je igra dobljena
    if len(coins) == 0:
        game_won = True

    # -------------------------
    # 4) Risanje
    # -------------------------
    # Počistimo zaslon (zelo pomembno v vsaki iteraciji)
    screen.fill(BG_COLOR)

    # Narišemo igralca
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # Narišemo kovance
    for coin in coins:
        # coin.center vrne središče rect-a -> super za krog
        pygame.draw.circle(screen, COIN_COLOR, coin.center, 10)

    # UI: rezultat
    score_text = font.render(f"Točke: {score}", True, TEXT_COLOR)
    remaining_text = font.render(f"Preostali kovanci: {len(coins)}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(remaining_text, (10, 45))

    # Če je zmaga, pokažemo sporočilo
    if game_won:
        win_text = big_font.render("Zmaga! 🎉", True, (255, 255, 255))
        info_text = font.render(
            "Pritisni R za novo igro ali ESC za izhod", True, (255, 255, 255)
        )

        # Centriranje besedila
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        info_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

        screen.blit(win_text, win_rect)
        screen.blit(info_text, info_rect)

    # Osvežimo prikaz
    pygame.display.update()

    # Omejimo hitrost na 60 sličic na sekundo
    clock.tick(60)
