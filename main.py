# Steps to use application
#   1. launch and draw the geojson file provided
#   2.5 change / set difficulty (50 == easy, 20 medium, 10 hard) These number are working numbers that set pixel offset accuracy
#   2. apon quiting the application the score of your accuracy will be printed in the console


import pygame
import json

if __name__ == "__main__":


    pygame_coordinates_Array = []

    #initalize pygame module
    pygame.init()

    #tuple to set window size
    win = pygame.display.set_mode((1200,1000))

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
    def convert_coordinates(coordinates, multiplyList, addList):
        x, y = coordinates

        # You may need to adjust the scaling factor depending on the size of your GeoJSON data
        return int((x * multiplyList[0])+addList[0]), int((y * multiplyList[1])+addList[1])

    def DrawMap(geojson_data, multiplyList, addList):
        # Loop through each feature in the GeoJSON data and draw it on the screen
        for feature in geojson_data['features']:
            # Get the coordinates of the feature
            coordinates = feature['geometry']['coordinates']
            # If the feature is a polygon or a multipolygon, draw it using Pygame
            if feature['geometry']['type'] in ['Polygon', 'MultiPolygon']:
                # Convert the GeoJSON coordinates to Pygame coordinates
                pygame_coordinates = [convert_coordinates(coord, multiplyList, addList) for coord in coordinates[0][0]]
                # Add to pygame_coordinates_dict
                pygame_coordinates_Array.append(pygame_coordinates)
                # Draw the polygon on the screen
                # Dont want to show map then comment out section below (This could bw used later possibly to show drawing at a later time)
                pygame.draw.polygon(win, (0, 0, 255), pygame_coordinates, 3)

    def pointComparator(difficulty):
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
                    correct_points = correct_points + coordinateComparator(x,y, difficulty)

        #if no points are correct dont divide by zero
        if(correct_points == 0):
            return 0
        else:
            # return result multiplied by 100 for percent value
            return (correct_points / pygame_coordinates_size)*100


    # check every point within 25 points of geojson coordinate
    def coordinateComparator(geo_coord, drawn_coord, difficulty):
        halfValueDifficulty = difficulty/2

        for i in geo_coord:
            # get the half value of the coordinate
            init_geo_x = i[0] - halfValueDifficulty
            init_geo_y = i[1] - halfValueDifficulty
            #loop the x of geocoord rang of 50
            for j in range(difficulty):
                #if a coord within the rage of the geojson cord(x) is within range of the drawn coord then check (y)
                if(init_geo_x+j == drawn_coord[0]):
                    for k in range(difficulty):
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

    def drawRectangle():
        smallest_XY = [pygame_coordinates_Array[0][0][0], pygame_coordinates_Array[0][0][1]]
        largest_XY = [pygame_coordinates_Array[0][0][0], pygame_coordinates_Array[0][1][1]]
        #find the smallest x value and largest x value
        for x in pygame_coordinates_Array[0]:
            if(x[0] > largest_XY[0]):
                largest_XY[0] = x[0]
            if(x[0] < smallest_XY[0]):
                smallest_XY[0] = x[0]
            if (x[1] > largest_XY[1]):
                largest_XY[1] = x[1]
            if (x[1] < smallest_XY[1]):
                smallest_XY[1] = x[1]


        smallest_XY = [smallest_XY[0]-100, smallest_XY[1]-100]
        largest_XY = [largest_XY[0]+100, largest_XY[1]+100]

        print(smallest_XY)
        print(largest_XY)
        width = largest_XY[0] - smallest_XY[0]
        height = largest_XY[1] - smallest_XY[1]
        pygame.draw.rect(win, (255,0,0), [smallest_XY[0],smallest_XY[1],width, height], 2, 5)


    def drawGrid(window, size, rows):

        # Size of cubes in grid
        distatnce_btw_rows = size // rows
        x=0
        y=0

        for z in range(rows):
            # increment x and y values using distance adder
            x+= distatnce_btw_rows
            y+= distatnce_btw_rows

            #draw line from x until size
            pygame.draw.line(window, (178,190,181), (x,0), (x, size))
            #draw line from from size to y
            pygame.draw.line(window, (178,190,181), (0,y), (size, y))


    def loadJSONFile(number):
        # Load GeoJSON data
        if(number == 0):
            with open('testGeoJsonFIle.json') as f:
                geojson_data = json.load(f)
            multiplyList = [16,-16]
            addList = [2130,1050]
            DrawMap(geojson_data, multiplyList,addList)

        elif(number == 1):
            with open('TestFileOFItaly.json') as f:
                geojson_data = json.load(f)
            multiplyList = [40, -40]
            addList = [100, 2150]
            DrawMap(geojson_data, multiplyList, addList)

        elif (number == 2):
            with open('TestFileOfAustralia.json') as f:
                geojson_data = json.load(f)
            multiplyList = [15, -15]
            addList = [-1400, 100]
            DrawMap(geojson_data, multiplyList, addList)

    drawGrid(win, 1200, 100)
    loadJSONFile(2)
    drawRectangle()
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
    print(pointComparator(50),"%")