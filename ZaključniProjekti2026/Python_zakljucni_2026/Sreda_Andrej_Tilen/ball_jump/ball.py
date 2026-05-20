import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twin Towers")
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)

clock = pygame.time.Clock()

player_img = pygame.image.load("slike/player.svg").convert_alpha()
tower_img = pygame.image.load("slike/tower.svg").convert_alpha()
background_img1 = pygame.image.load("slike/day.webp").convert()
background_img2 = pygame.image.load("slike/mid.jpg").convert()
background_img2 = pygame.transform.scale(background_img2, (WIDTH, HEIGHT))
background_img3 = pygame.image.load("slike/night.jpg").convert()
background_img3 = pygame.transform.scale(background_img3, (WIDTH, HEIGHT))

player_img = pygame.transform.scale(player_img, (50, 30))
background_img1 = pygame.transform.scale(background_img1, (WIDTH, HEIGHT))

plane = player_img.get_rect(topleft=(100, 250))
velocity = 0
gravity = 0.5
jump = -10
tocke = 0
time_of_day = 0

score = 0
score_font = pygame.font.Font(None, 40)


tower_width = 80
gap = 200

towers = []
for i in range(3):
    x = 600 + i * 300
    height_top = random.randint(50, 300)
    towers.append([x, height_top])

running = True
while running:
    
    clock.tick(60)
    time_of_day = ( tocke // 3 ) % 3

    if time_of_day == 0:
        background_img = background_img1
    if time_of_day == 1:
        background_img = background_img2
    elif time_of_day == 2:
        background_img = background_img3
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = jump

    velocity += gravity
    plane.y += int(velocity)

    if plane.top < 0:
        plane.top = 0
        velocity = 0
    if plane.bottom > HEIGHT:
        plane.bottom = HEIGHT
        running = False

    for t in towers:
        t[0] -= 5
        if t[0] < -tower_width:
            t[0] = WIDTH + random.randint(0, 200)
            t[1] = random.randint(50, 300)
            tocke += 1

        top_rect = pygame.Rect(t[0], 0, tower_width, t[1])
        bottom_rect = pygame.Rect(t[0], t[1] + gap, tower_width, HEIGHT - (t[1] + gap))

        scaled_top = pygame.transform.scale(tower_img, (top_rect.width, top_rect.height))
        flipped_top = pygame.transform.flip(scaled_top, False, True)
        screen.blit(flipped_top, top_rect)

        scaled_bottom = pygame.transform.scale(tower_img, (bottom_rect.width, bottom_rect.height))
        screen.blit(scaled_bottom, bottom_rect)
        prikaz_tock = my_font.render(str(tocke), False, (0, 0, 0))
        screen.blit(prikaz_tock, (0,0))

        if plane.colliderect(top_rect) or plane.colliderect(bottom_rect):
            running = False

    screen.blit(player_img, plane)
    pygame.display.update()

pygame.quit()
