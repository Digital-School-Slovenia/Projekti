# Nadgradnja – 32 Projekt Mini Wolfenstein z miško

import math
import sys
import pygame

# ============================================================
# MINI WOLFENSTEIN / RAYCASTING
# Učiteljska rešitev z obračanjem z miško
# ============================================================

pygame.init()

# -----------------------------
# Osnovne nastavitve
# -----------------------------
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Wolfenstein - učiteljska rešitev (miška)")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 54)

# -----------------------------
# Barve
# -----------------------------
WHITE = (245, 245, 245)
BLACK = (10, 10, 10)
GRAY = (90, 90, 90)
DARK_GRAY = (45, 45, 45)
SKY = (90, 140, 210)
FLOOR = (65, 55, 45)
RED = (210, 80, 80)
GREEN = (80, 200, 100)
YELLOW = (230, 220, 90)
BLUE = (80, 140, 220)

# -----------------------------
# Mapa
# 1 = stena
# 0 = prazno
# 2 = cilj / izhod
# -----------------------------
MAP_DATA = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,1,1,1,1,1,1,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
]

MAP_ROWS = len(MAP_DATA)
MAP_COLS = len(MAP_DATA[0])
TILE_SIZE = 64
WORLD_WIDTH = MAP_COLS * TILE_SIZE
WORLD_HEIGHT = MAP_ROWS * TILE_SIZE

# -----------------------------
# Igralec
# -----------------------------
player_x = 1.5 * TILE_SIZE
player_y = 1.5 * TILE_SIZE
player_angle = 0
MOVE_SPEED = 2.8
ROT_SPEED = 0.04
MOUSE_SENSITIVITY = 0.0035
PLAYER_RADIUS = 10

# -----------------------------
# Nadzor
# -----------------------------
show_minimap = True
mouse_look = True
won = False

