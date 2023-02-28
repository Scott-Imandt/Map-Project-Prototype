# Steps to use application
#   1. launch and draw the geojson file provided
#   2. apon quiting the application the score of your accuracy will be printed in the console


import pygame
import json

if __name__ == "__main__":

    # Load GeoJSON data
    with open('testGeoJsonFIle.json') as f:
        geojson_data = json.load(f)

    pygame_coordinates_Array = []

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

    clock = pygame.time.Clock()


    #points array to keep track of point information point informtaion is (0,0) from the top right of screen
    drawnpoints = []



    # Define a function to convert GeoJSON coordinates to Pygame coordinates
    def convert_coordinates(coordinates):
        x, y = coordinates
        # You may need to adjust the scaling factor depending on the size of your GeoJSON data
        return int((x * 12)+1650), int((y * -12)+850)

    def DrawMap():
        # Loop through each feature in the GeoJSON data and draw it on the screen
        for feature in geojson_data['features']:
            # Get the coordinates of the feature
            coordinates = feature['geometry']['coordinates']
            # If the feature is a polygon or a multipolygon, draw it using Pygame
            if feature['geometry']['type'] in ['Polygon', 'MultiPolygon']:
                # Convert the GeoJSON coordinates to Pygame coordinates
                pygame_coordinates = [convert_coordinates(coord) for coord in coordinates[0]]
                # Add to pygame_coordinates_dict
                pygame_coordinates_Array.append(pygame_coordinates)
                # Draw the polygon on the screen
                # Dont want to show map then comment out section below (This could bw used later possibly to show drawing at a later time)
                pygame.draw.polygon(win, (0, 0, 255), pygame_coordinates, 3)

    def pointComparator():
        #get the size of how many correct points
        pygame_coordinates_size =len(pygame_coordinates_Array[0])
        #number of points found correctly
        correct_points = 0

        #loop cycle every feature in array (only one)
        for x in pygame_coordinates_Array:
            #sub loop cycles every point drawn
            for y in drawnpoints:
                #if the geoJson array is empty break out of loop
                if(len(x) == 0):
                    break
                else:
                    #call function to check points
                    correct_points = correct_points + coordinateComparator(x,y)

        #if no points are correct dont divide by zero
        if(correct_points == 0):
            return 0
        else:
            # return result multiplied by 100 for percent value
            return (correct_points / pygame_coordinates_size)*100


    # check every point within 25 points of geojson coordinate
    def coordinateComparator(geo_coord, drawn_coord):

        for i in geo_coord:
            # get the half value of the coordinate
            init_geo_x = i[0] - 25
            init_geo_y = i[1] - 25
            #loop the x of geocoord rang of 50
            for j in range(50):
                #if a coord within the rage of the geojson cord(x) is within range of the drawn coord then check (y)
                if(init_geo_x+j == drawn_coord[0]):
                    for k in range(50):
                        # if statment to check the y value of the geocords to see if it is in range of the drawn coord
                        if(init_geo_y+k == drawn_coord[1]):
                            # if a match is found remove the matched geocoord from the pygame_coordinates_Array to prevent unessesary checking
                            pygame_coordinates_Array[0].remove(i)
                            return 1

        return 0
        pass

    # when drawn points are added to the array they are sometime duplicated due to the current implementaion of the while loop and append array
    # this function must be called before coordcomparator to remove unnessesary duplicate points
    def remove_duplicate_lists(arr):
        unique_tuples = set(tuple(x) for x in arr)
        unique_lists = [list(x) for x in unique_tuples]
        return unique_lists

    # this function is ment to check if a point exits in the array to not double add it (This helps but isnt fool proof and still lets additional points get added due to nature of pygame loop
    def findInList(point_to_find):
        for x in drawnpoints:
            if(point_to_find == x):
                return x
        return None


    DrawMap()
    pygame.display.update()

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
            if(findInList(pygame.mouse.get_pos()) == None):
                drawnpoints.append([mousexpos, mouseypos])
            #update the screen with the new shape information
            pygame.display.update()
           # print(drawnpoints)

        #right click detected
        if(mouse[2]):
            pass
            #DrawMap()
            #pygame.display.update()
            #xpos of the mouse at time of click
        #    mousexpos = pygame.mouse.get_pos()[0];
            # ypos of mouse at time of click
        #    mouseypos = pygame.mouse.get_pos()[1];
            #get the y value of check if it is in the dict
        #    temp = drawnpoints.get(mousexpos)
            # check if a y value exsits for the given x value
        #    if(temp != None):
                #if the y value returned equals the mouse posistion
        #        if(temp == mouseypos):
                    #print("TRUE")
                    #draw a white circle to cove the drawn black circle
        #            pygame.draw.circle(win, (255, 255, 255), (mousexpos, temp), 3)
                    #update the displat with the new shape
        #            pygame.display.update()
                    #remove the now coverd drawn black point
        #            drawnpoints.pop(pygame.mouse.get_pos()[0])
                    #debug print to see what is in the dict
        #            print(drawnpoints)

        #middle mouse click
        if(mouse[1]):
            #print(pygame_coordinates_Array)
            pass


        clock.tick(120)
    drawnpoints = remove_duplicate_lists(drawnpoints)
    pygame.display.update()
    print("Your Score is equal to:")
    print(pointComparator())