import pygame
import random
import math

pygame.init()


info = pygame.display.Info()

width = info.current_w
height = info.current_h

#width = 1200
#height = 800

gameSpeed = 1

brickSizeX, brickSizeY = 30, 120


screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


score = 0

pygame.display.set_caption("pingalo pongalo")

bela = (255, 255, 255)
crna = (0, 0, 0)

zelena = (0, 255, 0)
zlata = (255, 214, 79)
modra = (0, 0, 255)
vijola = (170, 0, 170)
rumena = (255, 255, 0)

lopar_width, lopar_height = 16, 112
ball_size = 15

left_paddle = pygame.Rect(20, height//2 - lopar_height//2, lopar_width, lopar_height)
right_paddle = pygame.Rect(width - 30, height//2 - lopar_height//2, lopar_width, lopar_height)

#img
leftPaddleTop = pygame.image.load("PingiPongi/leftPaddleTop.png").convert()
leftPaddleBottom = pygame.image.load("PingiPongi/leftPaddleBottom.png").convert()
leftPaddleMiddle = pygame.image.load("PingiPongi/leftPaddleMiddle.png").convert()

rightPaddleTop = pygame.image.load("PingiPongi/rightPaddleTop.png").convert()
rightPaddleBottom = pygame.image.load("PingiPongi/rightPaddleBottom.png").convert()
rightPaddleMiddle = pygame.image.load("PingiPongi/rightPaddleMiddle.png").convert()

background = pygame.image.load("PingiPongi/background.png")
background = pygame.transform.scale(background, (width, height))


#pygame.mixer.music.load("PingiPongi/sfx/sfx/bg.mp3")
#pygame.mixer.music.play(-1)

brickBreakSound = pygame.mixer.Sound("sfx/sfx/brickBreak.mp3")
paddleBounceSound = pygame.mixer.Sound("sfx/sfx/paddleBounce.mp3")

#start = pygame.mixer.Sound("PingiPongi/sfx/sfx/start.mp3")
#pygame.mixer.Sound.play(start)


bigPaddleImage = pygame.image.load("bricki/bricki/Big paddle.png").convert()
bigPaddleImage = pygame.transform.scale(bigPaddleImage, (brickSizeX, brickSizeY))

duplicateBallsImage = pygame.image.load("bricki/bricki/Duplicate balls.png").convert()
duplicateBallsImage = pygame.transform.scale(duplicateBallsImage, (brickSizeX, brickSizeY))

fasterPaddle = pygame.image.load("bricki/bricki/Faster paddle.png").convert()
fasterPaddle = pygame.transform.scale(fasterPaddle, (brickSizeX, brickSizeY))

speed = pygame.image.load("bricki/bricki/Speed.png").convert()
speed = pygame.transform.scale(speed, (brickSizeX, brickSizeY))

superSpeed = pygame.image.load("bricki/bricki/Super speed.png").convert()
superSpeed = pygame.transform.scale(superSpeed, (brickSizeX, brickSizeY))



font = pygame.font.Font("freesansbold.ttf", 32)

ballImg = pygame.image.load("PingiPongi/ball.png").convert()

basePaddleSpeed = 10
baseBallSpeed = 9

paddle_speed = basePaddleSpeed

collisionForBrick = 2
collisionCount = 0

bricks = []

balls = [[pygame.Rect(20, 20, 10, 10), [baseBallSpeed, baseBallSpeed], 0]]

brickTypes = [
    ["Speed", zelena, speed],
    ["Super speed", zlata, superSpeed],
    ["Faster paddle", modra, fasterPaddle],
    ["Big paddle", rumena, bigPaddleImage],
    ["Duplicate balls", vijola, duplicateBallsImage]
]

#-----------FUNCTION-ZA-POWER-UPS-----------
def speedUp(speed):
    for i in balls:

        newBallSpeed = 0
        if i[1][0] > 0:
            newBallSpeed = i[1][0] + speed
        else:
            newBallSpeed = i[1][0] - speed

        i[1][0] = newBallSpeed

def paddleSpeedUp(speed):
    global paddle_speed

    paddle_speed += speed

def dupeBalls():
    global balls
    newBalls = balls.copy()
    
    for i in balls:
        newBalls.append([i[0].copy(), [i[1][0] *-1, i[1][1] *-1], 30])
    
    balls = newBalls

def big_paddle(size):
    left_paddle.height += size
    right_paddle.height += size

#----------NEW BRICK FUNCTION----------
offCenterPosition = 100

def newBrick():
    #brick type
    Type = brickTypes[random.randint(1, len(brickTypes)) - 1]

    #brick size
    x_size = brickSizeX
    y_size = brickSizeY

    #brick position
    x_pos = random.randint(width//2 - offCenterPosition, width//2 + offCenterPosition)
    y_pos = random.randint(10, height - y_size - 10)

    #adding to bricks seznam [type(string), rect, barva]
    brick = pygame.Rect(x_pos, y_pos, x_size, y_size)

    found = False
    for i in bricks:
        if i[1].colliderect(brick):
            found = True
    
    if found:
        newBrick()
    else:
        bricks.append([Type[0], brick, Type[1]])

#mode

mode = 0

while mode == 0:

    screen.fill((0,0,0))

    font = pygame.font.Font(None, 60)

    text1 = font.render("1 = Singleplayer", True, (255,255,255))
    text2 = font.render("2 = Multiplayer", True, (255,255,255))

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 110))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                mode = 1

            elif event.key == pygame.K_2:
                mode = 2




running = True
while running:
    pygame.time.delay(gameSpeed)

    #check if app running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    
    if mode == 2:
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < height:
            right_paddle.y += paddle_speed
    
    elif mode == 1:

        closestBall = None
        closestDistance = math.inf

        for ball in balls:

            #moving towards the ai
            if ball[1][0] > 0:

                distance = right_paddle.x - ball[0].x


                if distance < closestDistance:
                    closestDistance = distance
                    closestBall = ball

        if closestBall is not None:

            paddleCenter = right_paddle.centery


            ballCenter = closestBall[0].centery

            difference = ballCenter - paddleCenter

            deadzone = right_paddle.height/4

            if abs(difference) > deadzone:

                if difference > 0:
                    if right_paddle.bottom < height:
                        right_paddle.y += paddle_speed

                else:
                    if right_paddle.top > 0:
                        right_paddle.y -= paddle_speed
    
    #making the ball move based on speed
    for i in balls:
        x_speed = i[1][0]
        y_speed = i[1][1]

        i[0].left += x_speed
        i[0].top += y_speed

        score = score + math.sqrt(pow(x_speed, 2) + pow(y_speed, 2))

    #hitting bottom/top
    for i in balls:
        if i[0].top < 0 or i[0].top > height:
            i[1][1] *= -1
    
    #paddleCol
    for i in balls:
        if i[2] > 0:
            i[2] -= 1

    #colliding with paddles
    for i in balls:
        if i[0].colliderect(left_paddle) and i[2] <= 0:
            distance = (left_paddle.top + left_paddle.height/2) - (i[0].top + i[0].height/2)
        
            distancePartly = distance/left_paddle.height

            y_speed = abs(i[1][0]) * -distancePartly
            i[1][1] = y_speed

            i[1][0] *= -1

            collisionCount += 1
            if collisionCount == collisionForBrick:
                collisionCount = 0
                newBrick()
            
            pygame.mixer.Sound.play(paddleBounceSound)

            i[2] = 30
        elif i[0].colliderect(right_paddle) and i[2] <= 0:
            distance = (right_paddle.top + right_paddle.height/2) - (i[0].top - i[0].height/2)

            distancePartly = distance/right_paddle.height

            y_speed = abs(i[1][0]) * -distancePartly
            i[1][1] = y_speed

            i[1][0] *= -1

            collisionCount += 1
            if collisionCount == collisionForBrick:
                collisionCount = 0
                newBrick()
            
            pygame.mixer.Sound.play(paddleBounceSound)

            i[2] = 30

    
    #reseting the game
    for ball in balls:
        if ball[0].left <= 0 or ball[0].right >= width:
            balls.remove(ball)

            if len(balls) <= 0:
                balls = [[pygame.Rect(20, 20, 10, 10), [baseBallSpeed, baseBallSpeed], 0]]
                bricks = []
                left_paddle = pygame.Rect(20, height//2 - lopar_height//2, lopar_width, lopar_height)
                right_paddle = pygame.Rect(width - 30, height//2 - lopar_height//2, lopar_width, lopar_height)
                score = 0
    
   # brick collisions
    toDelete = []
    duplicateQueued = False

    for brick in bricks[:]:
        for ball in balls[:]:

            if ball[0].colliderect(brick[1]):

                pygame.mixer.Sound.play(brickBreakSound)

                if brick[0] == "Speed":
                    speedUp(0.4)

                elif brick[0] == "Super speed":
                    speedUp(0.8)

                elif brick[0] == "Faster paddle":
                    paddleSpeedUp(0.2)

                elif brick[0] == "Big paddle":
                    big_paddle(16)

                elif brick[0] == "Duplicate balls":
                    duplicateQueued = True

                # bounce
                ball[1][0] *= -1

                if brick not in toDelete:
                    toDelete.append(brick)

    # remove bricks
    for brick in toDelete:
        if brick in bricks:
            bricks.remove(brick)

    if duplicateQueued:
        dupeBalls()
    
    screen.fill(crna)
    screen.blit(background, (0, 0))

    #---------------DRAWING-SHAPES-BOTTOM-FROM-HERE---------------#

    #paddles
    pygame.draw.rect(screen, bela, left_paddle)
    pygame.draw.rect(screen, bela, right_paddle)

    for i in range(int(left_paddle.height/16)):
        screen.blit(leftPaddleMiddle, (left_paddle.left, left_paddle.top + i*16))
    
    screen.blit(leftPaddleTop, left_paddle.topleft)
    screen.blit(leftPaddleBottom, (left_paddle.left, left_paddle.top + left_paddle.height - 16))

    for i in range(int(right_paddle.height/16)):
        screen.blit(rightPaddleMiddle, (right_paddle.left, right_paddle.top + i*16))
    
    screen.blit(rightPaddleTop, right_paddle.topleft)
    screen.blit(rightPaddleBottom, (right_paddle.left, right_paddle.top + right_paddle.height - 16))

    #ball
    for i in balls:
        #pygame.draw.circle(screen, bela, i[0].topleft, i[0].width/2)
        screen.blit(ballImg, i[0].topleft)

    #lines in middle
    for i in range(10, height, 30):
        pygame.draw.rect(screen, bela, (width//2 - 1, i, 2, 15))

    #drawing bricks
    for i in bricks:
        pygame.draw.rect(screen, i[2], i[1])

        for x in brickTypes:
            if x[0] == i[0]:
                screen.blit(x[2], i[1].topleft)

    #score
    scoreRender = font.render(str(int(score/10)), True, bela, crna)
    textRect = scoreRender.get_rect()
    screen.blit(scoreRender, (width/2 - textRect.width/2, height - 40))


    pygame.display.update() 
