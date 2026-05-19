"""Rešitve dodatnih nalog – 27 – Projekt – Lov na kovance."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lov na kovance – dodatne naloge")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 34)
big_font = pygame.font.SysFont(None, 60)

BG_COLOR = (25, 35, 70)
FLASH_COLOR = (45, 70, 120)
PLAYER_COLOR = (235, 100, 90)
COIN_COLOR = (255, 215, 0)
ENEMY_COLOR = (80, 220, 160)
TEXT_COLOR = (255, 255, 255)

TIME_LIMITS = {1: 30, 2: 20}


def ustvari_kovance(kolicina):
    kovanci = []
    for _ in range(kolicina):
        x_polozaj = random.randint(30, WIDTH - 50)
        y_polozaj = random.randint(90, HEIGHT - 40)
        kovanci.append(pygame.Rect(x_polozaj, y_polozaj, 20, 20))
    return kovanci


def pripravi_nivo(nivo):
    global coins, enemy, enemy_direction, level, remaining_time

    level = nivo
    remaining_time = TIME_LIMITS[nivo]
    coins = ustvari_kovance(15 if nivo == 1 else 20)
    enemy = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2, 120, 24)
    enemy_direction = 1


def reset_game():
    global player, score, game_state, flash_frames

    player = pygame.Rect(60, HEIGHT - 80, 42, 42)
    score = 0
    flash_frames = 0
    game_state = "start"
    pripravi_nivo(1)


player = pygame.Rect(60, HEIGHT - 80, 42, 42)
coins = []
enemy = pygame.Rect(0, 0, 0, 0)
enemy_direction = 1
score = 0
flash_frames = 0
level = 1
remaining_time = TIME_LIMITS[1]
game_state = "start"
start_ticks = 0

reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                start_ticks = pygame.time.get_ticks()
                game_state = "play"

            elif game_state == "next_level" and event.key == pygame.K_SPACE:
                pripravi_nivo(2)
                start_ticks = pygame.time.get_ticks()
                game_state = "play"

            elif game_state in {"win", "lose"} and event.key == pygame.K_r:
                reset_game()

            elif game_state in {"win", "lose"} and event.key == pygame.K_ESCAPE:
                running = False

    if game_state == "play":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_UP]:
            player.y -= 5
        if keys[pygame.K_DOWN]:
            player.y += 5

        player.clamp_ip(screen.get_rect())

        hitrost_sovraznika = 4 if level == 1 else 7
        enemy.x += hitrost_sovraznika * enemy_direction
        if enemy.left <= 0 or enemy.right >= WIDTH:
            enemy_direction *= -1

        if player.colliderect(enemy):
            game_state = "lose"

        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1
                flash_frames = 6

        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        remaining_time = max(0, TIME_LIMITS[level] - elapsed_seconds)

        if remaining_time == 0 and coins:
            game_state = "lose"

        if not coins and level == 1:
            game_state = "next_level"

        if not coins and level == 2:
            game_state = "win"

    background = FLASH_COLOR if flash_frames > 0 else BG_COLOR
    if flash_frames > 0:
        flash_frames -= 1

    screen.fill(background)

    if game_state != "start":
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
        for coin in coins:
            pygame.draw.circle(screen, COIN_COLOR, coin.center, 10)

        score_text = font.render(f"Točke: {score}", True, TEXT_COLOR)
        level_text = font.render(f"Nivo: {level}", True, TEXT_COLOR)
        time_text = font.render(f"Čas: {remaining_time}", True, TEXT_COLOR)
        screen.blit(score_text, (15, 12))
        screen.blit(level_text, (15, 45))
        screen.blit(time_text, (15, 78))

    if game_state == "start":
        naslov = big_font.render("LOV NA KOVANCE", True, TEXT_COLOR)
        navodilo = font.render("SPACE za začetek", True, TEXT_COLOR)
        opis = font.render(
            "2 nivoja, časovnik, sovražnik in naključni kovanci", True, TEXT_COLOR
        )
        screen.blit(naslov, naslov.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(navodilo, navodilo.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(opis, opis.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    elif game_state == "next_level":
        naslov = big_font.render("NIVO 2", True, TEXT_COLOR)
        navodilo = font.render("SPACE za nadaljevanje", True, TEXT_COLOR)
        opis = font.render(
            "V drugem nivoju je več kovancev in hitrejši sovražnik.", True, TEXT_COLOR
        )
        screen.blit(naslov, naslov.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(navodilo, navodilo.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(opis, opis.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    elif game_state == "win":
        naslov = big_font.render("ZMAGA!", True, TEXT_COLOR)
        navodilo = font.render("R za novo igro ali ESC za izhod", True, TEXT_COLOR)
        opis = font.render(f"Skupne točke: {score}", True, TEXT_COLOR)
        screen.blit(naslov, naslov.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(navodilo, navodilo.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(opis, opis.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    elif game_state == "lose":
        naslov = big_font.render("KONEC IGRE", True, TEXT_COLOR)
        navodilo = font.render("R za nov poskus ali ESC za izhod", True, TEXT_COLOR)
        opis = font.render(
            "Iztekel se je čas ali pa te je ujel sovražnik.", True, TEXT_COLOR
        )
        screen.blit(naslov, naslov.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(navodilo, navodilo.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(opis, opis.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
