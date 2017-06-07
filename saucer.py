# Main Menu
# Jason Yeung
# 2017-06-02

import random
import pygame

# Setup
import pygame
pygame.init()

# Set Colour Variables
white = (255,255,255)
red = (255,0,0)
sky = (146,144,255)

# Set Screen
size = (1300,700)
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Sprite Thing
class StartUp(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/presskey.png')
       self.rect = self.image.get_rect()
       self.rect.x = 340
       self.rect.y = 400

class MainMenu(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/nohighscore.png')
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 350

class Play(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/play.png')
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 350

    def changeArrow(self, whichButton):
        if whichButton == 1:
            self.image = pygame.image.load('assets/text/playarrow.png')
        elif whichButton == 2:
            self.image = pygame.image.load('assets/text/instructionarrow.png')
        elif whichButton == 3:
            self.image = pygame.image.load('assets/text/creditsarrow.png')
        elif whichButton == 4:
            self.image = pygame.image.load('assets/text/exitarrow.png')

'''
class Instructions(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/instructions.png')
       self.rect = self.image.get_rect()
       self.rect.x = 462
       self.rect.y = 394

class Credits(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/credits.png')
       self.rect = self.image.get_rect()
       self.rect.x = 523
       self.rect.y = 438

class Exit(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/exit.png')
       self.rect = self.image.get_rect()
       self.rect.x = 559
       self.rect.y = 483
'''
       
startUp = StartUp()
mainMenu = MainMenu()
play = Play()
'''instructions = Instructions()
creditScreen = Credits()
close = Exit()'''

spriteList = pygame.sprite.Group()
spriteList.add(play)
spriteList.add(mainMenu)

# Set a Background
bg = pygame.image.load ('assets/mainmenu.png')

# Display Text
screen.blit (bg,[0,0],None,0)
screen.blit (startUp.image, startUp.rect,None,0)

# Display Graphics
pygame.display.flip()

# Boolean Stuff
done = False
keyPressed = False
menuScreen = False
whichButton = 1

# Game Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# Start Screen
    if keyPressed == False:
        if event.type == pygame.KEYDOWN:
            keyPressed = True
            menuScreen = True

# Main Menu
    if menuScreen == True:
        pygame.draw.rect(screen,sky,[340,400,615,25],0)
        screen.blit (mainMenu.image, mainMenu.rect,None,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                whichButton += 1
        play.changeArrow(whichButton)
    spriteList.draw(screen)
    pygame.display.flip()
    screen.blit(bg, [0, 0])
    clock.tick(60)
pygame.quit()
