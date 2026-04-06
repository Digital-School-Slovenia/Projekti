"""Rešitve učnega lista – 28 – Projekt – Mini Zelda."""

# Namen: glavna delovna rešitev za učni list tega sklopa.

import pygame
import random
import math

pygame.init()

# Nastavitve okna
WIDTH, HEIGHT = 960, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Zelda - glavna rešitev")
clock = pygame.time.Clock()

# Pisave za HUD in sporočila
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 56)

# Barve (RGB)
WHITE = (245, 245, 245)
BLACK = (25, 25, 25)
BLUE = (70, 120, 255)
RED = (220, 80, 80)
GREEN = (70, 200, 100)
YELLOW = (240, 210, 70)
GRAY = (70, 70, 70)
DARK_BG = (35, 35, 45)

# Velikost "chunka" sveta (svet je neskončen, generira se okoli igralca)
CHUNK_SIZE = 600


def new_player():
    """Ustvari začetno stanje igralca."""
    return {
        "x": 0.0,
        "y": 0.0,
        "size": 40,
        "speed": 4,
        "hp": 5,
        "score": 0,
        "dir_x": 0,
        "dir_y": 1,
        "invuln": 0,
    }


# Globalno stanje igre
player = new_player()
collectibles = []
enemies = []
generated_chunks = set()

# Napad: timer (v frame-ih) in trenutni pravokotnik dosega napada
attack_timer = 0
attack_rect = pygame.Rect(0, 0, 0, 0)


def reset_game():
    """Ponastavi igro na začetno stanje."""
    global player, collectibles, enemies, generated_chunks, attack_timer, attack_rect
    player = new_player()
    collectibles = []
    enemies = []
    generated_chunks = set()
    attack_timer = 0
    attack_rect = pygame.Rect(0, 0, 0, 0)


def world_to_screen(wx, wy, camera_x, camera_y):
    """Pretvori svetovne koordinate v zaslonske (glede na kamero)."""
    return int(wx - camera_x), int(wy - camera_y)


def player_world_rect():
    """Pravokotnik igralca v svetovnih koordinatah (za trke)."""
    return pygame.Rect(
        int(player["x"]), int(player["y"]), player["size"], player["size"]
    )


def generate_chunk(chunk_x, chunk_y):
    """Generira vsebino enega chunka (kovanci + sovražniki), če še ni generiran."""
    if (chunk_x, chunk_y) in generated_chunks:
        return

    generated_chunks.add((chunk_x, chunk_y))
    base_x = chunk_x * CHUNK_SIZE
    base_y = chunk_y * CHUNK_SIZE

    # Kovanci
    for _ in range(5):
        size = 20
        x = random.randint(base_x + 40, base_x + CHUNK_SIZE - 40)
        y = random.randint(base_y + 40, base_y + CHUNK_SIZE - 40)
        collectibles.append({"x": x, "y": y, "size": size})

    # Sovražniki
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


