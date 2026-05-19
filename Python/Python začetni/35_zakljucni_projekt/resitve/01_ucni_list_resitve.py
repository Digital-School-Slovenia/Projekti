"""Rešitve učnega lista – 35 – Zaključni projekt."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

import random
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zaključni projekt - vzorčni prototip")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 58)

player = pygame.Rect(120, 120, 50, 50)
enemy = pygame.Rect(620, 260, 60, 60)
star = pygame.Rect(420, 180, 26, 26)
world_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

player_speed = 5
enemy_speed = 4
enemy_direction = 1
score = 0
lives = 3
game_over = False
running = True


def reset_game():
    global player, enemy, star, enemy_direction, score, lives, game_over
    player = pygame.Rect(120, 120, 50, 50)
    enemy = pygame.Rect(620, 260, 60, 60)
    star = pygame.Rect(420, 180, 26, 26)
    enemy_direction = 1
    score = 0
    lives = 3
    game_over = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            reset_game()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        player.clamp_ip(world_rect)

        enemy.x += enemy_speed * enemy_direction
        if enemy.left <= 120 or enemy.right >= WIDTH - 120:
            enemy_direction *= -1

        if player.colliderect(star):
            score += 1
            star.x = random.randint(80, WIDTH - 80)
            star.y = random.randint(80, HEIGHT - 80)

        if player.colliderect(enemy):
            lives -= 1
            player.topleft = (120, 120)
            if lives <= 0:
                game_over = True

    screen.fill((30, 30, 50))
    pygame.draw.rect(screen, (80, 170, 255), player)
    pygame.draw.rect(screen, (220, 90, 90), enemy)
    pygame.draw.circle(screen, (255, 220, 80), star.center, 13)

    hud = font.render(f"Točke: {score}   Življenja: {lives}", True, (255, 255, 255))
    screen.blit(hud, (10, 10))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        screen.blit(overlay, (0, 0))
        title = big_font.render("KONEC IGRE", True, (255, 255, 255))
        info = font.render("Pritisni R za nov poskus.", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
