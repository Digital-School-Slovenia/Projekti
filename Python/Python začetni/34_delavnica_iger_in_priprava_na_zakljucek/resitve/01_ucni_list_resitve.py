"""Rešitve učnega lista – 34 – Delavnica iger in priprava na zaključek."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prototip projekta")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 52)

player = pygame.Rect(100, 100, 50, 50)
zvezda = pygame.Rect(560, 180, 24, 24)
speed = 5
score = 0
zvezda_pobrana = False
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

    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    if not zvezda_pobrana and player.colliderect(zvezda):
        zvezda_pobrana = True
        score = 1

    screen.fill((25, 25, 40))
    pygame.draw.rect(screen, (220, 70, 70), player)

    if not zvezda_pobrana:
        pygame.draw.circle(screen, (255, 220, 80), zvezda.center, 12)

    score_text = font.render(f"Točke: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if zvezda_pobrana:
        msg = big_font.render("Prototip deluje", True, (255, 255, 255))
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
