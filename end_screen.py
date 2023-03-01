import pygame, sys
from main_menu import get_font, mainMenu
from button import Button

def end(score):
    pygame.init()
    win = pygame.display.set_mode((1200,1000))
    BG = pygame.image.load("assets/Gradient Background.png")
    win.blit(BG, (0, 0))
    font = get_font(48)
    text = font.render('Your score is equal to '+score+'%', True, (0, 0, 255))
    textRect = text.get_rect()
 
    # set the center of the rectangular object.
    textRect.center = (600, 300)
    pygame.draw.rect(text, (255, 255, 255), textRect, 1)

    while True:
        win.blit(text, textRect)
        CLOSE_MOUSE_POS = pygame.mouse.get_pos()

        CLOSE_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 600), 
                        text_input="QUIT", font=get_font(36), base_color="#a8f8d9", hovering_color="White")

        for button in [CLOSE_BUTTON]:
            button.changeColor(CLOSE_MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOSE_BUTTON.checkForInput(CLOSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

        