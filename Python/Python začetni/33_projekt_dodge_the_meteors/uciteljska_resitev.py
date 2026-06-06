# Učiteljska referenčna rešitev – 33 Projekt Dodge the Meteors
# Namen: pokaže osnovno arkadno igro z izmikanjem, točkami in ponovnim zagonom.

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Meteors")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

player_speed = 7


def reset_game():
    global player, meteors, score, game_over
    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)
    meteors = []
    score = 0
    game_over = False


def spawn_meteor():
    size = random.randint(20, 55)
    x_position = random.randint(0, WIDTH - size)
    return pygame.Rect(x_position, -size, size, size)


reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_r:
            reset_game()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        player.x = max(0, min(WIDTH - player.width, player.x))

        if random.randint(1, 18) == 1:
            meteors.append(spawn_meteor())

        for meteor in meteors[:]:
            meteor.y += 5
            if meteor.top > HEIGHT:
                meteors.remove(meteor)
                score += 1
            elif meteor.colliderect(player):
                game_over = True

    screen.fill((20, 20, 35))
    pygame.draw.rect(screen, (80, 180, 255), player)
    for meteor in meteors:
        pygame.draw.ellipse(screen, (180, 100, 70), meteor)

    score_text = font.render(f"Rezultat: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        over = big_font.render("KONEC IGRE", True, (255, 220, 100))
        info = font.render("Pritisni R za novo igro", True, (255, 255, 255))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()
    clock.tick(60)
