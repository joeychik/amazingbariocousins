#menu screen STUFF
import pygame

class PressKeyToStart(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/presskey.png')
       self.rect = self.image.get_rect()
       self.rect.x = 340
       self.rect.y = 400

class MainMenuText(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/nohighscore.png')
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 350

class MainMenuArrows(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('assets/text/playarrow.png')
       self.rect = self.image.get_rect()
       self.rect.x = 462
       self.rect.y = 350

    def update(self, whichButton):
       if whichButton % 4 == 0:
            self.image = pygame.image.load('assets/text/playarrow.png')
       elif whichButton % 4 == 1:
            self.image = pygame.image.load('assets/text/instructionarrow.png')
       elif whichButton % 4 == 2:
            self.image = pygame.image.load('assets/text/creditsarrow.png')
       elif whichButton % 4 == 3:
            self.image = pygame.image.load('assets/text/exitarrow.png')

class MainMenu():
    def __init__(self):
        self.done = False
        self.menuScreen = False
        self.keyPressed = False
        self.keyDown = False
        self.whichButton = 1
        mainMenuArrows = MainMenuArrows()
        mainMenuText = MainMenuText()
        pressKeyToStart = PressKeyToStart()
        menu = pygame.sprite.Group()
        menu.add(mainMenuText)
        menu.add(mainMenuArrows)
        playGroup = pygame.sprite.GroupSingle()
        play = PressKeyToStart()
        playGroup.add(play)
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    done = True
            if not self.keyPressed:
                if event.type == pygame.KEYDOWN:
                    keyPressed = True
                    self.menuScreen = True
            if self.menuScreen:
                pygame.draw.rect(screen,sky,[340,400,615,25],0)
                if event.type == pygame.KEYDOWN:
                    if not self.keyDown:
                        if event.key == pygame.K_DOWN:
                            self.whichButton += 1
                            self.keyDown = True
                        if event.key == pygame.K_UP:
                            self.whichButton -= 1
                            self.keyDown = True
                        if event.key == pygame.K_RETURN:
                            if whichButton % 4 == 3:
                                done = True
                            if whichButton % 4 == 2:
                                self.menuScreen = False
                                #add credit screen stuff here
                if event.type == pygame.KEYUP:
                    keyDown = False
                mainMenuArrows.update(self.whichButton)
                menu.draw(screen)
            else:
                playGroup.draw(screen)
            pygame.display.flip()
            screen.blit(bg, [0, 0])
            clock.tick(60)
