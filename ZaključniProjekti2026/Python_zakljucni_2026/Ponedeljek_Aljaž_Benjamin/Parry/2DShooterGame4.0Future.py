import pygame
import random
import math
import tkinter as tk
from quizToPlay import *

# =========================
# QUIZ START
# =========================

root = tk.Tk()
app = Quiz(root)
root.mainloop()

# =========================
# PYGAME INIT
# =========================

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Glasba-Napisal-LeonJonatanPrebil.mp3")
pygame.mixer.music.play(-1)

# =========================
# SCREEN
# =========================

SIRINA = 900
VISINA = 600

zaslon = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption("JOHN > v <")

ura = pygame.time.Clock()

# =========================
# SPRITES
# =========================

player_idle = pygame.image.load(
    "img/player_idle.png"
).convert_alpha()

player_shooting = pygame.image.load(
    "img/player_shooting.png"
).convert_alpha()

zombie_idle = pygame.image.load(
    "img/zombie_idle.png"
).convert_alpha()

zombie_shooting = pygame.image.load(
    "img/zombie_shooting.png"
).convert_alpha()

boss_idle = pygame.image.load(
    "img/boss_idle.png"
).convert_alpha()

boss_shooting = pygame.image.load(
    "img/boss_shooting.png"
).convert_alpha()

johnName = pygame.image.load(
    "img/johnName.png"
).convert_alpha()

# =========================
# COLORS
# =========================

BELA = (255,255,255)
RDECA = (255,0,0)
ZELENA = (0,255,0)
MODRA = (50,100,255)
SVETLO_MODRA = (100,200,255)
CRNA = (0,0,0)
RUMENA = (255,255,0)
VIJOLICNA = (180,0,255)
STRELA = (200,255,255)
ORANZNA = (255,140,0)

# =========================
# FONTS
# =========================

pisava = pygame.font.SysFont(None, 36)
velika_pisava = pygame.font.SysFont(None, 72)

# =========================
# PLAYER
# =========================

