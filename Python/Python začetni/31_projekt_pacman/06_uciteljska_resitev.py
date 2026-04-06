# Referenčna rešitev – 31 Projekt Pac-Man

# Namen: demonstracijska rešitev za postopno gradnjo projekta in razlago glavnih mehanik igre.

import pygame
import sys
import random

# Zagon Pygame
pygame.init()

# Velikost enega polja v mreži
CELL_SIZE = 40

# Zemljevid igre
maze = [
    list("###################"),
    list("#P...#............#"),
    list("#.##.#.#..........#"),
    list("#....#...#####....#"),
    list("#.####.#E.####....#"),
    list("#.........####....#"),
    list("###################"),
]

ROWS = len(maze)
COLS = len(maze[0])

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirint in zbiranje točk")
clock = pygame.time.Clock()

# Barve
BLACK = (0, 0, 0)
BLUE = (40, 40, 200)
YELLOW = (255, 220, 0)
WHITE = (240, 240, 240)
DARK = (30, 30, 30)
RED = (200, 50, 50)

font = pygame.font.SysFont(None, 32)

# Začetni položaji
player_row = 0
player_col = 0
enemy_row = 0
enemy_col = 0

for row in range(ROWS):
    for col in range(COLS):
        if maze[row][col] == "P":
            player_row = row
            player_col = col
            maze[row][col] = " "
        elif maze[row][col] == "E":
            enemy_row = row
            enemy_col = col
            maze[row][col] = " "

score = 0
game_over = False


def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if maze[row][col] == "#":
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))

                if maze[row][col] == ".":
                    pygame.draw.circle(
                        screen, WHITE, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 5
                    )


def draw_player():
    x = player_col * CELL_SIZE + CELL_SIZE // 2
    y = player_row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, YELLOW, (x, y), CELL_SIZE // 2 - 4)


def draw_enemy():
    x = enemy_col * CELL_SIZE + CELL_SIZE // 2
    y = enemy_row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, RED, (x, y), CELL_SIZE // 2 - 4)


def draw_score():
    text = font.render(f"Točke: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def all_dots_collected():
    for row in maze:
        if "." in row:
            return False
    return True


def move_enemy():
    global enemy_row, enemy_col

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row = enemy_row + dr
        new_col = enemy_col + dc

        if maze[new_row][new_col] != "#":
            enemy_row = new_row
            enemy_col = new_col
            break


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_over:
            new_row = player_row
            new_col = player_col

            if event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1
            elif event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1

            if maze[new_row][new_col] != "#":
                player_row = new_row
                player_col = new_col

                if maze[player_row][player_col] == ".":
                    maze[player_row][player_col] = " "
                    score += 1

    if not game_over and not all_dots_collected():
        move_enemy()

    if player_row == enemy_row and player_col == enemy_col:
        game_over = True

    screen.fill(DARK)
    draw_maze()
    draw_player()
    draw_enemy()
    draw_score()

    if all_dots_collected():
        win_text = font.render("ZMAGA!", True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))

    if game_over:
        over_text = font.render("KONEC IGRE", True, RED)
        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(5)
