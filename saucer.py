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

# Boolean Stuff
done = False
keyPressed = False
menuScreen = False
whichButton = 1
keyDown = False
creditScreen = False
#MOVED BOOLEAN STUFF UP HERE

# Sprite Thing
class Play(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/presskey.png')
       self.rect = self.image.get_rect()
       self.rect.x = 340
       self.rect.y = 400

class MainMenuBG(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/nohighscore.png')
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 350

class MainMenuArrows(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/nohighscore.png')
       self.rect = self.image.get_rect()
       self.rect.x = 462
       self.rect.y = 350

    def update(self, whichButton):
       if whichButton % 4 == 0:
            self.image = pygame.image.load('assets/text/playarrow.png')
       elif whichButton % 4 == 1:
            self.image = pygame.image.load('assets/text/instructionarrow.png')
       elif whichButton % 4 == 2:
            self.image = pygame.image.load('assets/text/creditsarrow.png')
       elif whichButton % 4 == 3:
            self.image = pygame.image.load('assets/text/exitarrow.png')
            
class MainMenu ():
    def __init__(self):
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if keyPressed == False:
                if event.type == pygame.KEYDOWN:
                    keyPressed = True
                    menuScreen = True
            if menuScreen:
                pygame.draw.rect(screen,sky,[340,400,615,25],0)
                if event.type == pygame.KEYDOWN:
                    if keyDown == False:
                        if event.key == pygame.K_DOWN:
                            whichButton += 1
                            keyDown = True
                        if event.key == pygame.K_UP:
                            whichButton -= 1
                            keyDown = True
                        if event.key == pygame.K_RETURN and whichButton % 4 == 3:
                            done = True
                        if event.key == pygame.K_RETURN and whichButton % 4 == 2:
                            mainScreen = False
                            creditScreen = True
                if event.type == pygame.KEYUP:
                    keyDown = False
                menu.update(whichButton)
                menu.draw(screen)
            else:
                playGroup.draw(screen)
            pygame.display.flip()
            screen.blit(bg, [0, 0])
            clock.tick(60)

mainMenu = MainMenu() #I ADDED THIS THINGY IS THIS RIGHT            
mainMenuArrows = MainMenuArrows()
mainMenuBG = MainMenuBG()
play = Play()

playGroup = pygame.sprite.GroupSingle() #group
menu = pygame.sprite.Group() #group
menu.add(mainMenuBG) #menu bg
menu.add(mainMenuArrows) #arrows
menu.add(mainMenu) #I ADDED THIS TO THE MENU GROUP PLS TO CHECK
playGroup.add(play) #press any key

# Set a Background
bg = pygame.image.load ('assets/mainmenu.png')

# Display Graphics
pygame.display.flip()

# Game Loop
#HOW DO I CALL THE MAIN MENU THING
pygame.quit()