def ensure_chunks_around_player():
    """Poskrbi, da so chunki v okolici igralca generirani (3x3 mreža)."""
    chunk_x = int(player["x"] // CHUNK_SIZE)
    chunk_y = int(player["y"] // CHUNK_SIZE)

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            generate_chunk(chunk_x + dx, chunk_y + dy)


def collect_items():
    """Pobere kovance, če igralec trči vanje."""
    p_rect = player_world_rect()

    for item in collectibles[:]:
        item_rect = pygame.Rect(item["x"], item["y"], item["size"], item["size"])
        if p_rect.colliderect(item_rect):
            collectibles.remove(item)
            player["score"] += 1


def update_enemies():
    """Premika sovražnike proti igralcu in ob trku zmanjša HP (z ohlajanjem)."""
    p_rect = player_world_rect()
    player_cx = player["x"] + player["size"] / 2
    player_cy = player["y"] + player["size"] / 2

    # Invuln: kratek čas neprebojnosti po zadetku (da se HP ne zmanjša vsako frame)
    if player["invuln"] > 0:
        player["invuln"] -= 1

    for enemy in enemies[:]:
        enemy_cx = enemy["x"] + enemy["size"] / 2
        enemy_cy = enemy["y"] + enemy["size"] / 2

        # Enostavna "AI": približaj se igralcu, če je dovolj blizu
        dx = player_cx - enemy_cx
        dy = player_cy - enemy_cy
        dist = math.hypot(dx, dy)

        if dist < 320 and dist != 0:
            enemy["x"] += enemy["speed"] * dx / dist
            enemy["y"] += enemy["speed"] * dy / dist

        # Ohlajanje, da isti sovražnik ne udari vsako frame
        if enemy["cooldown"] > 0:
            enemy["cooldown"] -= 1

        # Trk igralec–sovražnik
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
    """Začne napad: nastavi attack_rect glede na smer in poškoduje sovražnike v dosegu."""
    global attack_timer, attack_rect

    # Velikost hitboxa napada in dodatni doseg v smeri napada
    size = 36
    reach = 26
    px = player["x"]
    py = player["y"]
    ps = player["size"]

    # Hitbox napada se postavi pred igralca glede na zadnjo smer gibanja
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

    # Napad traja nekaj frame-ov (da se vidi bel okvir)
    attack_timer = 8

    # Zadeni vse sovražnike, ki so v hitboxu napada
    for enemy in enemies[:]:
        enemy_rect = pygame.Rect(
            int(enemy["x"]), int(enemy["y"]), enemy["size"], enemy["size"]
        )
        if attack_rect.colliderect(enemy_rect):
            enemy["hp"] -= 1
            if enemy["hp"] <= 0:
                enemies.remove(enemy)


def draw_hud():
    """Izriše HUD (kovanci, HP, navodila)."""
    score_text = font.render(f"Kovanci: {player['score']}", True, WHITE)
    hp_text = font.render(f"HP: {player['hp']}", True, WHITE)
    info_text = font.render(
        "WASD / puščice = gibanje, SPACE = napad, R = restart", True, WHITE
    )

    screen.blit(score_text, (20, 20))
    screen.blit(hp_text, (20, 55))
    screen.blit(info_text, (20, 90))


def draw_center_message(title, subtitle):
    """Izriše prosojno prekrivno sporočilo na sredini zaslona."""
    title_surf = big_font.render(title, True, WHITE)
    subtitle_surf = font.render(subtitle, True, WHITE)

    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    subtitle_rect = subtitle_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

    # Prosojna črna "zavesa" čez ozadje
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)


running = True
game_over = False

while running:
    # Omejitev na 60 FPS
    clock.tick(60)

    # 1) Dogodki (zapiranje, tipke)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                game_over = False
            elif event.key == pygame.K_SPACE and not game_over:
                start_attack()

    keys = pygame.key.get_pressed()

    # 2) Posodobitev logike (premik, trki, sovražniki)
    if not game_over:
        dx = 0
        dy = 0

        # Smer gibanja + zapomnimo si zadnjo smer (za napad)
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

        # Normalizacija: diagonala ne sme biti hitrejša od premika v eno smer
        if dx != 0 or dy != 0:
            length = math.hypot(dx, dy)
            dx = dx / length * player["speed"]
            dy = dy / length * player["speed"]

        # Premik v svetovnih koordinatah
        player["x"] += dx
        player["y"] += dy

        # Generiraj okolico, pobiraj kovance in posodobi sovražnike
        ensure_chunks_around_player()
        collect_items()
        update_enemies()

        # Odštevanje trajanja napada (število frame-ov)
        if attack_timer > 0:
            attack_timer -= 1

        # Pogoj za konec igre
        if player["hp"] <= 0:
            game_over = True

    # 3) Kamera: igralec je na sredini zaslona, svet se premika okoli njega
    camera_x = player["x"] - WIDTH // 2 + player["size"] // 2
    camera_y = player["y"] - HEIGHT // 2 + player["size"] // 2

    # 4) Risanje
    screen.fill(DARK_BG)

    # Mreža ozadja (za občutek premika po svetu)
    grid_size = 80
    start_x = -int(camera_x) % grid_size
    start_y = -int(camera_y) % grid_size

    for x in range(start_x, WIDTH, grid_size):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(start_y, HEIGHT, grid_size):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # Kovanci
    for item in collectibles:
        sx, sy = world_to_screen(item["x"], item["y"], camera_x, camera_y)
        pygame.draw.rect(screen, YELLOW, (sx, sy, item["size"], item["size"]))

    # Sovražniki
    for enemy in enemies:
        sx, sy = world_to_screen(enemy["x"], enemy["y"], camera_x, camera_y)
        pygame.draw.rect(screen, RED, (sx, sy, enemy["size"], enemy["size"]))

    # Vizualizacija napada (bel okvir), dokler attack_timer teče
    if attack_timer > 0:
        ax, ay = world_to_screen(attack_rect.x, attack_rect.y, camera_x, camera_y)
        pygame.draw.rect(
            screen, WHITE, (ax, ay, attack_rect.width, attack_rect.height), 3
        )

    # Igralec je vedno izrisan na sredini (ker kamera sledi igralcu)
    player_rect = pygame.Rect(
        WIDTH // 2 - player["size"] // 2,
        HEIGHT // 2 - player["size"] // 2,
        player["size"],
        player["size"],
    )

    # Utripanje med invuln (vizualni feedback, da je neprebojen)
    if player["invuln"] == 0 or player["invuln"] % 10 < 5:
        pygame.draw.rect(screen, BLUE, player_rect)

    draw_hud()

    # Sporočilo ob koncu igre
    if game_over:
        draw_center_message("Konec igre", "Pritisni R za novo igro")

    pygame.display.flip()

pygame.quit()
