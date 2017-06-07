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

# Background
screen = pygame.image.load('assets/mainmenu.png')

# Clock
clock = pygame.time.Clock()

# Sprite Thing
class StartUp(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/presskey.png')
       self.rect = self.image.get_rect()
       self.rect.x = 325
       self.rect.y = 400
        
startUp = StartUp()

# Add startup to group
sprite_list = pygame.sprite.Group()
sprite_list.add(startUp)

# Display Text
sprite_list.draw(screen)

# Display Graphics
pygame.display.flip()

# Closing the Program
done = False
keyPressed = False
mainMenu = True
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if keyPressed == False:
        if event.type == pygame.KEYDOWN:
            keyPressed = True
    clock.tick(60)
pygame.quit()