igralec_poz = [150, VISINA//2]

igralec_radius = 20

igralec_hp = 100

igralec_speedx = 0
igralec_speedy = 0

player_shoot_timer = 0

player_flip = False

# =========================
# PARRY
# =========================

parry_aktiven = False

parry_timer = 0

PARRY_TRAJANJE = 150

parry_cooldown = 0

PARRY_COOLDOWN_MAX = 120

# =========================
# BOSS
# =========================

boss_poz = [700, VISINA//2]

boss_radius = 45

boss_hp = 200

boss_hitrost = 2

boss_damage_timer = 0

boss_damage_delay = 25

boss_shoot_timer = 0

boss_flip = False

# =========================
# BULLETS
# =========================

metki = []

timer_metkov = 0

ZAMIK_STRELJANJA = 10

# =========================
# ZOMBIES
# =========================

zombiji = []

timer_zombijev = 0

zombi_damage_timer = 0

zombi_damage_delay = 10

# =========================
# GRENADES
# =========================

granate = []

maks_granat = 4

stevilo_granat = 4

super_granata_uporabljena = False

super_granate = []

# =========================
# EFFECTS
# =========================

lightning_zones = []

lightning_hits = []

shockwaves = []

# =========================
# GAME STATE
# =========================

game_over = False

zmagovalec = ""

# =========================
# MENU
# =========================

v_menuju = True

while v_menuju:

    zaslon.fill((10,10,10))

    naslov = pygame.transform.scale(
        johnName,
        (420,140)
    )

    play_text = pisava.render(
        "KLIKNI SPACE DA IGRAŠ",
        True,
        BELA
    )

    controls1 = pisava.render(
        "WASD / PUŠČICE = PREMIKANJE",
        True,
        SVETLO_MODRA
    )

    controls2 = pisava.render(
        "M / E = GRENATE",
        True,
        VIJOLICNA
    )

    controls3 = pisava.render(
        "R = SUPER GRENATA",
        True,
        ORANZNA
    )

    controls4 = pisava.render(
        "Q / N = PARRY/ŠČIT",
        True,
        ZELENA
    )

    exit_text = pisava.render(
        "ESC = ZAPRI",
        True,
        RDECA
    )

    zaslon.blit(
        naslov,
        (
            SIRINA//2 - naslov.get_width()//2,
            120
        )
    )

    zaslon.blit(
        play_text,
        (
            SIRINA//2 - play_text.get_width()//2,
            250
        )
    )

    zaslon.blit(
        controls1,
        (
            SIRINA//2 - controls1.get_width()//2,
            340
        )
    )

    zaslon.blit(
        controls2,
        (
            SIRINA//2 - controls2.get_width()//2,
            390
        )
    )

    zaslon.blit(
        controls3,
        (
            SIRINA//2 - controls3.get_width()//2,
            440
        )
    )

    zaslon.blit(
        controls4,
        (
            SIRINA//2 - controls4.get_width()//2,
            490
        )
    )

    zaslon.blit(
        exit_text,
        (
            SIRINA//2 - exit_text.get_width()//2,
            540
        )
    )

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                v_menuju = False

    ura.tick(60)

# =========================
# GAME LOOP
# =========================

tece = True

while tece:

    zaslon.fill((20,20,20))

    mx, my = pygame.mouse.get_pos()

    # =========================
    # TIMERS
    # =========================

    if boss_damage_timer > 0:
        boss_damage_timer -= 1

    if zombi_damage_timer > 0:
        zombi_damage_timer -= 1

    if player_shoot_timer > 0:
        player_shoot_timer -= 1

    if boss_shoot_timer > 0:
        boss_shoot_timer -= 1

    # =========================
    # FLIP
    # =========================

    if mx < igralec_poz[0]:
        player_flip = True
    else:
        player_flip = False

    if igralec_poz[0] < boss_poz[0]:
        boss_flip = True
    else:
        boss_flip = False

    # =========================
    # EVENTS
    # =========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            tece = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                tece = False

            if (
                event.key == pygame.K_n
            ) or (
                event.key == pygame.K_q
            ):

                if (
                    not parry_aktiven
                    and
                    parry_cooldown <= 0
                ):

                    parry_aktiven = True

                    parry_timer = PARRY_TRAJANJE

                    parry_cooldown = PARRY_COOLDOWN_MAX
                if (
                (
                    event.key == pygame.K_m
                )
                or
                (
                    event.key == pygame.K_e
                )
            ) and stevilo_granat > 0:

                    dx = mx - igralec_poz[0]
                    dy = my - igralec_poz[1]

                razdalja = math.hypot(dx, dy)

                if razdalja != 0:
                    dx /= razdalja
                    dy /= razdalja

                granate.append({
                    "x": igralec_poz[0] + dx * 140,
                    "y": igralec_poz[1] + dy * 140,
                    "timer": 60
                })

                stevilo_granat -= 1

    # =========================
    # MOVEMENT
    # =========================

    tipke = pygame.key.get_pressed()

    if tipke[pygame.K_a] or tipke[pygame.K_LEFT]:
        igralec_speedx -= 1.5

    if tipke[pygame.K_d] or tipke[pygame.K_RIGHT]:
        igralec_speedx += 1.5

    if tipke[pygame.K_w] or tipke[pygame.K_UP]:
        igralec_speedy -= 1.5

    if tipke[pygame.K_s] or tipke[pygame.K_DOWN]:
        igralec_speedy += 1.5

    igralec_poz[0] += igralec_speedx
    igralec_poz[1] += igralec_speedy

    igralec_speedx *= 0.75
    igralec_speedy *= 0.75

    igralec_poz[0] = max(
        0,
        min(SIRINA, igralec_poz[0])
    )

    igralec_poz[1] = max(
        0,
        min(VISINA, igralec_poz[1])
    )

    # =========================
    # PARRY
    # =========================

    if parry_aktiven:

        parry_timer -= 1

        if parry_timer <= 0:
            parry_aktiven = False

    if parry_cooldown > 0:
        parry_cooldown -= 1

    # =========================
    # SHOOTING
    # =========================

    timer_metkov += 1

    if (
        timer_metkov >= ZAMIK_STRELJANJA
        and
        not parry_aktiven
    ):

        player_shoot_timer = 8

        dx = mx - igralec_poz[0]
        dy = my - igralec_poz[1]

        razdalja = math.hypot(dx,dy)

        if razdalja != 0:
            dx /= razdalja
            dy /= razdalja

        metki.append({
            "x": igralec_poz[0],
            "y": igralec_poz[1],
            "dx": dx,
            "dy": dy
        })

        timer_metkov = 0

    # =========================
    # BULLETS
    # =========================

    for metek in metki[:]:

        metek["x"] += metek["dx"] * 14
        metek["y"] += metek["dy"] * 14

        if (
            metek["x"] < 0
            or
            metek["x"] > SIRINA
            or
            metek["y"] < 0
            or
            metek["y"] > VISINA
        ):
            metki.remove(metek)
            continue

        pygame.draw.circle(
            zaslon,
            ORANZNA,
            (
                int(metek["x"]),
                int(metek["y"])
            ),
            6
        )

        pygame.draw.circle(
            zaslon,
            RUMENA,
            (
                int(metek["x"]),
                int(metek["y"])
            ),
            3
        )

    # =========================
    # BOSS MOVE
    # =========================

    if boss_poz[1] < igralec_poz[1]:
        boss_poz[1] += boss_hitrost

    elif boss_poz[1] > igralec_poz[1]:
        boss_poz[1] -= boss_hitrost

    # =========================
    # SPAWN ZOMBIES
    # =========================

    timer_zombijev += 1

    if timer_zombijev >= 45:

        stran = random.randint(1,4)

        if stran == 1:

            zx = random.randint(
                0,
                SIRINA
            )

            zy = -30

        elif stran == 2:

            zx = random.randint(
                0,
                SIRINA
            )

            zy = VISINA + 30

        elif stran == 3:

            zx = -30

            zy = random.randint(
                0,
                VISINA
            )

        else:

            zx = SIRINA + 30

            zy = random.randint(
                0,
                VISINA
            )

        zombiji.append([zx, zy])

        timer_zombijev = 0

    # =========================
    # ZOMBIES
    # =========================

    for zombi in zombiji:

        dx = igralec_poz[0] - zombi[0]
        dy = igralec_poz[1] - zombi[1]

        razdalja = math.hypot(dx,dy)

        if razdalja != 0:

            zombi[0] += (
                dx / razdalja
            ) * random.uniform(
                1.8,
                3.4
            )

            zombi[1] += (
                dy / razdalja
            ) * random.uniform(
                1.8,
                3.4
            )

        zombie_sprite = zombie_idle

        if random.randint(1,20) == 1:
            zombie_sprite = zombie_shooting

        zombie_flip = False

        if igralec_poz[0] < zombi[0]:
            zombie_flip = True

        zombie_img = pygame.transform.scale(
            zombie_sprite,
            (55,55)
        )

        if zombie_flip:

            zombie_img = pygame.transform.flip(
                zombie_img,
                True,
                False
            )

        zaslon.blit(
            zombie_img,
            (
                int(zombi[0] - 27),
                int(zombi[1] - 27)
            )
        )

    # =========================
    # PLAYER SPRITE
    # =========================

    if player_shoot_timer > 0:
        player_sprite = player_shooting
    else:
        player_sprite = player_idle

    player_img = pygame.transform.scale(
        player_sprite,
        (90,90)
    )

    if player_flip:

        player_img = pygame.transform.flip(
            player_img,
            True,
            False
        )

    zaslon.blit(
        player_img,
        (
            int(igralec_poz[0] - 45),
            int(igralec_poz[1] - 45)
        )
    )

    # =========================
    # PARRY VISUAL
    # =========================

    if parry_aktiven:

        pygame.draw.circle(
            zaslon,
            SVETLO_MODRA,
            (
                int(igralec_poz[0]),
                int(igralec_poz[1])
            ),
            igralec_radius + 10,
            4
        )

    # =========================
    # BOSS SPRITE
    # =========================

    if boss_shoot_timer > 0:
        boss_sprite = boss_shooting
    else:
        boss_sprite = boss_idle

    boss_img = pygame.transform.scale(
        boss_sprite,
        (140,140)
    )

    if boss_flip:

        boss_img = pygame.transform.flip(
            boss_img,
            True,
            False
        )

    zaslon.blit(
        boss_img,
        (
            int(boss_poz[0] - 70),
            int(boss_poz[1] - 70)
        )
    )

    # =========================
    # HP BARS
    # =========================

    pygame.draw.rect(
        zaslon,
        RDECA,
        (20,20,200,20)
    )

    pygame.draw.rect(
        zaslon,
        ZELENA,
        (
            20,
            20,
            max(0,igralec_hp)*2,
            20
        )
    )

    pygame.draw.rect(
        zaslon,
        RDECA,
        (
            SIRINA-420,
            20,
            400,
            20
        )
    )

    pygame.draw.rect(
        zaslon,
        ZELENA,
        (
            SIRINA-420,
            20,
            max(0,boss_hp)*2,
            20
        )
    )

    igralec_text = pisava.render(
        f"{igralec_hp}/100",
        True,
        BELA
    )

    boss_text = pisava.render(
        f"{boss_hp}/200",
        True,
        BELA
    )

    zaslon.blit(
        igralec_text,
        (80,45)
    )

    zaslon.blit(
        boss_text,
        (SIRINA-250,45)
    )

    # =========================
    # GAME OVER
    # =========================

    if igralec_hp <= 0:

        game_over = True

        zmagovalec = "BOSS WINS"

    if boss_hp <= 0:

        game_over = True

        zmagovalec = "YOU WIN"

    if game_over:

        zaslon.fill(CRNA)

        barva = (
            RDECA
            if "BOSS" in zmagovalec
            else ZELENA
        )

        text = velika_pisava.render(
            zmagovalec,
            True,
            barva
        )

        zaslon.blit(
            text,
            (
                SIRINA//2 - text.get_width()//2,
                VISINA//2 - 50
            )
        )

        pygame.display.flip()

        pygame.time.delay(3000)

        tece = False

    pygame.display.flip()

    ura.tick(60)

pygame.quit()