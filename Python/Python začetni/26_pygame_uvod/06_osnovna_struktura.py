# Učiteljska referenčna rešitev – 26 Pygame uvod

import pygame
import sys

# Inicializicija pygame
pygame.init()


# Ustvarjanje okna
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Moja prva igra")




# Preverjanje dogodkov.
while True:
    for event in pygame.event.get():
        # Preverjamo ce je bil pritisnjen X.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    pygame.display.update()