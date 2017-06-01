#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-06-01
#last edit(TEQ8601 time format): 210-1067

#import necessary modules
import pygame

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
ORANGE =  (255, 127, 0)


#define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bario.png')
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.x = 650
        self.rect.y = 400

    def move(self, leftRight):
        if leftRight == 1:
            self.rect.x -= 5
        if leftRight == 2:
            self.rect.x += 5

#initialize game engine
pygame.init()

#set screen
size = (1300, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#create sprite list object
sprite_list = pygame.sprite.Group()

#create player object
player = Player()

#add objects to lists
sprite_list.add(player)

#initialize clock
clock = pygame.time.Clock()

#initialize necessary variables
kLeft = False
kRight = False

leftRight = 0

kLeftTemp1 = False
kRightTemp1 = False

kLeftTemp2 = False
kRightTemp2 = False

#loop until user clicks close button
done = False

while done == False:
    #event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if not hasattr(event, 'key'): continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                kLeft = True
                kLeftTemp1 = True
            elif event.key == pygame.K_RIGHT:
                kRight = True
                kRightTemp1 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kLeft = False
                kLeftTemp2 = True
            elif event.key == pygame.K_RIGHT:
                kRight = False
                kRightTemp2 = True

    #game logic
    if kLeftTemp1 or kRightTemp2:
        leftRight = 1
    if kRightTemp1 or kLeftTemp2:
        leftRight = 2
    if not(kLeft or kRight):
        leftRight = 0

    if kLeft or kRight:
        player.move(leftRight)

    kLeftTemp1 = False
    kRightTemp1 = False

    kLeftTemp2 = False
    kRightTemp2 = False

    #graphics
    sprite_list.draw(screen)
    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(60)
pygame.quit()
