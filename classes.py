#file that holds all the classes

#import modules
import pygame

#variables
worldScroll = 0

#create sprite list object
sprite_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()

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
        self.leftRight = 0
        self.jumping = False
        self.runCycleRight = 0
        self.runCycleLeft = 0
        self.falling = False
        self.midair = False

    def move(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2):
        if self.moved <= 0:
            if kLeftTemp1 or kRightTemp2:
                self.leftRight = 1
            if kRightTemp1 or kLeftTemp2:
                self.leftRight = 2
            if not(kLeft or kRight):
                self.leftRight = 0
            if self.leftRight == 2:
                if self.runCycleRight <= 9:
                    self.runCycleRight += 1
                else:
                    self.runCycleRight = 1
                if 1 <= self.runCycleRight <= 5:
                    self.image = pygame.image.load('assets/bariowalk1.png')
                elif 6 <= self.runCycleRight <= 10:
                    self.image = pygame.image.load('assets/bariowalk2.png')
                if self.moved == 0:
                    self.image = pygame.image.load('assets/barioflip.png')
                self.moved -= 10
            if self.leftRight == 1:
                if self.runCycleLeft <= 9:
                    self.runCycleLeft += 1
                else:
                    self.runCycleLeft = 1
                if 1 <= self.runCycleLeft <= 5:
                    self.image = pygame.image.load('assets/barioflipwalk1.png')
                elif 6 <= self.runCycleLeft <= 10:
                    self.image = pygame.image.load('assets/barioflipwalk2.png')
                if self.moved == 0:
                    self.image = pygame.image.load('assets/barioflip.png')
                self.moved += 10
        if self.moved >= 0:
            self.moved = 0

    def standSprite(self):
        if self.leftRight == 1:
            self.image = pygame.image.load('assets/barioflip.png')
        elif self.leftRight == 2:
            self.image = pygame.image.load('assets/bario.png')
        self.runCycleRight = 0
        self.runCycleLeft = 0

    def jump(self, kUp):
        if self.rect.y <= 100:
            self.falling = True
        if kUp and not self.falling:
            self.rect.y -= 10
        if not kUp:
            self.falling = True
        if self.rect.y >= 400:
            self.falling = False
        if self.falling:
            self.rect.y += 10
        if self.rect.y < 400:
            self.standSprite()
            self.midair = True


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
        self.moveleft()
        self.posUpdate(worldScroll)
        if self.rect.x == -300:
            self.kill()


#level platform sprite
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bricktemplate.png')
        self.rect = self.image.get_rect()
        self.rect.x = -800
        self.rect.y = 528

    def spawnNew(self):
        if self.rect.x < -1600:
            platform = Platform()
            obstacle_list.add(platform)
            sprite_list.add(platform)
            self.kill()

    def update(self, worldScroll):
        self.rect.x = worldScroll - 800
        self.spawnNew()


#pause screen
class Pause_screen():
    def __init__(self):
        self.image = pygame.image.load('assets/pause.png')
        self.runLoop = True
        screen.blit(self.image, [0, 0])
        while self.runLoop:
            for event in pygame.event.get():
                if not event.type  == pygame.KEYDOWN: continue
                if event.key == pygame.K_p: self.runLoop = False
