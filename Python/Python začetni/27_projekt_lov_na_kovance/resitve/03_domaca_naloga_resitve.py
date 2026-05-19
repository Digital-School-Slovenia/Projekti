"""Rešitve domače naloge – 27 – Projekt – Lov na kovance."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 820, 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lov na zvezde")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 56)

BACKGROUND = (20, 55, 45)
PLAYER_COLOR = (80, 220, 210)
STAR_COLOR = (255, 245, 120)
BONUS_COLOR = (255, 120, 200)
TEXT_COLOR = (255, 255, 255)


def nakljucni_kovanec():
    x_polozaj = random.randint(20, WIDTH - 40)
    y_polozaj = random.randint(20, HEIGHT - 40)
    return pygame.Rect(x_polozaj, y_polozaj, 20, 20)


def reset_game():
    global player, coins, bonus_star, score, won
    player = pygame.Rect(60, HEIGHT - 80, 42, 42)
    coins = [nakljucni_kovanec() for _ in range(10)]
    bonus_star = pygame.Rect(WIDTH - 120, 70, 24, 24)
    score = 0
    won = False


player = pygame.Rect(60, HEIGHT - 80, 42, 42)
coins = []
bonus_star = pygame.Rect(0, 0, 0, 0)
score = 0
won = False
reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and won and event.key == pygame.K_r:
            reset_game()

    if not won:
        keys = pygame.key.get_pressed()

        # Premikanje
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_UP]:
            player.y -= 5
        if keys[pygame.K_DOWN]:
            player.y += 5

        player.clamp_ip(screen.get_rect())

        # Pobiranje kovancev
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1

        if player.colliderect(bonus_star):
            score += 3
            bonus_star = pygame.Rect(-100, -100, 24, 24)

        if not coins:
            won = True

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    for coin in coins:
        pygame.draw.circle(screen, STAR_COLOR, coin.center, 10)

    pygame.draw.circle(screen, BONUS_COLOR, bonus_star.center, 12)

    # Izpis rezultata
    score_text = font.render(f"Točke: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (15, 15))

    if won:
        title = big_font.render("Zmaga!", True, TEXT_COLOR)
        help_text = font.render("Pritisni R za novo igro.", True, TEXT_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(
            help_text, help_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
