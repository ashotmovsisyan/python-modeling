import pygame
import math 

pygame.init()

screen_width = 1200
screen_height = 700
width, height = 50, 50


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
v_x, v_y, w = -9, -9, 0
x, y = screen_width-width / 2, screen_height-height / 2
# x, y = 0, 0
# x, y = width / 2, height / 2
angle = 0  # degrees

# Step 1: Create a transparent surface
rect_surf = pygame.Surface((width, height), pygame.SRCALPHA) # chatgpt
pygame.draw.rect(rect_surf, (0, 128, 255), (0, 0, width, height))

screen.fill((255, 255, 255))

def draw(x,y,angle):

    # Step 2: Rotate the surface

    rotated_surf = pygame.transform.rotate(rect_surf, angle)

    # Step 3: Get the new rect and center it
    rotated_rect = rotated_surf.get_rect(center=(x, y))

    # Step 4: Blit to screen
    # screen.fill((255, 255, 255))
    screen.blit(rotated_surf, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(30)  # 60 FPS

def move(x,y,angle):
    global v_y, v_x
    x += v_x
    y += v_y

    v_y += 0.5
    # v_x += 0.5
    angle += w  

    return clash(x,y,angle)

def clash(x,y,angle):
    global v_x
    global v_y

    if x + width / 2 >= screen_width or x < width / 2:
        v_x = -v_x

    if y + height / 2 >= screen_height or y < height / 2:
        if y > screen_height-height / 2: 
            y = 2 * (screen_height-height/2) - y

        if y < height / 2:
            y = height - y

        v_y = -v_y
    
    return x,y,angle

for i in range(1000):
    x, y, angle = move(x,y,angle)

    draw(x,y,angle)

pygame.quit()
