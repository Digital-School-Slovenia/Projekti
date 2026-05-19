# Predloga – 35 Zaključni projekt
# Namen: čista osnova, ki jo učenec predela v svojo igro ali program.

import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zaključni projekt")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(120, 120, 50, 50)
player_speed = 5
world_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
score = 0
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

    # Igralec ostane v vidnem delu zaslona, tudi ko učenec hitro nadgrajuje kodo.
    player.clamp_ip(world_rect)

    screen.fill((30, 30, 50))
    pygame.draw.rect(screen, (80, 170, 255), player)

    # Tukaj postopno dodaj svoje objekte, trke, pravila in sistem točkovanja.
    hud = font.render(f"Točke: {score}", True, (255, 255, 255))
    screen.blit(hud, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
