from pygame.locals import *
from Icons.constants import *

X_PLUS = 235
X_MINUS = 185
Y_PLUS_MINUS = 210
X_START = 177
Y_START = 270
class Menu:

    def __init__(self, win):
        self.win = win
        self.start_button = Rect(X_START, Y_START, 100, 40)
        self.button_clicked = False
        self.colors_num = 5
        self.start_game = False

    def draw_menu(self):
        self.win.fill(WIN_FILL)
        self.win.blit(BACKGROUND, (0, 0))
        self.draw_plus_minus()
        self.draw_num_of_colors()

    def run_menu(self):
        self.draw_menu()
        self.start_button_click()
        self.plus_minus_click()
        self.win.blit(COW, (350, 12))
        self.win.blit(BULL, (400, 10))

    def draw_num_of_colors(self):
        if self.colors_num == 5:
            self.win.blit(FIVE, (X_MINUS + 9, Y_PLUS_MINUS - 80))
        elif self.colors_num == 6:
            self.win.blit(SIX, (X_MINUS + 9, Y_PLUS_MINUS - 80))
        elif self.colors_num == 7:
            self.win.blit(SEVEN, (X_MINUS + 9, Y_PLUS_MINUS - 80))
        elif self.colors_num == 8:
            self.win.blit(EIGHT, (X_MINUS + 9, Y_PLUS_MINUS - 80))
        elif self.colors_num == 9:
            self.win.blit(NINE, (X_MINUS + 9, Y_PLUS_MINUS - 80))

    def draw_plus_minus(self):
        x_plus = 235
        x_minus = 185
        y = 200
        self.win.blit(PLUS, (X_PLUS, Y_PLUS_MINUS))
        # font = pygame.font.SysFont("David", 75)
        # num = font.render(str(self.colors_num), True, BLACK)
        # self.win.blit(num, (X_MINUS + 23, Y_PLUS_MINUS - 80))
        self.win.blit(MINUS, (X_MINUS, Y_PLUS_MINUS))

    def plus_minus_click(self):
        pos = pygame.mouse.get_pos()
        x_plus = 150
        x_minus = 100
        y = 175

        if X_PLUS + 30 > pos[0] > X_PLUS and Y_PLUS_MINUS + 30 > pos[1] > Y_PLUS_MINUS:
            if pygame.mouse.get_pressed()[0] == 1:
                self.button_clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.button_clicked is True:
                self.button_clicked = False
                if self.colors_num < 9:
                    self.colors_num += 1

        elif X_MINUS + 30 > pos[0] > X_MINUS and Y_PLUS_MINUS + 30 > pos[1] > Y_PLUS_MINUS:
            if pygame.mouse.get_pressed()[0] == 1:
                self.button_clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.button_clicked is True:
                self.button_clicked = False
                if self.colors_num > 5:
                    self.colors_num -= 1

    def start_button_click(self):
        pos = pygame.mouse.get_pos()
        if self.start_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.button_clicked = True
                self.draw_start_button(BLUE_CLICK)
            elif pygame.mouse.get_pressed()[0] == 0 and self.button_clicked is True:
                self.button_clicked = False
                self.start_game = True
            else:
                self.draw_start_button(BLUE_HOVER)
        else:
            self.draw_start_button(BLUE)

    def draw_start_button(self, color):
        x = 180
        y = 270
        pygame.draw.rect(self.win, color, self.start_button)
        text = "  Start"
        font = pygame.font.SysFont("David", 32)
        outline_font = pygame.font.SysFont("David", 32)

        outline_text = outline_font.render(text, True, BLACK)
        button_text = font.render(text, True, WHITE)
        # self.win.blit(outline_text, (350, 449))
        # self.win.blit(button_text, (348, 447))
        # pygame.draw.line(self.win, BLACK, (340, 440), (340, 480), 2)
        # pygame.draw.line(self.win, BLACK, (340, 440), (440, 440), 2)
        # pygame.draw.line(self.win, BLACK, (340, 480), (440, 480), 2)
        # pygame.draw.line(self.win, BLACK, (440, 440), (440, 480), 2)
        self.win.blit(outline_text, (X_START + 7, y + 10))
        self.win.blit(button_text, (X_START + 5, y + 8))
        pygame.draw.line(self.win, BLACK, (X_START, Y_START), (X_START, Y_START + 40), 2)
        pygame.draw.line(self.win, BLACK, (X_START, Y_START), (X_START + 100, Y_START), 2)
        pygame.draw.line(self.win, BLACK, (X_START, Y_START + 40), (X_START + 100, Y_START + 40), 2)
        pygame.draw.line(self.win, BLACK, (X_START + 100, Y_START), (X_START + 100, Y_START + 40), 2)
