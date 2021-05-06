import pygame
from Icons.constants import BLACK, GREY, WHITE, COLORS


class GuessCircle:
    ROW_SPACE = 100
    COL_SPACE = 145

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.curr_color = -1
        self.color = GREY
        self.radius = 20
        self.active = False
        self.centerY = self.ROW_SPACE + 55 * self.row + 55 // 2
        self.centerX = self.COL_SPACE + 47 * self.col + 30 // 2

    def change_color(self, colors_num):
        if self.active is True:
            self.curr_color += 1
            if self.curr_color >= colors_num:
                self.curr_color = 0
            self.color = COLORS[self.curr_color]

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.centerX, self.centerY), self.radius + 2)
        pygame.draw.circle(win, self.color, (self.centerX, self.centerY), self.radius)

    def change_active(self):
        if self.active is True:
            self.active = False
        else:
            self.active = True
            self.color = WHITE




