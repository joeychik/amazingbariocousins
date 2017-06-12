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
        self.moved = 0
        self.change_x = 0
        self.change_y = 0
        self.leftRight = 0
        self.jumping = False
        self.runCycleRight = 0
        self.runCycleLeft = 0
        self.falling = False
        self.midair = False
        self.level = None

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
                self.change_x -= 10
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
                self.change_x += 10

        hitList = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for block in hitList:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            if self.change_x < 0:
                self.rect.left = block.rect.right

        self.moved += self.change_x
        if self.moved >= 0:
            self.moved = 0

    def standSprite(self):
        if self.leftRight == 1:
            self.image = pygame.image.load('assets/barioflip.png')
        elif self.leftRight == 2:
            self.image = pygame.image.load('assets/bario.png')
        self.runCycleRight = 0
        self.runCycleLeft = 0

    def jump(self, kUp, obstacle_list):
        if self.rect.y <= 100:
            self.falling = True
        if kUp and not self.falling:
            self.change_y = -10
        if not kUp:
            self.falling = True
        if self.rect.y >= 400:
            self.falling = False
        if self.falling:
            self.change_y = 10
        hitList = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        hit = False
        for block in hitList:
            hit = True
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0
        if not hit:
            self.midair = True
        else:
            self.midair = False
        if self.midair:
            self.standSprite()

    def update(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2, kUp, obstacle_list):
        if kLeft or kRight:
            player.move(kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2)
        else:
            player.standSprite()
        self.jump(kUp, obstacle_list)

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
        """ Move the player. """
        # Gravity
        self.calc_grav()

        self.move(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2):

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.obstacleList, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def move(self, kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2):
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
            self.change_x -= 10
        if self.leftRight == 1:
            if self.runCycleLeft <= 9:
                self.runCycleLeft += 1
            else:
                self.runCycleLeft = 1
            if 1 <= self.runCycleLeft <= 5:
                self.image = pygame.image.load('assets/barioflipwalk1.png')
            elif 6 <= self.runCycleLeft <= 10:
                self.image = pygame.image.load('assets/barioflipwalk2.png')
            self.change_x += 10

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.obstacleList, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
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
def Pause_screen():
    global pause
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
    def __init__(self, player):
        self.obstacle_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.worldShift = 0
        self.levelLimit = -1000

    def update(self):
        self.obstacle_list.update()
        self.enemy_list.update()

    def draw(self):
        self.obstacle_list.draw()
        self.enemy_list.draw()

    def shiftWorld(self, shiftX):
        self.worldShift += shiftX
        for obstacle in self.obstacle_list:
            obstacle.rect.x += shiftX
        for enemy in self.enemy_list:
            enemy.rect.x += shiftX

#level 1
class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player):
        self.levelLimit = -2150
        level = [[2100, -1500],
                 [500, 800],
                 [200, 1500],
                 [800, 1900]]
        for platform in level:
            block = Platform(platform[0], platform[1])
            self.obstacle_list.add(block)

class Level_02(Level):
    def __init__(self, player):
        Level.__init__(self, player):
        self.levelLimit = -2150
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
