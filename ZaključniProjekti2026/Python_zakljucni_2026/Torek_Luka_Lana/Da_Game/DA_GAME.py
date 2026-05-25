import pygame
import random

def dino():
    # Initialize pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 800, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Easy Dino Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (50, 200, 50)
    RED = (200, 50, 50)

    # Clock
    clock = pygame.time.Clock()
    FPS = 60

    # Dino settings
    dino_x = 80
    dino_y = 300
    dino_width = 40
    dino_height = 40

    velocity_y = 0
    gravity = 1
    jump_power = -18
    is_jumping = False

    # Ground
    ground_y = 340

    # Obstacle settings
    obstacle_width = 30
    obstacle_height = 50
    obstacle_x = WIDTH
    obstacle_speed = 8

    # Score
    score = 0
    font = pygame.font.SysFont(None, 36)

    # Game loop
    running = True

    while running:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    velocity_y = jump_power
                    is_jumping = True

        # Dino physics
        dino_y += velocity_y
        velocity_y += gravity

        # Stop at ground
        if dino_y >= ground_y - dino_height:
            dino_y = ground_y - dino_height
            velocity_y = 0
            is_jumping = False

        # Move obstacle
        obstacle_x -= obstacle_speed

        # Reset obstacle
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH + random.randint(0, 200)
            score += 1

        # Rectangles for collision
        dino_rect = pygame.Rect(
            dino_x,
            dino_y,
            dino_width,
            dino_height
        )

        obstacle_rect = pygame.Rect(
            obstacle_x,
            ground_y - obstacle_height,
            obstacle_width,
            obstacle_height
        )

        # Collision detection
        if dino_rect.colliderect(obstacle_rect):
            print("Game Over!")
            running = False

        # Draw everything
        screen.fill(WHITE)

        # Ground
        pygame.draw.line(
            screen,
            BLACK,
            (0, ground_y),
            (WIDTH, ground_y),
            3
        )

        # Dino
        pygame.draw.rect(screen, GREEN, dino_rect)

        # Obstacle
        pygame.draw.rect(screen, RED, obstacle_rect)

        # Score
        score_text = font.render(
            f"Score: {score}",
            True,
            BLACK
        )

        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

def jumper():
    #set up pygame
    pygame.init()
    WIDTH = 400
    HEIGHT = 600

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("JDCT")

    clock = pygame.time.Clock()
    #barve
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    BLUE = (50,100,255)
    RED = (200,0,0)




    platforms = []
    rect = pygame.Rect(120, 200, 80, 15)
    platforms.append(rect)
    for i in range(6):
        x = random.randint(0, WIDTH - 80)
        y = HEIGHT - i * 100
        rect = pygame.Rect(x, y, 80, 15)
        platforms.append(rect)
        
        
    #player
    player_width = 40
    player_height = 40
    player_x = WIDTH// 2 - player_width // 2
    player_y = 200

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    #player stats
    player_vel_y = -12
    GRAVITY = 0.8
    JUMP_STRENGHT = -15
    MOVE_SPEED = 7
    if player_width > 40:
        GRAVITY = 2.0






    #main game loop
    running = True
    while running:
        clock.tick(60)
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= MOVE_SPEED
            keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_rect.x += MOVE_SPEED            
                
        if player_rect.right < 0:
            player_left = WIDTH
        elif player_rect.left > WIDTH:
            player_rect.right = 0
            
        player_vel_y += GRAVITY
        player_rect.y += player_vel_y
        
        #Collision detection
        if player_vel_y > 0:
            for platform in platforms:
                if player_rect.colliderect(platform):
                    if player_rect.bottom <= platform.top +15:
                        player_rect.bottom = platform.top
                        player_vel_y = JUMP_STRENGHT
        if player_rect.top <= HEIGHT //3:
            scroll = (HEIGHT// 3) - player_rect.top
            player_rect.top = HEIGHT // 3
            
            for platform in platforms:
                platform.y += scroll
                
            #move invisible platforms
            for platform in platforms:
                if platform.top > HEIGHT:
                    platform.x = random.randint(0,WIDTH - platform.width)
                    platform.y = -20
        #game over
        if player_rect.top > HEIGHT:
            running = False
        # Narisemo Igro
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, player_rect)
        for platform in platforms:
            pygame.draw.rect(screen, GREEN, platform)
        pygame.display.flip()
            

    pygame.quit()

while True:
    a = input("Vnesi jumper ali dino  ")
    if a == "dino":
        dino()
        break
    if a == "jumper":
        jumper()
        break