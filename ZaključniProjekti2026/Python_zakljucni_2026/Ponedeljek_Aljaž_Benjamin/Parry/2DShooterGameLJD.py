import pygame

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Parry Demo")
clock = pygame.time.Clock()

# Colors
BLUE = (50,50,200)
LIGHTBLUE = (100,200,255)
WHITE = (255,255,255)

# Player
player_pos = [WIDTH//2, HEIGHT//2]
player_radius = 20
player_speed = 5

# Parry
parry_active = False
parry_timer = 0
PARRY_DURATION = 60  # 1 second at 60 FPS

running = True
while running:
    screen.fill((0, 0, 0))
    #background = pygame.image.load('desertBackground.jpg')
    #screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Press C to parry
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if not parry_active:
                    parry_active = True
                    parry_timer = PARRY_DURATION

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: player_pos[0] -= player_speed
    if keys[pygame.K_d]: player_pos[0] += player_speed
    if keys[pygame.K_w]: player_pos[1] -= player_speed
    if keys[pygame.K_s]: player_pos[1] += player_speed

    # Parry timer
    if parry_active:
        parry_timer -= 1
        if parry_timer <= 0:
            parry_active = False

    # Draw player
    pygame.draw.circle(screen, BLUE, player_pos, player_radius)
    # Draw parry visual
    if parry_active:
        pygame.draw.circle(screen, LIGHTBLUE, player_pos, player_radius+8, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
