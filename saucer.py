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
class Text1(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('text1.png')
       self.rect = self.image.get_rect()
       self.rect.x = 325
       self.rect.y = 400
       
text1 = Text1()

# Set a Background
bg = pygame.image.load ('mainmenu.png')

# Display Text
screen.blit (bg,[0,0],None,0)
screen.blit (text1.image, text1.rect,None,0)

# Display Graphics
pygame.display.flip()

# Flashing Text
frame = 0

# Closing the Program
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True        
    clock.tick(60)
pygame.quit()
