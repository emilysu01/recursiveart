import pygame, sys, math, random
from pygame.locals import *

black = (  0,  0,    0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

pygame.init()
size = (700,700)
screen = pygame.display.set_mode(size)
screen.fill(white)

def drawTriangles(screen, x, y, width, height, fractal):
    #define x1, y1, x2, y2
    x1 = x
    y1 = height
    x2 = x + width//2
    y2 = y
    x3 = width
    y3 = width
    pygame.draw.line(screen, green, (x1, y1), (x2, y2), 1)
    pygame.draw.line(screen, blue, (x2, y2), (x3, y3), 1)
    pygame.draw.line(screen, red, (x3, y3), (x1, y1), 1)
    if fractal>0:
        #recursive calls go here
        fractal = fractal - 1
        recursive_fractal(screen, x + width//4, y, width//2, height//2,fractal)
        #recursive_fractal(screen, x + 3*width//4, y + width//2, width//2, height//2,fractal)
        #recursive_fractal(screen, x + width//2, y, width//2, height//2,fractal)
        #recursive_fractal(screen, x + width//2, y, width//2, height//2,fractal)
        #recursive_fractal(screen, x + width//2, y + width//2, width//2, height//2,fractal)
    pygame.display.update()

def drawSierpinski (topx, topy, leftx, lefty, rightx, righty, fractal):
    if fractal == 0:
        return
    else:
        pygame.draw.polygon(screen, black, [[topx, topy], [leftx, lefty], [rightx, righty]], 1)
        middleTopLeftx = (topx + leftx) // 2
        middleTopLefty = (topy + lefty) // 2
        middleTopRightx = (topx + rightx) // 2
        middleTopRighty = (topy + righty) // 2
        middleLeftRightx = (leftx + rightx) // 2
        middleLeftRighty = (lefty + righty) // 2
        drawSierpinski (topx, topy, middleTopLeftx, middleTopLefty, middleTopRightx, middleTopRighty, fractal-1)
        drawSierpinski (leftx, lefty, middleTopLeftx, middleTopLefty, middleLeftRightx, middleLeftRighty, fractal-1)
        drawSierpinski (rightx, righty, middleLeftRightx, middleLeftRighty, middleTopRightx, middleLeftRighty, fractal-1)

def main():
    topx = 350
    topy = 0
    leftx = 0
    lefty = 700
    rightx = 700
    righty = 700
    fractal = 3
    drawSierpinski (topx, topy, leftx, lefty, rightx, righty, fractal)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
         if event.type == QUIT:
             sys.exit()

if __name__ == '__main__':
    main()