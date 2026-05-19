# Predloga – 34 Delavnica iger in priprava na zaključek
# Uporabi jo samo kot osnovo za prvi prototip.

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moj projekt")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(100, 100, 50, 50)
speed = 5
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    screen.fill((25, 25, 40))
    pygame.draw.rect(screen, (220, 70, 70), player)

    score_text = font.render(f"Točke: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
