import pygame, sys, os
from button import Button
import gm

def end():
    lbPoints = []
    maxEntries = 10
    map_name = ""
    if gm.MAP == 0:
        map_name = "United States"
    elif gm.MAP == 1:
        map_name = "Italy"
    else:
        map_name = "Australia"

    # open leaderboard file and write score
    lbPath = "./leaderboard.txt"
    if(os.path.exists(lbPath)):
        # if file exists, initialize array of high scores
        lbFile = open(lbPath, "r")
        lbPoints = lbFile.read().splitlines()
        lbFile.close()
    else:
        # create new file
        lbFile = open(lbPath, "x")
        lbFile.close()

    # find location to add score in
    added = False
    for i, item in enumerate(lbPoints):
        score = item.split(", ")
        score = float(score[1])
        if gm.SCORE > score:
            lbPoints.insert(i, map_name+", "+str(gm.SCORE))
            if len(lbPoints) > maxEntries:
                lbPoints.pop(len(lbPoints) - 1)

            lbFile = open(lbPath, "w")
            lbFile.write('\n'.join(lbPoints))
            lbFile.close()

            added = True
            break

    if gm.SCORE > 0 and not added and len(lbPoints) < maxEntries:
        lbFile = open(lbPath, "w")
        lbPoints.append(map_name+", "+str(gm.SCORE))
        lbFile.write('\n'.join(lbPoints))
        lbFile.close()
    # file write end

    pygame.init()
    BG = pygame.image.load("assets/Leaderboard.png")
    gm.SCREEN.blit(BG, (0, 0))

    text = gm.get_font(48).render('Your score is equal to '+ str(gm.SCORE) +'%', True, (0, 0, 255))
    gm.SCREEN.blit(text, ((gm.SCREEN_WIDTH - text.get_width()) / 2, 95))

    for i, item in enumerate(lbPoints):
        text = gm.get_font(24).render(item, True, (0, 0, 0))
        gm.SCREEN.blit(text, ((gm.SCREEN_WIDTH - text.get_width()) / 2, 375 + 32 * i))

    while True:
        CLOSE_MOUSE_POS = pygame.mouse.get_pos()

        CLOSE_BUTTON = Button(image=pygame.image.load("assets/Select Box.png"), pos=(600, 800), 
                        text_input="QUIT", font=gm.get_font(36), base_color="#a8f8d9", hovering_color="White")

        for button in [CLOSE_BUTTON]:
            button.changeColor(CLOSE_MOUSE_POS)
            button.update(gm.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOSE_BUTTON.checkForInput(CLOSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

        