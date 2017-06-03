#file that holds all the classes

#import modules
import pygame

#variables
worldScroll = 0

#define classes
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bario.png')
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = 400
        self.moved = 0

    def move(self, leftRight):
        if leftRight == 2:
            self.moved -= 5
        if leftRight == 1:
            self.moved += 5

#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, xPos):
        super().__init__()
        self.image = pygame.image.load('assets/boomba.png')
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = 400
        self.movex = 0
        self.speed = 3

    def moveleft(self):
        self.movex -= self.speed

    def posUpdate(self, worldScroll):
        self.rect.x = worldScroll + self.movex

    def update(self, worldScroll):
        #self.moveleft()
        self.posUpdate(worldScroll)
        if self.rect.x == -300:
            self.kill()

#pause screen
#class pause_screen
