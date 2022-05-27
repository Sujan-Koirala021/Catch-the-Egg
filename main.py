import pygame
from pygame.locals import *

(WIDTH, HEIGHT) = (800, 600)

def createWindow(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Catch Egg")

createWindow(WIDTH, HEIGHT)
running = True
while (running):
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()