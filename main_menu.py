import pygame, sys
from button import Button
from main import *

MAP_FILE_NUMBER = 0
DIFFICULTY = 50

pygame.init()

SCREEN = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Dividing Line")

BG = pygame.image.load("assets/MainMenu.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def setDifficulty(difficulty):
    DIFFICULTY = difficulty

def setMap(number):
    MAP_FILE_NUMBER = number

def chooseDifficulty():
    while True:
        BG = pygame.image.load("assets/Difficulty.png")
        SCREEN.blit(BG, (0, 0))

        DIFF_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Button.png"), pos=(300, 600), 
                            text_input="EASY", font=get_font(48), base_color="#09eaf6", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Button.png"), pos=(600, 600), 
                            text_input="MEDIUM", font=get_font(48), base_color="#f39e0c", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Button.png"), pos=(900, 600), 
                            text_input="HARD", font=get_font(48), base_color="#ff000f", hovering_color="White")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(DIFF_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    setDifficulty(50)
                    chooseMap()
                elif MEDIUM_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    setDifficulty(20)
                    chooseMap()
                elif HARD_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    setDifficulty(10)
                    chooseMap()

        pygame.display.update()

def chooseMap():
    while True:
        BG = pygame.image.load("assets/Difficulty.png")
        SCREEN.blit(BG, (0, 0))

        MAP_MOUSE_POS = pygame.mouse.get_pos()

        US_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(300, 600), 
                            text_input="US", font=get_font(48), base_color="#d5e5f7", hovering_color="White")
        ITALY_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(600, 600), 
                            text_input="ITALY", font=get_font(48), base_color="#d5e5f7", hovering_color="White")
        AUSTRALIA_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(900, 600), 
                            text_input="AUSTRALIA", font=get_font(48), base_color="#d5e5f7", hovering_color="White")

        for button in [US_BUTTON, ITALY_BUTTON, AUSTRALIA_BUTTON]:
            button.changeColor(MAP_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if US_BUTTON.checkForInput(MAP_MOUSE_POS):
                    setMap(0)
                    playGame(DIFFICULTY, MAP_FILE_NUMBER)
                elif ITALY_BUTTON.checkForInput(MAP_MOUSE_POS):
                    setMap(1)
                    playGame(DIFFICULTY, MAP_FILE_NUMBER)
                elif AUSTRALIA_BUTTON.checkForInput(MAP_MOUSE_POS):
                    setMap(2)
                    playGame(DIFFICULTY, MAP_FILE_NUMBER)

        pygame.display.update()

def play():
    chooseDifficulty()

if __name__ == "__main__":
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(600, 600), 
                            text_input="PLAY", font=get_font(48), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 750), 
                            text_input="QUIT", font=get_font(48), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()