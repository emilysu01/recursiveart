import pygame, sys, math, random
from pygame.locals import *

black = (  0,  0,    0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

def recursive_fractal(screen, x,y,width,height,fractal):
    #define x1, y1, x2, y2
    x1 = x + width//4
    y1 = y + height//2
    x2 = x + 3*width//4
    y2 = y + height//2
    pygame.draw.line(screen, blue, (x1, y1), (x2, y2), 1)  #middle line
    
    #define x3, y3, x4, y4
    x3 = x1
    y3 = y + height//4
    x4 = x1
    y4 = y + 3*height//4
    pygame.draw.line(screen, red, (x3, y3), (x4, y4), 1)  #left line

    #define x5, y5, x6, y6
    x5 = x + 3*width//4
    y5 = y3
    x6 = x5
    y6 = y4
    pygame.draw.line(screen, black, (x5, y5), (x6, y6), 1)  #left line

    if fractal>0:
        #recursive calls go here
        fractal = fractal - 1
        recursive_fractal(screen, x, y, width//2, height//2,fractal)
        recursive_fractal(screen, x, y + width//2, width//2, height//2,fractal)
        recursive_fractal(screen, x + width//2, y, width//2, height//2,fractal)
        recursive_fractal(screen, x + width//2, y + width//2, width//2, height//2,fractal)
    pygame.display.update()

        

def main():
    pygame.init()
    #set screen size
    size = (700,700)
    screen = pygame.display.set_mode(size)
    
  
    screen.fill(white)
    
    fractal_level = 5
    recursive_fractal(screen, 0, 0, 700, 700, fractal_level)
    #redraws screen
    pygame.display.update()
   
    #deals with quitting the program
    while True:
        for event in pygame.event.get():
         if event.type == QUIT:
             sys.exit()

 #runs the program
if __name__ == '__main__':
    main()