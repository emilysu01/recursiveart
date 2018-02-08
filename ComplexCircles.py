import pygame, sys
from pygame.locals import *

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
PINK = (245, 54, 188)
BLACK = (0,0,0)

WIDTH = 700
HEIGHT= 500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Recursive Rectangles')

screen.fill(WHITE)

pygame.init()

def recursive_draw (screen, BLACK, x, y, r, thickness):
    if r > 2:
        pygame.draw.circle (screen, BLACK, (x, y), r, 1)
        r = int (r * 0.3)
        recursive_draw (screen, BLACK, x, y + r, r, thickness)
        recursive_draw (screen, BLACK, x, y - r, r, thickness)
        recursive_draw (screen, BLACK, x - r, y, r, thickness)
        recursive_draw (screen, BLACK, x + r, y, r, thickness)

def main():
    recursive_draw(screen, BLACK, 350, 250, 350, 1)
    pygame.display.update()

inPlay = True
print "Hit ESC to end the program."

while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    main()
    pygame.time.delay(2)                                     