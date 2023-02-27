import pygame

if __name__ == "__main__":

    #initalize pygame module
    pygame.init()

    #tuple to set window size
    win = pygame.display.set_mode((1000,1000))

    #String to set window title
    pygame.display.set_caption("Map Game Prototype");

    #Define a variable to control the main loop
    running = True

    #fill window with white on game start
    win.fill((255,255,255))

    #points array to keep track of point information point informtaion is (0,0) from the top right of screen
    drawnpoints = dict()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value too False, to exit the main loop
                running = False

        mouse = pygame.mouse.get_pressed()

        #if left click is detected
        if(mouse[0]):
            #print("leftclick")
            #xpos of mouse at time of click
            mousexpos = pygame.mouse.get_pos()[0];
            #ypos of mouse at time of click
            mouseypos = pygame.mouse.get_pos()[1];
            #draw action to create the circle on the graph
            pygame.draw.circle(win, (0,0,0), (mousexpos,mouseypos),3)
            #add point to the dictionary object
            drawnpoints.update({mousexpos: mouseypos})
            #update the screen with the new shape information
            pygame.display.update()
           # print(drawnpoints)

        #right click detected
        if(mouse[2]):
            #xpos of the mouse at time of click
            mousexpos = pygame.mouse.get_pos()[0];
            # ypos of mouse at time of click
            mouseypos = pygame.mouse.get_pos()[1];
            #get the y value of check if it is in the dict
            temp = drawnpoints.get(mousexpos)
            # check if a y value exsits for the given x value
            if(temp != None):
                #if the y value returned equals the mouse posistion
                if(temp == mouseypos):
                    #print("TRUE")
                    #draw a white circle to cove the drawn black circle
                    pygame.draw.circle(win, (255, 255, 255), (mousexpos, temp), 3)
                    #update the displat with the new shape
                    pygame.display.update()
                    #remove the now coverd drawn black point
                    drawnpoints.pop(pygame.mouse.get_pos()[0])
                    #debug print to see what is in the dict
                    print(drawnpoints)