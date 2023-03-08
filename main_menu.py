import pygame, sys
from button import Button
import gm

BG = pygame.image.load("assets/MainMenu.png")

def chooseDifficulty():
    while True:
        BG = pygame.image.load("assets/Difficulty.png")
        gm.SCREEN.blit(BG, (0, 0))

        DIFF_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Button.png"), pos=(300, 600), 
                            text_input="EASY", font=gm.get_font(48), base_color="#a8f8d9", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Button.png"), pos=(600, 600), 
                            text_input="MEDIUM", font=gm.get_font(48), base_color="#f39e0c", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Button.png"), pos=(900, 600), 
                            text_input="HARD", font=gm.get_font(48), base_color="#ff000f", hovering_color="White")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(DIFF_MOUSE_POS)
            button.update(gm.SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    gm.DIFFICULTY = "easy"
                    chooseMap()
                    return
                elif MEDIUM_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    gm.DIFFICULTY = "medium"
                    chooseMap()
                    return
                elif HARD_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    gm.DIFFICULTY = "hard"
                    chooseMap()
                    return
        pygame.display.update()

def chooseMap():
    while True:
        BG = pygame.image.load("assets/Choose Map.png")
        gm.SCREEN.blit(BG, (0, 0))

        MAP_MOUSE_POS = pygame.mouse.get_pos()

        US_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(300, 600), 
                            text_input="US", font=gm.get_font(48), base_color="#b2d0f0", hovering_color="White")
        ITALY_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(600, 600), 
                            text_input="ITALY", font=gm.get_font(48), base_color="#b2d0f0", hovering_color="White")
        AUSTRALIA_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(900, 600), 
                            text_input="AUSTRALIA", font=gm.get_font(48), base_color="#b2d0f0", hovering_color="White")

        for button in [US_BUTTON, ITALY_BUTTON, AUSTRALIA_BUTTON]:
            button.changeColor(MAP_MOUSE_POS)
            button.update(gm.SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if US_BUTTON.checkForInput(MAP_MOUSE_POS):
                    #playGame(difficulty, 0)
                    gm.MAP = 0
                    gm.SCENE = "play"
                    return
                elif ITALY_BUTTON.checkForInput(MAP_MOUSE_POS):
                    #playGame(difficulty, 1)
                    gm.MAP = 1
                    gm.SCENE = "play"
                    return
                elif AUSTRALIA_BUTTON.checkForInput(MAP_MOUSE_POS):
                    #playGame(difficulty, 2)
                    gm.MAP = 2
                    gm.SCENE = "play"
                    return
        pygame.display.update()

def mainMenu():
    pygame.init()
    while True:
        gm.SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 600), 
                            text_input="PLAY", font=gm.get_font(48), base_color="#c2eae3", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 750), 
                            text_input="QUIT", font=gm.get_font(48), base_color="#c2eae3", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(gm.SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    chooseDifficulty()
                    return
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit(0)
        pygame.display.update()