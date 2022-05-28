import pygame
from pygame.locals import *

(WIDTH, HEIGHT) = (800, 600)

def createWindow(width, height):
    global win
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Catch Egg")

basketImg_notScaled = pygame.image.load('basket.png')
baseketImg_scaled = pygame.transform.scale(basketImg_notScaled, (64, 64))

createWindow(WIDTH, HEIGHT)
running = True
while (running):
    #   Get mouse postion as a tuple
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    win.fill((0, 0, 0))
    #   Throw image onto screen
    win.blit(baseketImg_scaled, (mx-32, 500))

    pygame.display.update()