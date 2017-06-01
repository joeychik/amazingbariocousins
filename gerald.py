#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-06-01
#last edit(TEQ8601 time format): 2010-1067

#import necessary modules
import pygame

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


#define classes

worldScroll = 0

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, xPos):
        super().__init__()
        self.image = pygame.image.load('assets/boomba.png')
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = 400
        self.movex = 0

    def moveleft(self):
        self.movex -= 3

    def posUpdate(self, worldScroll):
        self.rect.x = worldScroll + self.movex

    def update(self, worldScroll):
        #self.moveleft()
        self.posUpdate(worldScroll)
        if self.rect.x == -150:
            self.kill()

#initialize game engine
pygame.init()

#set screen
size = (1300, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#create sprite list object
sprite_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

#create player object
player = Player()
sprite_list.add(player)

#create enemy objects
enemy = Enemy(900)
sprite_list.add(enemy)
enemy_list.add(enemy)

#initialize clock
clock = pygame.time.Clock()

#initialize necessary variables
kLeft = False
kRight = False
kUp = False

leftRight = 0

kLeftTemp1 = False
kRightTemp1 = False
kUpTemp1 = False

kLeftTemp2 = False
kRightTemp2 = False
kUpTemp2 = False

#loop until user clicks close button
done = False

while done == False:
    #event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if not hasattr(event, 'key'): continue
        #the kXXXTemp variables represent the key being pressed and released
        #the kXXX variables will stay true as long as the key is being held down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                kLeft = True
                kLeftTemp1 = True
            if event.key == pygame.K_RIGHT:
                kRight = True
                kRightTemp1 = True
            if event.key == pygame.K_UP:
                kUp = True
                kUpTemp1 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kLeft = False
                kLeftTemp2 = True
            if event.key == pygame.K_RIGHT:
                kRight = False
                kRightTemp2 = True
            if event.key == pygame.K_UP:
                kUp = False
                kUpTemp2 = False

    #game logic
    #where everything should be relative to the player
    worldScroll = player.moved

    if kLeftTemp1 or kRightTemp2:
        leftRight = 1
    if kRightTemp1 or kLeftTemp2:
        leftRight = 2
    if not(kLeft or kRight):
        leftRight = 0

    if kLeft or kRight:
        player.move(leftRight)

    #update position of everything that moved
    enemy_list.update(worldScroll)

    #reset temporary variables
    kLeftTemp1 = False
    kRightTemp1 = False

    kLeftTemp2 = False
    kRightTemp2 = False

    #graphics
    screen.fill(LIGHT_BLUE)
    sprite_list.draw(screen)

    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(60)
pygame.quit()
