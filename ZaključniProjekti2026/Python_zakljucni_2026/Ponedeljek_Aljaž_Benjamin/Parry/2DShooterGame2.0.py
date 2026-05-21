import pygame
import random
import math
#from quizToPlay import *
#root = tk.Tk()
#app = Quiz(root)
#root.mainloop()

pygame.init()

SIRINA = 900
VISINA = 600

zaslon = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption("ULTIMATE BOSS FIGHT")

ura = pygame.time.Clock()

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

pisava = pygame.font.SysFont(None, 36)
velika_pisava = pygame.font.SysFont(None, 72)

igralec_poz = [150, VISINA//2]
igralec_radius = 20
igralec_hp = 100

parry_aktiven = False
parry_timer = 0
PARRY_TRAJANJE = 150

parry_cooldown = 0
PARRY_COOLDOWN_MAX = 120

boss_poz = [700, VISINA//2]
boss_radius = 45
boss_hp = 200
boss_hitrost = 2

metki = []
timer_metkov = 0
ZAMIK_STRELJANJA = 10

zombiji = []
timer_zombijev = 0

granate = []

lightning_zones = []
lightning_hits = []
shockwaves = []

game_over = False
zmagovalec = ""

igralec_speedx = 0
igralec_speedy = 0

tece = True

while tece:

    zaslon.fill((20,20,20))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            tece = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                tece = False

            if (event.key == pygame.K_n) or (event.key == pygame.K_q):
                if not parry_aktiven and parry_cooldown <= 0:
                    parry_aktiven = True
                    parry_timer = PARRY_TRAJANJE
                    parry_cooldown = PARRY_COOLDOWN_MAX

            if (event.key == pygame.K_m) or (event.key == pygame.K_e):

                smerx = 0
                smery = 0

                if igralec_speedx > 0:
                    smerx = 1
                elif igralec_speedx < 0:
                    smerx = -1

                if igralec_speedy > 0:
                    smery = 1
                elif igralec_speedy < 0:
                    smery = -1

                granate.append({
                    "x": igralec_poz[0] + smerx * 90,
                    "y": igralec_poz[1] + smery * 90,
                    "timer": 60
                })

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

    igralec_poz[0] = max(0, min(SIRINA, igralec_poz[0]))
    igralec_poz[1] = max(0, min(VISINA, igralec_poz[1]))

    if parry_aktiven:

        parry_timer -= 1

        if parry_timer <= 0:
            parry_aktiven = False

    if parry_cooldown > 0:
        parry_cooldown -= 1

    timer_metkov += 1

    if timer_metkov >= ZAMIK_STRELJANJA and not parry_aktiven:

        mx, my = pygame.mouse.get_pos()

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

    for metek in metki[:]:

        metek["x"] += metek["dx"] * 14
        metek["y"] += metek["dy"] * 14

        if (
            metek["x"] < 0 or
            metek["x"] > SIRINA or
            metek["y"] < 0 or
            metek["y"] > VISINA
        ):
            metki.remove(metek)
            continue

        razdalja = math.hypot(
            metek["x"]-boss_poz[0],
            metek["y"]-boss_poz[1]
        )

        if razdalja < boss_radius:

            boss_hp -= 2

            shockwaves.append({
                "x": metek["x"],
                "y": metek["y"],
                "radius": 10,
                "max": 60
            })

            metki.remove(metek)
            continue

        for zombi in zombiji[:]:

            razdalja_z = math.hypot(
                metek["x"]-zombi[0],
                metek["y"]-zombi[1]
            )

            if razdalja_z < 20:

                shockwaves.append({
                    "x": metek["x"],
                    "y": metek["y"],
                    "radius": 10,
                    "max": 40
                })

                zombiji.remove(zombi)

                if metek in metki:
                    metki.remove(metek)

                break

    if boss_poz[1] < igralec_poz[1]:
        boss_poz[1] += boss_hitrost

    elif boss_poz[1] > igralec_poz[1]:
        boss_poz[1] -= boss_hitrost

    if random.randint(1,120) == 1:

        lightning_zones.append({
            "x": random.randint(100,800),
            "y": random.randint(100,500),
            "timer": 120,
            "radius": 80
        })

    for zone in lightning_zones[:]:

        zone["timer"] -= 1

        pygame.draw.circle(
            zaslon,
            RDECA,
            (int(zone["x"]), int(zone["y"])),
            zone["radius"],
            5
        )

        if zone["timer"] <= 0:

            lightning_hits.append({
                "x": zone["x"],
                "y": zone["y"],
                "timer": 15,
                "shock": 20
            })

            razdalja = math.hypot(
                igralec_poz[0]-zone["x"],
                igralec_poz[1]-zone["y"]
            )

            if razdalja < zone["radius"]:

                if not parry_aktiven:
                    igralec_hp -= 20

            lightning_zones.remove(zone)

    for hit in lightning_hits[:]:

        for i in range(20):

            offsetx = random.randint(-25,25)

            pygame.draw.line(
                zaslon,
                STRELA,
                (
                    int(hit["x"] + offsetx),
                    0
                ),
                (
                    int(hit["x"]),
                    int(hit["y"])
                ),
                random.randint(2,5)
            )

        pygame.draw.circle(
            zaslon,
            STRELA,
            (int(hit["x"]), int(hit["y"])),
            int(hit["shock"]),
            5
        )

        pygame.draw.circle(
            zaslon,
            BELA,
            (int(hit["x"]), int(hit["y"])),
            int(hit["shock"] // 2),
            3
        )

        hit["shock"] += 10
        hit["timer"] -= 1

        if hit["timer"] <= 0:
            lightning_hits.remove(hit)

    timer_zombijev += 1

    if timer_zombijev >= 45:

        stran = random.randint(1,4)

        if stran == 1:
            zx = random.randint(0, SIRINA)
            zy = -30

        elif stran == 2:
            zx = random.randint(0, SIRINA)
            zy = VISINA + 30

        elif stran == 3:
            zx = -30
            zy = random.randint(0, VISINA)

        else:
            zx = SIRINA + 30
            zy = random.randint(0, VISINA)

        zombiji.append([zx, zy])

        timer_zombijev = 0

    for zombi in zombiji[:]:

        dx = igralec_poz[0] - zombi[0]
        dy = igralec_poz[1] - zombi[1]

        razdalja = math.hypot(dx,dy)

        if razdalja != 0:

            zombi[0] += dx/razdalja * random.uniform(1.8,3.4)
            zombi[1] += dy/razdalja * random.uniform(1.8,3.4)

        if razdalja < igralec_radius + 15:

            if not parry_aktiven:
                igralec_hp -= 1

    for granata in granate[:]:

        granata["timer"] -= 1

        pygame.draw.circle(
            zaslon,
            VIJOLICNA,
            (int(granata["x"]), int(granata["y"])),
            20
        )

        if granata["timer"] <= 0:

            shockwaves.append({
                "x": granata["x"],
                "y": granata["y"],
                "radius": 20,
                "max": 140
            })

            for zombi in zombiji[:]:

                razdalja = math.hypot(
                    granata["x"]-zombi[0],
                    granata["y"]-zombi[1]
                )

                if razdalja < 100:
                    zombiji.remove(zombi)

            razdalja_boss = math.hypot(
                granata["x"]-boss_poz[0],
                granata["y"]-boss_poz[1]
            )

            if razdalja_boss < 100:
                boss_hp -= 20

            granate.remove(granata)

    for shock in shockwaves[:]:

        pygame.draw.circle(
            zaslon,
            STRELA,
            (int(shock["x"]), int(shock["y"])),
            int(shock["radius"]),
            4
        )

        shock["radius"] += 6

        if shock["radius"] >= shock["max"]:
            shockwaves.remove(shock)

    pygame.draw.circle(
        zaslon,
        MODRA,
        (int(igralec_poz[0]), int(igralec_poz[1])),
        igralec_radius
    )

    if parry_aktiven:

        pygame.draw.circle(
            zaslon,
            SVETLO_MODRA,
            (int(igralec_poz[0]), int(igralec_poz[1])),
            igralec_radius+10,
            4
        )

    pygame.draw.circle(
        zaslon,
        RDECA,
        (int(boss_poz[0]), int(boss_poz[1])),
        boss_radius
    )

    for zombi in zombiji:

        pygame.draw.circle(
            zaslon,
            ZELENA,
            (int(zombi[0]), int(zombi[1])),
            15
        )

    for metek in metki:

        pygame.draw.circle(
            zaslon,
            ORANZNA,
            (int(metek["x"]), int(metek["y"])),
            6
        )

        pygame.draw.circle(
            zaslon,
            RUMENA,
            (int(metek["x"]), int(metek["y"])),
            3
        )

    pygame.draw.rect(
        zaslon,
        RDECA,
        (20,20,200,20)
    )

    pygame.draw.rect(
        zaslon,
        ZELENA,
        (20,20,max(0,igralec_hp)*2,20)
    )

    pygame.draw.rect(
        zaslon,
        RDECA,
        (SIRINA-420,20,400,20)
    )

    pygame.draw.rect(
        zaslon,
        ZELENA,
        (SIRINA-420,20,max(0,boss_hp)*2,20)
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

    zaslon.blit(igralec_text, (80,45))
    zaslon.blit(boss_text, (SIRINA-250,45))

    if igralec_hp <= 0:

        game_over = True
        zmagovalec = "BOSS WINS"

    if boss_hp <= 0:

        game_over = True
        zmagovalec = "YOU WIN"

    if game_over:

        zaslon.fill(CRNA)

        barva = RDECA if "BOSS" in zmagovalec else ZELENA

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