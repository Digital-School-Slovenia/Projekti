# Rešitve domače naloge – 30 Projekt Dirkalna igra

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 520, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neonska cesta")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 34)
big_font = pygame.font.SysFont(None, 58)

GRASS = (30, 110, 50)
ROAD = (35, 35, 45)
WHITE = (255, 255, 255)
NEON_BLUE = (90, 220, 255)
NEON_PINK = (255, 90, 170)
YELLOW = (250, 220, 80)

ROAD_X = 110
ROAD_WIDTH = 300
PLAYER_WIDTH = 52
PLAYER_HEIGHT = 92
PLAYER_Y = HEIGHT - 125
PLAYER_SPEED = 7


def draw_car(x_polozaj, y_polozaj):
    pygame.draw.rect(
        screen,
        NEON_BLUE,
        (x_polozaj, y_polozaj, PLAYER_WIDTH, PLAYER_HEIGHT),
        border_radius=10,
    )
    pygame.draw.rect(
        screen, WHITE, (x_polozaj + 10, y_polozaj + 15, 32, 20), border_radius=6
    )
    pygame.draw.rect(
        screen, WHITE, (x_polozaj + 10, y_polozaj + 50, 32, 20), border_radius=6
    )
    pygame.draw.rect(
        screen, ROAD, (x_polozaj - 4, y_polozaj + 10, 6, 18), border_radius=3
    )
    pygame.draw.rect(
        screen,
        ROAD,
        (x_polozaj + PLAYER_WIDTH - 2, y_polozaj + 10, 6, 18),
        border_radius=3,
    )
    pygame.draw.rect(
        screen, ROAD, (x_polozaj - 4, y_polozaj + 64, 6, 18), border_radius=3
    )
    pygame.draw.rect(
        screen,
        ROAD,
        (x_polozaj + PLAYER_WIDTH - 2, y_polozaj + 64, 6, 18),
        border_radius=3,
    )


def ustvari_ovire():
    ovire = []
    for indeks in range(2):
        ovire.append(
            {
                "x": random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - 52),
                "y": -220 * (indeks + 1),
                "w": 52,
                "h": 92,
            }
        )
    return ovire


def reset_game():
    global player_x, obstacles, score, lives, game_over

    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    obstacles = ustvari_ovire()
    score = 0
    lives = 3
    game_over = False


player_x = WIDTH // 2 - PLAYER_WIDTH // 2
obstacles = []
score = 0
lives = 3
game_over = False

reset_game()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_r:
            reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()

        # Premikanje avtomobila
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        if player_x < ROAD_X:
            player_x = ROAD_X
        if player_x > ROAD_X + ROAD_WIDTH - PLAYER_WIDTH:
            player_x = ROAD_X + ROAD_WIDTH - PLAYER_WIDTH

        player_rect = pygame.Rect(player_x, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Nova mehanika: življenja
        for obstacle in obstacles:
            obstacle["y"] += 6 + score // 8

            if obstacle["y"] > HEIGHT:
                obstacle["y"] = random.randint(-260, -100)
                obstacle["x"] = random.randint(
                    ROAD_X, ROAD_X + ROAD_WIDTH - obstacle["w"]
                )
                score += 1

            obstacle_rect = pygame.Rect(
                obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]
            )

            # Trk z ovirami
            if player_rect.colliderect(obstacle_rect):
                lives -= 1
                obstacle["y"] = random.randint(-260, -100)
                obstacle["x"] = random.randint(
                    ROAD_X, ROAD_X + ROAD_WIDTH - obstacle["w"]
                )

                if lives <= 0:
                    game_over = True

    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    for crta_y in range(0, HEIGHT, 55):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, crta_y, 10, 32))

    draw_car(player_x, PLAYER_Y)

    for obstacle in obstacles:
        pygame.draw.rect(
            screen,
            NEON_PINK,
            (obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"]),
            border_radius=10,
        )

    score_text = font.render(f"Točke: {score}", True, WHITE)
    lives_text = font.render(f"Življenja: {lives}", True, WHITE)
    screen.blit(score_text, (18, 18))
    screen.blit(lives_text, (18, 52))

    if game_over:
        title = big_font.render("KONEC", True, YELLOW)
        help_text = font.render("Pritisni R za novo vožnjo", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 280)))
        screen.blit(help_text, help_text.get_rect(center=(WIDTH // 2, 340)))

    pygame.display.flip()

pygame.quit()
sys.exit()
