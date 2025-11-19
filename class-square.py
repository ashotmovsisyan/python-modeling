import pygame
import random
import math
import time

pygame.init()

screen_width = 1200
screen_height = 700
width, height = 5, 5
n = 0
g = -50
w = 0

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

pygame.display.update()

clock = pygame.time.Clock()

rect_surf = pygame.Surface((width, height), pygame.SRCALPHA)  # chatgpt
pygame.draw.rect(rect_surf, (0, 128, 255), (0, 0, width, height))


def sign(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


class Square:
    def __init__(self, m, x, y, v_x, v_y, angle):
        self.m = m
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.angle = angle

    def print(self):
        print(f"({self.x}, {self.y})")

    def move(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt + g / 2 * dt ** 2

        self.v_y += g * dt
        # v_x +=g
        self.angle += w * dt

        delta = 0

        if self.x + width / 2 >= screen_width or self.x < width / 2:
            self.v_x = -self.v_x

        if self.y + height / 2 >= screen_height or self.y < height / 2:

            if self.y > screen_height - height / 2:
                delta = 2 * (self.y - screen_height + height / 2)
                self.v_y = -sign(self.v_y) * math.sqrt(self.v_y ** 2 - sign(self.v_y) * 2 * delta * g)
                # y = 2 * (screen_height-height/2) - y
                self.y = screen_height - height / 2 - delta

            if self.y < height / 2:
                delta = height - 2 * self.y
                self.v_y = -sign(self.v_y) * math.sqrt(self.v_y ** 2 - sign(self.v_y) * 2 * delta * g)
                self.y = height - self.y

    def draw(self):
        rotated_surf = pygame.transform.rotate(rect_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(self.x, screen_height - self.y))
        screen.blit(rotated_surf, rotated_rect.topleft)

    def energy(self):
        return (self.v_x ** 2 + self.v_y ** 2) / 2 - self.y * g


class Spring:
    def __init__(self, k, x1, y1, x2, y2, width):
        self.k = k
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width

    def draw(self):
        prev_x = None
        prev_y = None

        alpha = math.atan((self.x1 - self.x2) / (self.y1 - self.y2))

        for index in range(2 * self.k + 2):
            i = int(index / 2)
            x_c = self.x1 + (self.x2 - self.x1) * i / self.k
            y_c = self.y1 - (self.y2 - self.y1) * i / self.k

            even = 1 if index % 2 == 0 else -1
            x = x_c - self.width / 2 * math.cos(alpha) * even
            y = y_c - self.width / 2 * math.sin(alpha) * even

            if prev_x is not None or prev_y is not None:
                pygame.draw.line(screen, (0, 0, 0), (prev_x, prev_y), (x, y), 1)

            prev_x, prev_y = x, y
            pass


spring = Spring(2, 500, 500, 500, 0, 100)

spring.draw()

pygame.display.flip()

# squares = []
#
# for i in range(n):
#     squares.insert(
#         n,
#         Square(
#             1,
#             random.uniform(0 + width / 2, screen_width - width / 2),
#             random.uniform(0 + height / 2, screen_height - height / 2),
#             random.uniform(-100, 100),
#             random.uniform(-100, 100),
#             0,
#         ),
#     )
#
#
#
# start_time = time.time()
# prev_time = start_time
#
# while prev_time - start_time < 10:
#     current_time = time.time()
#
#     deltaT = current_time - prev_time
#
#     total_energy = 0
#
#     for i in range(len(squares)):
#         squares[i].move(deltaT)
#         squares[i].draw()
#         total_energy += squares[i].energy()
#
#     pygame.display.flip()
#
#     print(f"FPS: {current_time - start_time} {total_energy}")
#
#     clock.tick(30)
#
#     prev_time = current_time

time.sleep(3)

pygame.quit()
