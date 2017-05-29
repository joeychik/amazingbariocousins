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


#loop until user clicks close button
done = False

while done == False:


    #check if close button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
