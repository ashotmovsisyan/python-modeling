import pygame
import random
import math

pygame.init()

screen_width = 1200
screen_height = 700
width, height = 50, 50
n = 10
g = 0.5


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# v_x, v_y, w = -9, -9, 0
# v_x2, v_y2, w2 = -12, -15, 0
# x, y = screen_width-width / 2, screen_height-height / 2
x = []
y = []
v_x = []
v_y = []
w = 0
angle = []

# x, y = 0, 0
# x, y = width / 2, height / 2
# angle = 0  # degrees
# angle2 = 0  # degrees

# Step 1: Create a transparent surface
rect_surf = pygame.Surface((width, height), pygame.SRCALPHA)  # chatgpt
pygame.draw.rect(rect_surf, (0, 128, 255), (0, 0, width, height))

screen.fill((255, 255, 255))


def draw(x, y, angle):

    # Step 2: Rotate the surface

    rotated_surf = pygame.transform.rotate(rect_surf, angle)

    # Step 3: Get the new rect and center it
    rotated_rect = rotated_surf.get_rect(center=(x, y))

    # Step 4: Blit to screen
    screen.blit(rotated_surf, rotated_rect.topleft)

    pygame.display.flip()


def move(x, v_x, y, v_y, angle):
    x += v_x
    y += v_y

    v_y += g
    # v_x +=g
    angle += w

    return clash(x, v_x, y, v_y, angle)


def sign(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


def clash(x, v_x, y, v_y, angle):
    delta = 0

    if x + width / 2 >= screen_width or x < width / 2:
        v_x = -v_x

    if y + height / 2 >= screen_height or y < height / 2:

        if y > screen_height - height / 2:
            delta = 2 * (y - screen_height + height / 2)
            v_y = -sign(v_y) * math.sqrt(v_y**2 - sign(v_y) * 2 * delta * g)
            # y = 2 * (screen_height-height/2) - y
            y = screen_height - height / 2 - delta

        if y < height / 2:
            delta = height - 2 * y
            v_y = -sign(v_y) * math.sqrt(v_y**2 - sign(v_y) * 2 * delta * g)
            y = height - y

    return x, v_x, y, v_y, angle



for index in range(n):
    x.insert(index, random.uniform(0 + width / 2, screen_width - width / 2))
    y.insert(index, random.uniform(0 + height / 2, screen_height - height / 2))
    v_x.insert(index, random.uniform(-15, 15))
    v_y.insert(index, random.uniform(-15, 15))
    angle.insert(index, 0)

# print('x', x)
# print('y', y)
# print('v_x', v_x)
# print('v_y', v_y)

for i in range(1000):
    screen.fill((255, 255, 255))

    for index in range(n):
        x[index], v_x[index], y[index], v_y[index], angle[index] = move(x[index], v_x[index], y[index], v_y[index], angle[index])
        draw(x[index], y[index], angle[index])

    clock.tick(30)  # 60 FPS


pygame.quit()
