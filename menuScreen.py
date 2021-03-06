#menu screen STUFF
import pygame

class PressKeyToStart(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('presskey.png')
       self.rect = self.image.get_rect()
       self.rect.x = 340
       self.rect.y = 400

class MainMenuText(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('nohighscore.png')
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 350

class MainMenuArrows(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('playarrow.png')
       self.rect = self.image.get_rect()
       self.rect.x = 462
       self.rect.y = 350

    def update(self, whichButton):
       if whichButton % 4 == 0:
            self.image = pygame.image.load('playarrow.png')
       elif whichButton % 4 == 1:
            self.image = pygame.image.load('instructionarrow.png')
       elif whichButton % 4 == 2:
            self.image = pygame.image.load('creditsarrow.png')
       elif whichButton % 4 == 3:
            self.image = pygame.image.load('exitarrow.png')

class Credits(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('credit.png')
       self.rect = self.image.get_rect()
       self.rect.x = 450
       self.rect.y = 310

class Instructions(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('instruction1.png')
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 0
       self.slide = 0

    def update(self):
        if self.slide % 3 == 0:
            self.image = pygame.image.load('instruction1.png')
        elif self.slide % 3 == 1:
            self.image = pygame.image.load('instruction2.png')
        elif self.slide % 3 == 2:
            self.image = pygame.image.load('instruction3.png')

class CharSelect(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load ('charactersel.png')
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 0

def MainMenu(screen, clock):
    done = False
    menuScreen = False
    creditScreen = False
    instructionScreen = False
    charScreen = False
    keyPressed = False
    keyDown = False
    whichButton = 1
    bg = pygame.image.load('mainmenu.png')
    mainMenuArrows = MainMenuArrows()
    mainMenuText = MainMenuText()
    pressKeyToStart = PressKeyToStart()
    credit = Credits()
    play = PressKeyToStart()
    instructions = Instructions()
    selection = CharSelect()
    creditGroup = pygame.sprite.GroupSingle()
    menu = pygame.sprite.Group()
    instruction = pygame.sprite.Group()
    selectGroup = pygame.sprite.GroupSingle()
    menu.add(mainMenuText)
    menu.add(mainMenuArrows)
    creditGroup.add(credit)
    instruction.add(instructions)
    selectGroup.add (selection)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if not keyPressed:
            screen.blit(play.image, [play.rect.x, play.rect.y])
            if event.type == pygame.KEYDOWN:
                pygame.event.clear()
                keyPressed = True
                menuScreen = True
                keyDown = True
        if menuScreen:
            pygame.draw.rect(screen, (146, 144, 255), [340,400,615,25], 0)
            if event.type == pygame.KEYDOWN:
                if not keyDown:
                    if event.key == pygame.K_DOWN:
                        whichButton += 1
                        keyDown = True
                    if event.key == pygame.K_UP:
                        whichButton -= 1
                        keyDown = True
                    if event.key == pygame.K_RETURN:
                        if whichButton % 4 == 0:
                            menuScreen = False
                            charScreen = True
                        if whichButton % 4 == 1:
                            menuScreen = False
                            instructionScreen = True
                        if whichButton % 4 == 2:
                            menuScreen = False
                            creditScreen = True
                        if whichButton % 4 == 3:
                            pygame.quit()
                    keyDown = True
            if event.type == pygame.KEYUP:
                keyDown = False
            mainMenuArrows.update(whichButton)
            menu.draw(screen)

        if creditScreen:
            creditGroup.draw(screen)
            if event.type == pygame.KEYUP:
                keyDown = False
            if not keyDown:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        creditScreen = False
                        menuScreen = True

    # Instruction Screen
        if instructionScreen:
            instruction.draw(screen)
            if event.type == pygame.KEYDOWN:
                if not keyDown:
                    if event.key == pygame.K_RIGHT:
                        instructions.slide += 1
                    if event.key == pygame.K_LEFT:
                        instructions.slide -= 1
                    if event.key == pygame.K_ESCAPE:
                        instructionScreen = False
                        menuScreen = True
                        instructions.slide = 0
                keyDown = True
            if event.type == pygame.KEYUP:
                keyDown = False
            instruction.update()
        if charScreen:
            selectGroup.draw(screen)
            if event.type == pygame.KEYUP:
                keyDown = False
            if not keyDown:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        charScreen = False
                        menuScreen = True
                    if event.key == pygame.K_RETURN:
                        done = True
        pygame.display.flip()
        screen.blit(bg, [0, 0])
        clock.tick(60)
