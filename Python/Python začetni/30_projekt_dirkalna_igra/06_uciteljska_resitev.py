# Učiteljska referenčna rešitev – 30 Projekt Dirkalna igra
# Glavna rešitev je srednja, še vedno dosegljiva različica.

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dirkalna igra - LEVEL 2")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

GRASS = (40, 140, 40)
ROAD = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 50, 50)
BLUE = (50, 120, 220)
YELLOW = (240, 220, 70)

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

obstacles = []
for i in range(3):
    obstacle = {
        "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width),
        "y": -150 * (i + 1),
        "w": obstacle_width,
        "h": obstacle_height,
    }
    obstacles.append(obstacle)

game_over = False
score = 0


def reset_game():
    global player_x, game_over, score, obstacles

    player_x = WIDTH // 2 - player_width // 2
    game_over = False
    score = 0

    obstacles = []
    for i in range(3):
        obstacle = {
            "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle_width),
            "y": -150 * (i + 1),
            "w": obstacle_width,
            "h": obstacle_height,
        }
        obstacles.append(obstacle)


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                reset_game()

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

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        current_speed = base_obstacle_speed + score // 10

        for obstacle in obstacles:
            obstacle["y"] += current_speed

            if obstacle["y"] > HEIGHT:
                obstacle["y"] = random.randint(-220, -100)
                obstacle["x"] = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - obstacle["w"])
                score += 1

            obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"])
            if player_rect.colliderect(obstacle_rect):
                game_over = True

    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    for y in range(0, HEIGHT, 50):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 30))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]))

    score_text = font.render(f"Tocke: {score}", True, WHITE)
    speed_text = font.render(f"Hitrost: {base_obstacle_speed + score // 10}", True, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(speed_text, (20, 55))

    if game_over:
        text1 = big_font.render("KONEC!", True, YELLOW)
        text2 = font.render("Pritisni R za ponovni zagon.", True, WHITE)
        text3 = font.render(f"Koncne tocke: {score}", True, WHITE)
        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 240))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, 320))
        screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, 360))

    pygame.display.flip()

pygame.quit()
sys.exit()
