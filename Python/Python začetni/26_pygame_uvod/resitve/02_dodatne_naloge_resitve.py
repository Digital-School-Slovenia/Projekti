# Učiteljska referenčna rešitev – 26 Pygame premik kvadrata
# Namen: pokaže premikanje igralca, omejitev na zaslon in osnovni game loop.

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame – premik kvadrata")
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)
player_speed = 5
world_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Igralec ostane znotraj okna, tudi če držiš tipko predolgo.
    player.clamp_ip(world_rect)

    screen.fill((30, 30, 50))
    pygame.draw.rect(screen, (220, 80, 80), player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
