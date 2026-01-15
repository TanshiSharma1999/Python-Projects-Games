import pgzrun
import pygame
import math

WIDTH = 500
HEIGHT = 500

t = 0


def heartbeat(x):
    x = x % 1.0
    return (
        math.exp(-((x - 0.15) ** 2) * 90) +
        0.6 * math.exp(-((x - 0.35) ** 2) * 140)
    )


def heart_points(cx, cy, size, scale):
    points = []
    for i in range(0, 360, 5):
        a = math.radians(i)

        x = 16 * math.sin(a) ** 3
        y = (
            13 * math.cos(a)
            - 5 * math.cos(2 * a)
            - 2 * math.cos(3 * a)
            - math.cos(4 * a)
        )

        px = int(cx + x * size * scale)
        py = int(cy - y * size * scale)
        points.append((px, py))

    return points


def update():
    global t
    t += 0.01


def draw():
    screen.clear()

    beat = heartbeat(t)
    scale = 1 + beat * 0.18

    cx = WIDTH // 2
    cy = HEIGHT // 2 + 20

    heart_color = (
        int(210 + beat * 30),
        int(70 + beat * 20),
        int(100 + beat * 20),
    )

    # Glow layers
    for i in range(4, 0, -1):
        glow_scale = scale + i * 0.05
        glow_color = (
            min(255, heart_color[0] + i * 12),
            min(255, heart_color[1] + i * 6),
            min(255, heart_color[2] + i * 6),
        )

        pts = heart_points(cx, cy, 4, glow_scale)
        pygame.draw.polygon(screen.surface, glow_color, pts)

    # Main heart
    pts = heart_points(cx, cy, 4, scale)
    pygame.draw.polygon(screen.surface, heart_color, pts)

    # 💕 Title text
    screen.draw.text(
        "Happy Valentine's Day",
        center=(WIDTH // 2, 40),
        fontsize=40,
        color=(255, 120, 160),
        shadow=(2, 2),
        scolor=(150, 50, 80)
    )

    # 💌 Subtitle text
    screen.draw.text(
        "with love - Tanshi",
        center=(WIDTH // 2, HEIGHT - 30),
        fontsize=30,
        color=(255, 180, 200)
    )


pgzrun.go()
