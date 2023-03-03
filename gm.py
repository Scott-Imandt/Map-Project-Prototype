import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SCENE = "menu"
# possible values: menu, play, end

DIFFICULTY = "easy"
# possible values: easy, medium, hard

difficulties = {
    "easy": 50,
    "medium": 20,
    "hard": 10
}

MAP = 0
# map file number
# possible values: 0, 1, 2

SCORE = 0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)