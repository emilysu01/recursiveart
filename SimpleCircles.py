import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 700
HEIGHT= 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Recursive Circles')

pygame.init()

def drawCircles (screen, BLACK, x, y, r, thickness):
    pygame.draw.circle (screen, BLACK, (x, y), r, 1)
    if r > 2:
        r = int (r * 0.75)
        drawCircles (screen, BLACK, x, y, r, thickness)

def main():
    screen.fill(WHITE)
    drawCircles(screen, BLACK, 350, 250, 350, 1)
    pygame.display.update()

inPlay = True
print "Hit ESC to end the program."

while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    main()
    pygame.time.delay(2)                                      
if inPlay==False: 
    pygame.quit()