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
size = (1240, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Amazing Bario Cousins')

#initialize clock
clock = pygame.time.Clock()

#loop until user clicks close button
done = False

while done == False:
    #event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.K_UP


    #game logic

    #graphics
    all_sprites_list.draw(screen)
    #update display
    pygame.display.flip()

    #limit framerate
    clock.tick(60)
pygame.quit()