# -----------------------------
# Raycasting nastavitve
# -----------------------------
FOV = math.pi / 3           # 60 stopinj
NUM_RAYS = 220
MAX_DEPTH = 900
DELTA_ANGLE = FOV / NUM_RAYS
DIST_TO_PROJ_PLANE = (WIDTH // 2) / math.tan(FOV / 2)
SCALE = WIDTH / NUM_RAYS


def set_mouse_mode(enabled):
    """Vklopi ali izklopi 'zaklep' miške v okno."""
    pygame.event.set_grab(enabled)
    pygame.mouse.set_visible(not enabled)
    pygame.mouse.get_rel()  # Počisti prvi velik skok po preklopu


# -----------------------------
# Funkcije za mapo in gibanje
# -----------------------------
def get_map_cell(world_x, world_y):
    """Vrne vrednost celice v mapi glede na world koordinate."""
    col = int(world_x // TILE_SIZE)
    row = int(world_y // TILE_SIZE)

    if row < 0 or row >= MAP_ROWS or col < 0 or col >= MAP_COLS:
        return 1
    return MAP_DATA[row][col]



def is_wall(world_x, world_y):
    return get_map_cell(world_x, world_y) == 1



def is_exit(world_x, world_y):
    return get_map_cell(world_x, world_y) == 2



def move_player(dx, dy):
    """Premakni igralca posebej po x in y, da je gibanje ob stenah bolj naravno."""
    global player_x, player_y

    new_x = player_x + dx
    new_y = player_y + dy

    if not is_wall(new_x, player_y):
        player_x = new_x
    if not is_wall(player_x, new_y):
        player_y = new_y



def cast_single_ray(ray_angle):
    """Preprost raycasting s koraki po žarku."""
    depth = 0
    step = 4

    while depth < MAX_DEPTH:
        target_x = player_x + math.cos(ray_angle) * depth
        target_y = player_y + math.sin(ray_angle) * depth
        cell = get_map_cell(target_x, target_y)

        if cell == 1:
            return depth, 1
        depth += step

    return MAX_DEPTH, 0


# -----------------------------
# Funkcije za risanje
# -----------------------------
def draw_3d_view():
    pygame.draw.rect(screen, SKY, (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(screen, FLOOR, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    start_angle = player_angle - FOV / 2

    for ray in range(NUM_RAYS):
        ray_angle = start_angle + ray * DELTA_ANGLE
        depth, hit_type = cast_single_ray(ray_angle)

        corrected_depth = depth * math.cos(player_angle - ray_angle)
        corrected_depth = max(corrected_depth, 0.0001)

        wall_height = (TILE_SIZE / corrected_depth) * DIST_TO_PROJ_PLANE
        wall_height = min(wall_height, HEIGHT * 2)

        shade = max(30, min(255, int(255 / (1 + corrected_depth * 0.01))))
        wall_color = (shade, shade, shade)

        x = ray * SCALE
        y = HEIGHT // 2 - wall_height // 2
        pygame.draw.rect(screen, wall_color, (x, y, SCALE + 1, wall_height))



def draw_minimap():
    if not show_minimap:
        return

    mini_scale = 0.22
    mini_tile = int(TILE_SIZE * mini_scale)
    offset_x = 15
    offset_y = 15

    map_w = MAP_COLS * mini_tile
    map_h = MAP_ROWS * mini_tile
    pygame.draw.rect(screen, (20, 20, 20), (offset_x - 6, offset_y - 6, map_w + 12, map_h + 12), border_radius=8)

    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            value = MAP_DATA[row][col]
            x = offset_x + col * mini_tile
            y = offset_y + row * mini_tile

            color = DARK_GRAY
            if value == 1:
                color = GRAY
            elif value == 2:
                color = GREEN

            pygame.draw.rect(screen, color, (x, y, mini_tile - 1, mini_tile - 1))

    px = offset_x + int((player_x / TILE_SIZE) * mini_tile)
    py = offset_y + int((player_y / TILE_SIZE) * mini_tile)
    pygame.draw.circle(screen, YELLOW, (px, py), 4)

    line_length = 18
    lx = px + math.cos(player_angle) * line_length
    ly = py + math.sin(player_angle) * line_length
    pygame.draw.line(screen, YELLOW, (px, py), (lx, ly), 2)



def draw_hud():
    line1 = font.render("W/S = naprej/nazaj | A/D = rezervno obračanje | TAB = miška ON/OFF", True, WHITE)
    line2 = font.render("M = minimapa | ESC = izhod", True, WHITE)
    screen.blit(line1, (15, HEIGHT - 58))
    screen.blit(line2, (15, HEIGHT - 30))



def draw_win_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    screen.blit(overlay, (0, 0))

    text1 = big_font.render("CILJ DOSEŽEN!", True, GREEN)
    text2 = font.render("Pritisni R za ponovno igro ali ESC za izhod.", True, WHITE)

    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 15))



def reset_game():
    global player_x, player_y, player_angle, won
    player_x = 1.5 * TILE_SIZE
    player_y = 1.5 * TILE_SIZE
    player_angle = 0
    won = False
    pygame.mouse.get_rel()



def main():
    global player_angle, show_minimap, mouse_look, won

    if mouse_look:
        set_mouse_mode(True)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    show_minimap = not show_minimap
                if event.key == pygame.K_r and won:
                    reset_game()
                if event.key == pygame.K_TAB:
                    mouse_look = not mouse_look
                    set_mouse_mode(mouse_look)

        keys = pygame.key.get_pressed()

        if not won:
            if mouse_look and pygame.mouse.get_focused():
                mouse_dx, _ = pygame.mouse.get_rel()
                player_angle += mouse_dx * MOUSE_SENSITIVITY
            else:
                pygame.mouse.get_rel()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player_angle -= ROT_SPEED
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player_angle += ROT_SPEED

            player_angle %= math.tau

            move_step = 0
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                move_step += MOVE_SPEED
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                move_step -= MOVE_SPEED

            dx = math.cos(player_angle) * move_step
            dy = math.sin(player_angle) * move_step
            move_player(dx, dy)

            if is_exit(player_x, player_y):
                won = True

        draw_3d_view()
        draw_minimap()
        draw_hud()

        if won:
            draw_win_screen()

        pygame.display.flip()


if __name__ == "__main__":
    main()
