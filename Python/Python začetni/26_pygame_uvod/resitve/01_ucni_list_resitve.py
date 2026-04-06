"""Rešitve učnega lista – 26 – Pygame – uvod, okno, risanje in premikanje."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja prva igra")
clock = pygame.time.Clock()

running = True
while running:
    # Najprej vedno obdelaš dogodke, da se okno pravilno odziva.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ozadje pobriše prejšnji frame in pripravi prostor za novo risanje.
    screen.fill((30, 30, 50))

    # Tukaj bi kasneje dodal risanje igralca, predmetov ali besedila.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
