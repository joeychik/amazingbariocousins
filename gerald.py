#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-06-08

#import necessary modules
import pygame
from classes import *

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

#initialize game engine
pygame.init()

#set screen
size = (1300, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#initialize clock
clock = pygame.time.Clock()

#initialize necessary variables
kLeft = False
kRight = False
kUp = False

kLeftTemp1 = False
kRightTemp1 = False
kUpTemp1 = False

kLeftTemp2 = False
kRightTemp2 = False
kUpTemp2 = False

pause = False

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
            if event.key == pygame.K_p:
                pause == True
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

    worldScroll = player.moved

    #move player
    playergroup.update(kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2, kUp, obstacle_list)

    #pause loop
    if pause:
        Pause_screen()

    #update position of everything that moved
    enemy_list.update(worldScroll)
    obstacle_list.update(worldScroll)

    #reset temporary variables
    kLeftTemp1 = False
    kRightTemp1 = False

    kLeftTemp2 = False
    kRightTemp2 = False

    pause = False

    #graphics
    screen.fill(LIGHT_BLUE)

    sprite_list.draw(screen)

    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(60)
pygame.quit()
