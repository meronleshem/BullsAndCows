import pygame

WIDTH = 450
HEIGHT = 500

COL_PAD = 30
ROW_PAD = 55

ROWS = 7
COLS = 4

## COLORS ##
WHITE = (255, 255, 255)
BLACK = (36, 34, 34)
YELLOW = (255, 255, 51)
RED = (255, 0, 0)
GREEN = (0, 102, 0)
PINK = (255, 26, 179)
PURPLE = (128, 0, 128)
ORANGE = (255, 153, 0)
TURQOUISE = (26, 255, 163)
BLUE = (63, 125, 224)
BLUE_HOVER = (40, 84, 153)
BLUE_CLICK = (20, 44, 82)
GREY = (217, 213, 204)
DARK_GREY = (62, 62, 40)
BROWN = (153, 102, 51)
LIGHT_BROWN = (255, 204, 102)
COLORS = [RED, BLUE, YELLOW, PINK, TURQOUISE, PURPLE, ORANGE, GREEN]
WIN_FILL = (249, 242, 236)

SUBMIT_BUTTON = (340, 440, 100, 40)

## ICONS ##
LOCK = pygame.transform.scale(pygame.image.load('icons/lock.png'), (25, 25))
BULL = pygame.transform.scale(pygame.image.load('icons/bull.png'), (45, 45))
COW = pygame.transform.scale(pygame.image.load('icons/cow.png'), (45, 45))
SCARED = pygame.transform.scale(pygame.image.load('icons/scared.png'), (90, 90))
HAPPY = pygame.transform.scale(pygame.image.load('icons/happy.png'), (90, 90))
SMILE = pygame.transform.scale(pygame.image.load('icons/smile.png'), (90, 90))
DEAD = pygame.transform.scale(pygame.image.load('icons/dead.png'), (90, 90))
CONFUSED = pygame.transform.scale(pygame.image.load('icons/confused.png'), (90, 90))

