# Rešitve dodatnih nalog – 30 Projekt Dirkalna igra

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 520, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dirkalna igra – dodatne naloge")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 34)
big_font = pygame.font.SysFont(None, 60)

GRASS = (45, 145, 55)
ROAD = (55, 55, 60)
WHITE = (255, 255, 255)
RED = (220, 70, 70)
BLUE = (70, 130, 240)
YELLOW = (250, 225, 80)
GREEN = (60, 220, 110)

ROAD_X = 110
ROAD_WIDTH = 300

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 90
PLAYER_Y = HEIGHT - 120
PLAYER_SPEED = 7

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 90
BASE_SPEED = 6

COIN_SIZE = 28
FUEL_WIDTH = 32
FUEL_HEIGHT = 42


def nakljucna_x_pozicija(sirina_objekta):
    return random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - sirina_objekta)


def ustvari_ovire():
    ovire = []
    for indeks in range(4):
        ovire.append(
            {
                "x": nakljucna_x_pozicija(OBSTACLE_WIDTH),
                "y": -180 * (indeks + 1),
                "w": OBSTACLE_WIDTH,
                "h": OBSTACLE_HEIGHT,
            }
        )
    return ovire


def reset_game():
    global player_x, obstacles, coin, fuel_item, score, lives, collected_coins, fuel, game_state

    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    obstacles = ustvari_ovire()
    coin = {
        "x": nakljucna_x_pozicija(COIN_SIZE),
        "y": -250,
        "size": COIN_SIZE,
    }
    fuel_item = {
        "x": nakljucna_x_pozicija(FUEL_WIDTH),
        "y": -500,
        "w": FUEL_WIDTH,
        "h": FUEL_HEIGHT,
    }
    score = 0
    lives = 3
    collected_coins = 0
    fuel = 100
    game_state = "play"


player_x = WIDTH // 2 - PLAYER_WIDTH // 2
obstacles = []
coin = {"x": 0, "y": 0, "size": COIN_SIZE}
fuel_item = {"x": 0, "y": 0, "w": FUEL_WIDTH, "h": FUEL_HEIGHT}
score = 0
lives = 3
collected_coins = 0
fuel = 100
game_state = "start"

reset_game()
game_state = "start"

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                reset_game()
            elif game_state == "game_over" and event.key == pygame.K_r:
                reset_game()

    if game_state == "play":
        fuel -= 0.04
        if fuel <= 0:
            fuel = 0
            game_state = "game_over"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        if player_x < ROAD_X:
            player_x = ROAD_X
        if player_x > ROAD_X + ROAD_WIDTH - PLAYER_WIDTH:
            player_x = ROAD_X + ROAD_WIDTH - PLAYER_WIDTH

        player_rect = pygame.Rect(player_x, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        current_speed = BASE_SPEED + score // 5

        for obstacle in obstacles:
            obstacle["y"] += current_speed

            if obstacle["y"] > HEIGHT:
                obstacle["y"] = random.randint(-260, -100)
                obstacle["x"] = nakljucna_x_pozicija(obstacle["w"])
                score += 1

            obstacle_rect = pygame.Rect(
                obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]
            )
            if player_rect.colliderect(obstacle_rect):
                lives -= 1
                obstacle["y"] = random.randint(-260, -100)
                obstacle["x"] = nakljucna_x_pozicija(obstacle["w"])
                if lives <= 0:
                    game_state = "game_over"

        coin["y"] += current_speed
        if coin["y"] > HEIGHT:
            coin["y"] = random.randint(-420, -180)
            coin["x"] = nakljucna_x_pozicija(coin["size"])

        fuel_item["y"] += current_speed - 1
        if fuel_item["y"] > HEIGHT:
            fuel_item["y"] = random.randint(-760, -460)
            fuel_item["x"] = nakljucna_x_pozicija(fuel_item["w"])

        coin_rect = pygame.Rect(coin["x"], coin["y"], coin["size"], coin["size"])
        fuel_rect = pygame.Rect(
            fuel_item["x"], fuel_item["y"], fuel_item["w"], fuel_item["h"]
        )

        if player_rect.colliderect(coin_rect):
            collected_coins += 1
            score += 5
            coin["y"] = random.randint(-420, -180)
            coin["x"] = nakljucna_x_pozicija(coin["size"])

        if player_rect.colliderect(fuel_rect):
            fuel = min(100, fuel + 30)
            fuel_item["y"] = random.randint(-760, -460)
            fuel_item["x"] = nakljucna_x_pozicija(fuel_item["w"])

    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    for crta_y in range(0, HEIGHT, 50):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, crta_y, 10, 30))

    pygame.draw.rect(screen, BLUE, (player_x, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

    if game_state != "start":
        for obstacle in obstacles:
            pygame.draw.rect(
                screen,
                RED,
                (obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]),
            )

        pygame.draw.ellipse(
            screen, YELLOW, (coin["x"], coin["y"], coin["size"], coin["size"])
        )
        pygame.draw.rect(
            screen,
            GREEN,
            (fuel_item["x"], fuel_item["y"], fuel_item["w"], fuel_item["h"]),
        )

    score_text = font.render(f"Točke: {score}", True, WHITE)
    speed_text = font.render(f"Hitrost: {BASE_SPEED + score // 5}", True, WHITE)
    lives_text = font.render(f"Življenja: {lives}", True, WHITE)
    coins_text = font.render(f"Kovanci: {collected_coins}", True, WHITE)
    fuel_text = font.render(f"Gorivo: {int(fuel)}", True, WHITE)

    screen.blit(score_text, (18, 18))
    screen.blit(speed_text, (18, 50))
    screen.blit(lives_text, (18, 82))
    screen.blit(coins_text, (18, 114))
    screen.blit(fuel_text, (18, 146))

    if game_state == "start":
        title = big_font.render("DIRKALNA IGRA", True, YELLOW)
        help_text = font.render("SPACE za začetek", True, WHITE)
        info_text = font.render(
            "Ta verzija vključuje življenja, kovance in gorivo.", True, WHITE
        )
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(help_text, help_text.get_rect(center=(WIDTH // 2, 330)))
        screen.blit(info_text, info_text.get_rect(center=(WIDTH // 2, 370)))

    elif game_state == "game_over":
        title = big_font.render("KONEC", True, YELLOW)
        help_text = font.render("Pritisni R za novo igro", True, WHITE)
        result_text = font.render(f"Dosežene točke: {score}", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(help_text, help_text.get_rect(center=(WIDTH // 2, 320)))
        screen.blit(result_text, result_text.get_rect(center=(WIDTH // 2, 360)))

    pygame.display.flip()

pygame.quit()
sys.exit()
