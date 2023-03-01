#Run this file to start game!
import pygame, sys
from button import Button
from play import *

pygame.init()

SCREEN = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Dividing Line - Prototype")

BG = pygame.image.load("assets/MainMenu.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def chooseDifficulty():
    while True:
        BG = pygame.image.load("assets/Difficulty.png")
        SCREEN.blit(BG, (0, 0))

        DIFF_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Button.png"), pos=(300, 600), 
                            text_input="EASY", font=get_font(48), base_color="#a8f8d9", hovering_color="White")
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
                    chooseMap(50)
                elif MEDIUM_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    chooseMap(20)
                elif HARD_BUTTON.checkForInput(DIFF_MOUSE_POS):
                    chooseMap(10)
        pygame.display.update()

def chooseMap(difficulty):
    while True:
        BG = pygame.image.load("assets/Choose Map.png")
        SCREEN.blit(BG, (0, 0))

        MAP_MOUSE_POS = pygame.mouse.get_pos()

        US_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(300, 600), 
                            text_input="US", font=get_font(48), base_color="#b2d0f0", hovering_color="White")
        ITALY_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(600, 600), 
                            text_input="ITALY", font=get_font(48), base_color="#b2d0f0", hovering_color="White")
        AUSTRALIA_BUTTON = Button(image=pygame.image.load("assets/Country Select.png"), pos=(900, 600), 
                            text_input="AUSTRALIA", font=get_font(48), base_color="#b2d0f0", hovering_color="White")

        for button in [US_BUTTON, ITALY_BUTTON, AUSTRALIA_BUTTON]:
            button.changeColor(MAP_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if US_BUTTON.checkForInput(MAP_MOUSE_POS):
                    playGame(difficulty, 0)
                elif ITALY_BUTTON.checkForInput(MAP_MOUSE_POS):
                    playGame(difficulty, 1)
                elif AUSTRALIA_BUTTON.checkForInput(MAP_MOUSE_POS):
                    playGame(difficulty, 2)
        pygame.display.update()

def mainMenu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 600), 
                            text_input="PLAY", font=get_font(48), base_color="#c2eae3", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 750), 
                            text_input="QUIT", font=get_font(48), base_color="#c2eae3", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    chooseDifficulty()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
    
if __name__ == "__main__":
    mainMenu()