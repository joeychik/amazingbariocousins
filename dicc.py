#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-05-29

#import necessary modules
import pygame

#initialize game engine
pygame.init()

#set screen
size = (1300, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#initialize clock
clock = pygame.time.Clock()


#-----start of a bunch of dumbass test code shit
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill([255, 0, 0])
        self.rect = self.image.get_rect()

    def move(self, leftRight, upDown):
        if leftRight == 1:
            self.rect.x -= 5
        if leftRight == 2:
            self.rect.x += 5
        if upDown == 1:
            self.rect.y -= 5
        if upDown == 2:
            self.rect.y += 5

all_sprites_list = pygame.sprite.Group()

block1 = Block()
block1.rect.x = 50
block1.rect.y = 50
all_sprites_list.add(block1)

kLeft = False
kRight = False
kUp = False
kDown = False

leftRight = 0
upDown = 0

kLeftTemp1 = False
kRightTemp1 = False
kUpTemp1 = False
kDownTemp1 = False

kLeftTemp2 = False
kRightTemp2 = False
kUpTemp2 = False
kDownTemp2 = False
#-----end of all this dumbass test code shit


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
            elif event.key == pygame.K_UP:
                kUp = True
                kUpTemp1 = True
            elif event.key == pygame.K_DOWN:
                kDown = True
                kDownTemp1 = True
            continue
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kLeft = False
                kLeftTemp2 = True
            elif event.key == pygame.K_RIGHT:
                kRight = False
                kRightTemp2 = True
            elif event.key == pygame.K_UP:
                kUp = False
                kUpTemp2 = True
            elif event.key == pygame.K_DOWN:
                kDown = False
                kDownTemp2 = True

    #game logic
    if kLeftTemp1 or kRightTemp2:
        leftRight = 1
    if kRightTemp1 or kLeftTemp2:
        leftRight = 2
    if not(kLeft or kRight):
        leftRight = 0
    if kUpTemp1 or kDownTemp2:
        upDown = 1
    if kDownTemp1 or kUpTemp2:
        upDown = 2
    if not(kUp or kDown):
        upDown = 0

    if kLeft or kRight or kUp or kDown:
        block1.move(leftRight, upDown)

    kLeftTemp1 = False
    kRightTemp1 = False
    kUpTemp1 = False
    kDownTemp1 = False

    kLeftTemp2 = False
    kRightTemp2 = False
    kUpTemp2 = False
    kDownTemp2 = False

    #graphics
    screen.fill([255, 255, 255])
    all_sprites_list.draw(screen)
    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(120)

pygame.quit()
