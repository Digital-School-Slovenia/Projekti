# Nadgradnja – 30 Projekt Dirkalna igra

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dirkalna igra - nadgradnja s kovanci in gorivom")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

GRASS = (40, 140, 40)
ROAD = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 50, 50)
BLUE = (50, 120, 220)
YELLOW = (240, 220, 70)
GREEN = (40, 220, 90)

ROAD_X = 100
ROAD_WIDTH = 300

player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 7

obstacle_width = 50
obstacle_height = 90
base_obstacle_speed = 6

coin_size = 28
fuel_width = 32
fuel_height = 40

obstacles = []
for i in range(3):
    obstacle = {
        "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width),
        "y": -150 * (i + 1),
        "w": obstacle_width,
        "h": obstacle_height,
    }
    obstacles.append(obstacle)

coin = {
    "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - coin_size),
    "y": -250,
    "size": coin_size,
}

fuel_item = {
    "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - fuel_width),
    "y": -500,
    "w": fuel_width,
    "h": fuel_height,
}

game_state = "start"
score = 0
lives = 3
coins = 0
fuel = 100


def reset_game():
    global player_x, score, obstacles, game_state, lives, coins, fuel, coin, fuel_item

    player_x = WIDTH // 2 - player_width // 2
    score = 0
    lives = 3
    coins = 0
    fuel = 100
    game_state = "play"

    obstacles = []
    for i in range(3):
        obstacle = {
            "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width),
            "y": -150 * (i + 1),
            "w": obstacle_width,
            "h": obstacle_height,
        }
        obstacles.append(obstacle)

    coin = {
        "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - coin_size),
        "y": -250,
        "size": coin_size,
    }

    fuel_item = {
        "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - fuel_width),
        "y": -500,
        "w": fuel_width,
        "h": fuel_height,
    }


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                reset_game()
            if game_state == "game_over" and event.key == pygame.K_r:
                reset_game()

    if game_state == "play":
        fuel -= 0.05
        if fuel <= 0:
            game_state = "game_over"

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        if player_x < ROAD_X:
            player_x = ROAD_X
        if player_x > ROAD_X + ROAD_WIDTH - player_width:
            player_x = ROAD_X + ROAD_WIDTH - player_width

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        current_speed = base_obstacle_speed + score // 10

        for obstacle in obstacles:
            obstacle["y"] += current_speed

            if obstacle["y"] > HEIGHT:
                obstacle["y"] = random.randint(-220, -100)
                obstacle["x"] = random.randint(
                    ROAD_X, ROAD_X + ROAD_WIDTH - obstacle["w"]
                )
                score += 1

            obstacle_rect = pygame.Rect(
                obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]
            )
            if player_rect.colliderect(obstacle_rect):
                lives -= 1
                obstacle["y"] = random.randint(-220, -100)
                obstacle["x"] = random.randint(
                    ROAD_X, ROAD_X + ROAD_WIDTH - obstacle["w"]
                )

                if lives <= 0:
                    game_state = "game_over"

        coin["y"] += current_speed
        fuel_item["y"] += current_speed - 1

        if coin["y"] > HEIGHT:
            coin["y"] = random.randint(-400, -200)
            coin["x"] = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - coin["size"])

        if fuel_item["y"] > HEIGHT:
            fuel_item["y"] = random.randint(-700, -450)
            fuel_item["x"] = random.randint(
                ROAD_X, ROAD_X + ROAD_WIDTH - fuel_item["w"]
            )

        coin_rect = pygame.Rect(coin["x"], coin["y"], coin["size"], coin["size"])
        fuel_rect = pygame.Rect(
            fuel_item["x"], fuel_item["y"], fuel_item["w"], fuel_item["h"]
        )

        if player_rect.colliderect(coin_rect):
            coins += 1
            score += 5
            coin["y"] = random.randint(-400, -200)
            coin["x"] = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - coin["size"])

        if player_rect.colliderect(fuel_rect):
            fuel += 30
            if fuel > 100:
                fuel = 100
            fuel_item["y"] = random.randint(-700, -450)
            fuel_item["x"] = random.randint(
                ROAD_X, ROAD_X + ROAD_WIDTH - fuel_item["w"]
            )

    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    for y in range(0, HEIGHT, 50):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 30))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for obstacle in obstacles:
        pygame.draw.rect(
            screen, RED, (obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"])
        )

    if game_state != "start":
        pygame.draw.ellipse(
            screen, YELLOW, (coin["x"], coin["y"], coin["size"], coin["size"])
        )
        pygame.draw.rect(
            screen,
            GREEN,
            (fuel_item["x"], fuel_item["y"], fuel_item["w"], fuel_item["h"]),
        )

    score_text = font.render(f"Točke: {score}", True, WHITE)
    speed_text = font.render(
        f"Hitrost: {base_obstacle_speed + score // 10}", True, WHITE
    )
    lives_text = font.render(f"Življenja: {lives}", True, WHITE)
    coins_text = font.render(f"Kovanci: {coins}", True, WHITE)
    fuel_text = font.render(f"Gorivo: {int(fuel)}", True, WHITE)

    screen.blit(score_text, (20, 20))
    screen.blit(speed_text, (20, 55))
    screen.blit(lives_text, (20, 90))
    screen.blit(coins_text, (20, 125))
    screen.blit(fuel_text, (20, 160))

    if game_state == "start":
        text1 = big_font.render("DIRKALNA IGRA", True, YELLOW)
        text2 = font.render("SPACE = začetek igre", True, WHITE)
        text3 = font.render("Levo/desno za premik", True, WHITE)
        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 220))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, 310))
        screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, 350))

    if game_state == "game_over":
        text1 = big_font.render("KONEC!", True, YELLOW)
        text2 = font.render("Pritisni R za novo igro", True, WHITE)
        text3 = font.render(f"Točke: {score}", True, WHITE)
        text4 = font.render(f"Kovanci: {coins}", True, WHITE)
        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 220))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, 300))
        screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, 340))
        screen.blit(text4, (WIDTH // 2 - text4.get_width() // 2, 380))

    pygame.display.flip()

pygame.quit()
sys.exit()
