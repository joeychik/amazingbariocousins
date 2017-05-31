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



class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill([255, 0, 0])
        self.rect = self.image.get_rect()
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def left(self):
        self.rect.x -= 5

    def right(self):
        self.rect.x += 5

    def up(self):
        self.rect.y -= 5

    def down(self):
        self.rect.y += 5

all_sprites_list = pygame.sprite.Group()

block1 = Block()
block1.rect.x = 50
block1.rect.y = 50
all_sprites_list.add(block1)



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
                block1.moveLeft = True
                block1.moveRight = False
            elif event.key == pygame.K_RIGHT:
                block1.moveRight = True
                block1.moveLeft = False
            elif event.key == pygame.K_UP:
                block1.moveUp = True
                block1.moveDown = False
            elif event.key == pygame.K_DOWN:
                block1.moveDown = True
                block1.moveUp = False
            continue
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                block1.moveLeft = False
            elif event.key == pygame.K_RIGHT:
                block1.moveRight = False
            elif event.key == pygame.K_UP:
                block1.moveUp = False
            elif event.key == pygame.K_DOWN:
                block1.moveDown = False

    #game logic
    if block1.moveLeft == True:
        block1.left()
    if block1.moveRight == True:
        block1.right()
    if block1.moveUp == True:
        block1.up()
    if block1.moveDown == True:
        block1.down()

    #graphics
    screen.fill([255, 255, 255])
    all_sprites_list.draw(screen)
    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(120)

pygame.quit()
