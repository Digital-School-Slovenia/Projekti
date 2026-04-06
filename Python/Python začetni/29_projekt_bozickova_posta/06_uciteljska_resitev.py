# Učiteljska referenčna rešitev – 29 Projekt Božičkova pošta

import pygame
from random import randint

SIRINA_ZASLONA = 800
VISINA_ZASLONA = 500

def main():
    pygame.init()
    pygame.display.set_caption("IME IGRE")
    
    # Nastavitve zaslona, ure in pisave
    ZASLON = pygame.display.set_mode((SIRINA_ZASLONA, VISINA_ZASLONA))
    URA = pygame.time.Clock()
    PISAVA = pygame.font.SysFont(None, 32)
    # Položaj in dimenzije lika
    santa_x = SIRINA_ZASLONA // 2
    santa_y = VISINA_ZASLONA - 60
    santa_w = 50 # Sirina lika
    santa_h = 40 # Visina lika
    # Seznam za padanje predmetov
    emails = []
    stevilo_tock = 0
    stevilo_zivljenj = 3
    # Določitev začetka igre
    nadaljuj_igro = True
    while nadaljuj_igro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nadaljuj_igro = False
        # Premikanje lika
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            santa_x -= 6
        if keys[pygame.K_RIGHT]:
            santa_x += 6
        # Omejitev gibanja lika znotraj zaslona
        santa_x = max(0, min(SIRINA_ZASLONA - santa_w, santa_x))
        # Dodajanje novih predmetov
        if randint(1, 25) == 1: 
            email = {
                "x": randint(0, 770), # naključna x pozicija
                "y": -30, # začetna y pozicija (vedno nad zaslonom)
                "speed": randint(3, 6), # hitrost padanja
                "type": "spam" if randint(1, 4) == 1 else "good" # 25% možnost za spam
            }
            emails.append(email)
        # Ozadje in risanje lika ter predmetov
        ZASLON.fill((100, 100, 100))
        # Risanje lika
        santa_rect = pygame.Rect(santa_x, santa_y, santa_w, santa_h)
        pygame.draw.rect(ZASLON, (220, 40, 40), santa_rect)
        # Posodabljanje in risanje predmetov
        for email in emails[:]:
            # Posodobi pozicijo y (pade navzdol)
            email["y"] += email["speed"]
            # Ustvari pravokotnik za predmet
            rect = pygame.Rect(email["x"], email["y"], 20, 20)
            # Preverimo ali se je predmet dotaknil bozicnega lika.
            if rect.colliderect(santa_rect):
                if email["type"] == "good":
                    stevilo_tock += 1
                else:
                    stevilo_zivljenj -= 1
                emails.remove(email)
                continue
            # Določimo barvo glede na tip predmeta
            color = (0, 200, 100) if email["type"] == "good" else (255, 120, 0)
            pygame.draw.rect(ZASLON, color, rect)
        text = PISAVA.render(f"Točke: {stevilo_tock}   Življenj: {stevilo_zivljenj}", True, (255, 255, 255))
        ZASLON.blit(text, (10, 10))
        # Preverimo ce nimamo vec zivljenj
        if stevilo_zivljenj <= 0:
            nadaljuj_igro = False
        pygame.display.flip()
        URA.tick(60)

    pygame.quit()

main()
