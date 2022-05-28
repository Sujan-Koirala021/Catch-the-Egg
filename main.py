#   Egg Rush
#   May 28, 2022


import pygame, random, time
from pygame.locals import *

(WIDTH, HEIGHT) = (768, 384)
white = (255, 255, 255)

eggIcon = pygame.image.load('images/eggIcon.png')

def createWindow(width, height):
    global win
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_icon(eggIcon)
    pygame.display.set_caption("Egg Rush")

def eggAtTop():
    global eggX, eggY
    #   Create random number ranging from 20 to 
    eggX = random.randrange(20, 740, 20)
    eggY = 0

def addText(your_text, posX, posY, text_size):
    font = pygame.font.Font('freesansbold.ttf', text_size)
    text = font.render(your_text, True, white)
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    win.blit(text, textRect)

#   Egg    
eggAtTop()
eggImg = pygame.image.load('images/egg.png')
eggVel = 10

score = 0

#   Animation
countRate = pygame.time.Clock()
fps = 30

#   BackGround Img
background = pygame.image.load('images/background.png')

#   Basket Img
basketImg_notScaled = pygame.image.load('images/basket.png')
basketImg_scaled = pygame.transform.scale(basketImg_notScaled, (64, 64))

createWindow(WIDTH, HEIGHT)
running = True
while (running):
    #   Get mouse postion as a tuple
    mx, my = pygame.mouse.get_pos()
    #   Set 'my' variable to 300 to avoid moving up and down
    my = 300
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False

    win.fill((0, 0, 0))
    
    # background image
    win.blit(background, (0, 0))
    #   Throw image onto screen
    win.blit(basketImg_scaled, (mx, 300))
    win.blit(eggImg, (eggX, eggY))
    
    #   Egg Fall
    eggY += eggVel

    #   Check for catch
    if (mx-5<eggX and eggX<mx+32 and my<eggY and eggY<my+20):
        score += 1
        eggAtTop()
        
    
    #   Egg Miss
    if (eggY >= HEIGHT):
        eggAtTop()
    
    addText(f"Score : {score}", 700, 10, 20)
    addText(f"Quit : Press 'Q'", 690, 30, 20)
    pygame.display.update()
    countRate.tick(fps)