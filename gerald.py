#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-05-25

#import necessary modules
import pygame

#initialize game engine
pygame.init()

#set screen
size = (1240, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#initialize clock
clock = pygame.time.Clock()

#define classes
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([])



#loop until user clicks close button
done = False

while done == False:
    #event processing. all events such as key presses or clicks are events. this is the section that processes events(takes input)
    for event in pygame.event.get():
        #check if window close button has been pressed
        if event.type == pygame.QUIT:
            done = True

    #game logic


    #game drawing


pygame.quit()