#file that holds all the classes

#import modules
import pygame
from menuScreen import *

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (146, 144, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
ORANGE =  (255, 127, 0)

#create sprite list object
sprite_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()
playergroup = pygame.sprite.GroupSingle()

#global variables
pause = False

#define classes
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bario.png')
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = 400
        self.change_x = 0
        self.change_y = 0
        self.leftRight = 0
        self.runCycleRight = 0
        self.runCycleLeft = 0
        self.level = None

    def update(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2):
        self.calc_grav()

        self.move(kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2)

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

    def move(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2):
        if kLeftTemp1 or kRightTemp2:
            self.leftRight = 1
        if kRightTemp1 or kLeftTemp2:
            self.leftRight = 2
        self.standSprite(kRightTemp2, kLeftTemp2)
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
            self.change_x = -10
            self.rect.x += 10
        if self.leftRight == 1:
            if self.runCycleLeft <= 9:
                self.runCycleLeft += 1
            else:
                self.runCycleLeft = 1
            if 1 <= self.runCycleLeft <= 5:
                self.image = pygame.image.load('assets/barioflipwalk1.png')
            elif 6 <= self.runCycleLeft <= 10:
                self.image = pygame.image.load('assets/barioflipwalk2.png')
            self.change_x = 10
            self.rect.x -= 10
        if not(kLeft or kRight):
            self.change_x = 0
        block_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for block in block_hit_list:
            if self.change_x < 0:
                self.rect.right = block.rect.left
                self.change_x = 0
            elif self.change_x > 0:
                self.rect.left = block.rect.right
                self.change_x = 0
        if self.leftRight == 1:
            self.rect.x += 10
        if self.leftRight == 2:
            self.rect.x -= 10

    def standSprite(self, kRightTemp2, kLeftTemp2):
        if self.leftRight == 1 or (self.leftRight == 2 and kRightTemp2):
            self.image = pygame.image.load('assets/barioflip.png')
        if (self.leftRight == 2 and not kRightTemp2) or (self.leftRight == 1 and kLeftTemp2):
            self.image = pygame.image.load('assets/bario.png')

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= 700 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 700 - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.change_y = -10

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

    def update(self):
        self.moveleft()
        if self.rect.x == -300:
            self.kill()


#level platform sprite
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, x):
        super().__init__()
        self.image = pygame.Surface([width, 300])
        self.image.blit(pygame.image.load('assets/bricktemplate.png'), [0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 528

    def deSpawn(self):
        if self.rect.x < -2848:
            '''
            platform = Platform(self.startPos - 2048)
            obstacle_list.add(platform)
            sprite_list.add(platform)
            '''
            self.kill()

    def update(self):
        self.deSpawn()

#pause screen
def Pause_screen(screen, clock):
    pygame.event.clear()
    image = pygame.image.load('assets/pause.png')
    screen.blit(image, [0, 0])
    while pause:
        for event in pygame.event.get():
            if event.key == pygame.K_c or event.key == pygame.K_p: pause = False
            #if event.key == pygame.K_m:
    clock.tick(60)

#level super class
class Level():
    def __init__(self, player, screen):
        self.obstacle_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.worldShift = 0
        self.level_limit = -1000
        self.screen = screen

    def update(self, shiftX):
        self.obstacle_list.update()
        self.enemy_list.update()
        self.shiftWorld(shiftX)

    def draw(self):
        self.obstacle_list.draw(self.screen)
        self.enemy_list.draw(self.screen)

    def shiftWorld(self, shiftX):
        self.worldShift += shiftX
        for obstacle in self.obstacle_list:
            obstacle.rect.x += shiftX
        for enemy in self.enemy_list:
            enemy.rect.x += shiftX

#level 1
class Level_01(Level):
    def __init__(self, player, screen):
        Level.__init__(self, player, screen)
        self.level_limit = -2450
        level = [[2400, -1500],
                 [500, 1100],
                 [200, 1800],
                 [800, 2200]]
        for platform in level:
            block = Platform(platform[0], platform[1])
            self.obstacle_list.add(block)

class Level_02(Level):
    def __init__(self, player, screen):
        Level.__init__(self, player, screen)
        self.level_limit = -2150
        level = [[500, 800],
                 [300, 1900],
                 [200, 1500],
                 [2100, -1500]]
        for platform in level:
            block = Platform(platform[0], platform[1])
            self.obstacle_list.add(block)

#create player object
player = Player()

#create enemy objects
enemy = Enemy(900)
enemy_list.add(enemy)
