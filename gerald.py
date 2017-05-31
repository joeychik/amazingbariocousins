#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-05-30

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
        #self.image = pygame.image.load("bario.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.x = 650
        self.rect.y = 400

    def left():
        self.rect.x -= 5

    def right():
        self.rect.x += 5

    def jump():
        self.rect.y -= 15

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

#initialize clock
clock = pygame.time.Clock()

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
                player.left
            if event.key == pygame.K_RIGHT:
                player.right

    #game logic

    #graphics
    all_sprites_list.draw(screen)
    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(40)
pygame.quit()
