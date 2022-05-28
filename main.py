from datetime import MAXYEAR
import pygame, random, time
from pygame.locals import *

(WIDTH, HEIGHT) = (800, 600)

#   Egg    
#   Random x co-ordinate for egg
eggX = random.randrange(20, 760, 20)
eggY = 0
eggImg = pygame.image.load('images/egg.png')

score = 0

#   Animation
countRate = pygame.time.Clock()
fps = 30
def createWindow(width, height):
    global win
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Catch Egg")

def toTheTop():
    global eggX, eggY
    eggX = random.randrange(20, 760, 20)
    eggY = 0
    
        
basketImg_notScaled = pygame.image.load('images/basket.png')
basketImg_scaled = pygame.transform.scale(basketImg_notScaled, (64, 64))

createWindow(WIDTH, HEIGHT)
running = True
while (running):
    #   Get mouse postion as a tuple
    mx, my = pygame.mouse.get_pos()
    my = 500
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    win.fill((0, 0, 0))
    #   Throw image onto screen
    win.blit(basketImg_scaled, (mx, 500))
    win.blit(eggImg, (eggX, eggY))
    eggY += 5

    if (mx-5<eggX and eggX<mx+32 and my<eggY and eggY<my+20):
        score += 1
        print('Score '+ str(score))
        toTheTop()
        
    
    
    if (eggY >= HEIGHT):
        toTheTop()
    pygame.display.update()
    countRate.tick(fps)