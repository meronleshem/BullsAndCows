import pygame
from Icons.constants import BLACK, WHITE, GREY, LOCK


class Circle:
    def __init__(self, row, col, radius, centerX, centerY, color=WHITE):
        self.row = row
        self.col = col
        self.radius = radius
        self.centerX = centerX
        self.centerY = centerY
        self.color = color

    def draw(self, win, locked=False):
        pygame.draw.circle(win, BLACK, (self.centerX, self.centerY), self.radius + 2)
        if locked is False:
            pygame.draw.circle(win, self.color, (self.centerX, self.centerY), self.radius)
        else:
            pygame.draw.circle(win, GREY, (self.centerX, self.centerY), self.radius)
            win.blit(LOCK, (self.centerX - 1 - LOCK.get_width()//2, self.centerY - LOCK.get_height()//2))

    def set_color(self, color):
        self.color = color

