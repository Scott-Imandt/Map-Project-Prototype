import pygame
import gm
from main_menu import mainMenu
from play import playGame
from end_screen import end

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Dividing Line - Prototype")

    gm.SCENE = "menu"
    running = True

    while(running):
        match gm.SCENE:
            case "menu":
                mainMenu()
            case "play":
                playGame()
            case "end":
                end()