"""Rešitve dodatnih nalog – 28 – Projekt – Mini Zelda."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 960, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Zelda - dodatne naloge")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 56)

WHITE = (245, 245, 245)
BLACK = (25, 25, 25)
BLUE = (70, 120, 255)
RED = (220, 80, 80)
GREEN = (70, 200, 100)
YELLOW = (240, 210, 70)
GRAY = (70, 70, 70)
DARK_BG = (35, 35, 45)
PINK = (255, 110, 150)
PURPLE = (160, 110, 255)
STONE = (105, 105, 115)

CHUNK_SIZE = 600
PORTAL_SCORE = 12
MAX_HP = 5


def new_player():
    return {
        "x": 0.0,
        "y": 0.0,
        "size": 40,
        "speed": 4,
        "hp": MAX_HP,
        "score": 0,
        "dir_x": 0,
        "dir_y": 1,
        "invuln": 0,
    }


player = new_player()
collectibles = []
enemies = []
obstacles = []
hearts = []
generated_chunks = set()

portal = {"x": -50, "y": -50, "size": 100, "active": False}
attack_timer = 0
attack_rect = pygame.Rect(0, 0, 0, 0)


def reset_game():
    global player, collectibles, enemies, obstacles, hearts, generated_chunks, portal, attack_timer, attack_rect
    player = new_player()
    collectibles = []
    enemies = []
    obstacles = []
    hearts = []
    generated_chunks = set()
    portal = {"x": -50, "y": -50, "size": 100, "active": False}
    attack_timer = 0
    attack_rect = pygame.Rect(0, 0, 0, 0)


def world_to_screen(wx, wy, camera_x, camera_y):
    return int(wx - camera_x), int(wy - camera_y)


def player_world_rect():
    return pygame.Rect(
        int(player["x"]), int(player["y"]), player["size"], player["size"]
    )


def collides_with_obstacles(test_rect):
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(
            obstacle["x"], obstacle["y"], obstacle["size"], obstacle["size"]
        )
        if test_rect.colliderect(obstacle_rect):
            return True
    return False


def generate_chunk(chunk_x, chunk_y):
    if (chunk_x, chunk_y) in generated_chunks:
        return

    generated_chunks.add((chunk_x, chunk_y))
    base_x = chunk_x * CHUNK_SIZE
    base_y = chunk_y * CHUNK_SIZE

    for _ in range(5):
        size = 20
        x = random.randint(base_x + 40, base_x + CHUNK_SIZE - 40)
        y = random.randint(base_y + 40, base_y + CHUNK_SIZE - 40)
        collectibles.append({"x": x, "y": y, "size": size})

    for _ in range(2):
        size = 35
        x = random.randint(base_x + 60, base_x + CHUNK_SIZE - 60)
        y = random.randint(base_y + 60, base_y + CHUNK_SIZE - 60)
        enemies.append(
            {
                "x": float(x),
                "y": float(y),
                "size": size,
                "speed": 1.4,
                "hp": 2,
                "cooldown": 0,
            }
        )

    for _ in range(5):
        size = 60
        x = random.randint(base_x + 60, base_x + CHUNK_SIZE - 120)
        y = random.randint(base_y + 60, base_y + CHUNK_SIZE - 120)

        # okoli svetišča pustimo nekaj prostora
        if math.hypot(x, y) < 180:
            continue

        obstacle_rect = pygame.Rect(x, y, size, size)
        if not collides_with_obstacles(obstacle_rect):
            obstacles.append({"x": x, "y": y, "size": size})

    if random.random() < 0.35:
        size = 24
        x = random.randint(base_x + 80, base_x + CHUNK_SIZE - 80)
        y = random.randint(base_y + 80, base_y + CHUNK_SIZE - 80)
        hearts.append({"x": x, "y": y, "size": size})


def ensure_chunks_around_player():
    chunk_x = int(player["x"] // CHUNK_SIZE)
    chunk_y = int(player["y"] // CHUNK_SIZE)

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            generate_chunk(chunk_x + dx, chunk_y + dy)


def move_player_with_collisions(dx, dy):
    if dx != 0:
        test_rect = pygame.Rect(
            int(player["x"] + dx), int(player["y"]), player["size"], player["size"]
        )
        if not collides_with_obstacles(test_rect):
            player["x"] += dx

    if dy != 0:
        test_rect = pygame.Rect(
            int(player["x"]), int(player["y"] + dy), player["size"], player["size"]
        )
        if not collides_with_obstacles(test_rect):
            player["y"] += dy


def collect_items():
    p_rect = player_world_rect()

    for item in collectibles[:]:
        item_rect = pygame.Rect(item["x"], item["y"], item["size"], item["size"])
        if p_rect.colliderect(item_rect):
            collectibles.remove(item)
            player["score"] += 1


def collect_hearts():
    p_rect = player_world_rect()

    for heart in hearts[:]:
        heart_rect = pygame.Rect(heart["x"], heart["y"], heart["size"], heart["size"])
        if p_rect.colliderect(heart_rect):
            hearts.remove(heart)
            if player["hp"] < MAX_HP:
                player["hp"] += 1


def update_portal():
    if player["score"] >= PORTAL_SCORE:
        portal["active"] = True


def update_enemies():
    p_rect = player_world_rect()
    player_cx = player["x"] + player["size"] / 2
    player_cy = player["y"] + player["size"] / 2

    if player["invuln"] > 0:
        player["invuln"] -= 1

    for enemy in enemies[:]:
        enemy_cx = enemy["x"] + enemy["size"] / 2
        enemy_cy = enemy["y"] + enemy["size"] / 2

        dx = player_cx - enemy_cx
        dy = player_cy - enemy_cy
        dist = math.hypot(dx, dy)

        if dist < 320 and dist != 0:
            step_x = enemy["speed"] * dx / dist
            step_y = enemy["speed"] * dy / dist

            test_rect_x = pygame.Rect(
                int(enemy["x"] + step_x), int(enemy["y"]), enemy["size"], enemy["size"]
            )
            if not collides_with_obstacles(test_rect_x):
                enemy["x"] += step_x

            test_rect_y = pygame.Rect(
                int(enemy["x"]), int(enemy["y"] + step_y), enemy["size"], enemy["size"]
            )
            if not collides_with_obstacles(test_rect_y):
                enemy["y"] += step_y

        if enemy["cooldown"] > 0:
            enemy["cooldown"] -= 1

        enemy_rect = pygame.Rect(
            int(enemy["x"]), int(enemy["y"]), enemy["size"], enemy["size"]
        )
        if (
            enemy_rect.colliderect(p_rect)
            and enemy["cooldown"] == 0
            and player["invuln"] == 0
        ):
            player["hp"] -= 1
            player["invuln"] = 50
            enemy["cooldown"] = 45


def start_attack():
    global attack_timer, attack_rect

    size = 36
    reach = 26
    px = player["x"]
    py = player["y"]
    ps = player["size"]

    if player["dir_x"] == 1:
        attack_rect = pygame.Rect(
            int(px + ps), int(py + ps // 2 - size // 2), size + reach, size
        )
    elif player["dir_x"] == -1:
        attack_rect = pygame.Rect(
            int(px - size - reach), int(py + ps // 2 - size // 2), size + reach, size
        )
    elif player["dir_y"] == 1:
        attack_rect = pygame.Rect(
            int(px + ps // 2 - size // 2), int(py + ps), size, size + reach
        )
    else:
        attack_rect = pygame.Rect(
            int(px + ps // 2 - size // 2), int(py - size - reach), size, size + reach
        )

    attack_timer = 8

    for enemy in enemies[:]:
        enemy_rect = pygame.Rect(
            int(enemy["x"]), int(enemy["y"]), enemy["size"], enemy["size"]
        )
        if attack_rect.colliderect(enemy_rect):
            enemy["hp"] -= 1
            if enemy["hp"] <= 0:
                enemies.remove(enemy)


def portal_rect():
    return pygame.Rect(portal["x"], portal["y"], portal["size"], portal["size"])


def check_victory():
    return portal["active"] and player_world_rect().colliderect(portal_rect())


def draw_hud():
    score_text = font.render(f"Kovanci: {player['score']}/{PORTAL_SCORE}", True, WHITE)
    hp_text = font.render(f"HP: {player['hp']}", True, WHITE)
    info_text = font.render(
        "WASD / puščice = gibanje, SPACE = napad, R = restart", True, WHITE
    )
    goal_text = font.render("Cilj: zberi kovance in se vrni v svetišče", True, WHITE)

    screen.blit(score_text, (20, 20))
    screen.blit(hp_text, (20, 55))
    screen.blit(info_text, (20, 90))
    screen.blit(goal_text, (20, 125))


def draw_center_message(title, subtitle):
    title_surf = big_font.render(title, True, WHITE)
    subtitle_surf = font.render(subtitle, True, WHITE)

    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    subtitle_rect = subtitle_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)


running = True
game_over = False
victory = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                game_over = False
                victory = False
            elif event.key == pygame.K_SPACE and not game_over and not victory:
                start_attack()

    keys = pygame.key.get_pressed()

    if not game_over and not victory:
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
            player["dir_x"], player["dir_y"] = -1, 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
            player["dir_x"], player["dir_y"] = 1, 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
            player["dir_x"], player["dir_y"] = 0, -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
            player["dir_x"], player["dir_y"] = 0, 1

        if dx != 0 or dy != 0:
            length = math.hypot(dx, dy)
            dx = dx / length * player["speed"]
            dy = dy / length * player["speed"]

        ensure_chunks_around_player()
        move_player_with_collisions(dx, dy)
        collect_items()
        collect_hearts()
        update_portal()
        update_enemies()

        if attack_timer > 0:
            attack_timer -= 1

        if player["hp"] <= 0:
            game_over = True

        if check_victory():
            victory = True

    camera_x = player["x"] - WIDTH // 2 + player["size"] // 2
    camera_y = player["y"] - HEIGHT // 2 + player["size"] // 2

    screen.fill(DARK_BG)

    grid_size = 80
    start_x = -int(camera_x) % grid_size
    start_y = -int(camera_y) % grid_size

    for x in range(start_x, WIDTH, grid_size):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(start_y, HEIGHT, grid_size):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    for obstacle in obstacles:
        sx, sy = world_to_screen(obstacle["x"], obstacle["y"], camera_x, camera_y)
        pygame.draw.rect(screen, STONE, (sx, sy, obstacle["size"], obstacle["size"]))

    shrine = portal_rect()
    shrine_sx, shrine_sy = world_to_screen(shrine.x, shrine.y, camera_x, camera_y)
    shrine_color = PURPLE if portal["active"] else GRAY
    pygame.draw.rect(
        screen, shrine_color, (shrine_sx, shrine_sy, shrine.width, shrine.height), 4
    )

    for item in collectibles:
        sx, sy = world_to_screen(item["x"], item["y"], camera_x, camera_y)
        pygame.draw.rect(screen, YELLOW, (sx, sy, item["size"], item["size"]))

    for heart in hearts:
        sx, sy = world_to_screen(heart["x"], heart["y"], camera_x, camera_y)
        pygame.draw.rect(screen, PINK, (sx, sy, heart["size"], heart["size"]))

    for enemy in enemies:
        sx, sy = world_to_screen(enemy["x"], enemy["y"], camera_x, camera_y)
        pygame.draw.rect(screen, RED, (sx, sy, enemy["size"], enemy["size"]))

    if attack_timer > 0:
        ax, ay = world_to_screen(attack_rect.x, attack_rect.y, camera_x, camera_y)
        pygame.draw.rect(
            screen, WHITE, (ax, ay, attack_rect.width, attack_rect.height), 3
        )

    player_rect = pygame.Rect(
        WIDTH // 2 - player["size"] // 2,
        HEIGHT // 2 - player["size"] // 2,
        player["size"],
        player["size"],
    )

    if player["invuln"] == 0 or player["invuln"] % 10 < 5:
        pygame.draw.rect(screen, BLUE, player_rect)

    draw_hud()

    if game_over:
        draw_center_message("Konec igre", "Pritisni R za novo igro")
    elif victory:
        draw_center_message("Zmaga", "Vrnil si se v svetišče. Pritisni R za novo igro")

    pygame.display.flip()

pygame.quit()
