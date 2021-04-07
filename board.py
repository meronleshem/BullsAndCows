import math
from pygame.locals import *
from Icons.constants import *
from guess_circle import GuessCircle
from circle import Circle
import random


class Board:
    def __init__(self, win):
        self.win = win
        self.current_row = ROWS - 1
        self.guess_circles = []
        self.answer_circles = []
        self.code = []
        self.submit_button = Rect(SUBMIT_BUTTON)
        self.button_clicked = False
        self.button_active = True
        self.finish = False
        self.create_board()
        self.draw_board()

    def draw_board(self):
        self.draw_circles()

    def draw_circles(self):
        for row in range(ROWS):
            for col in range(4):
                guess_circle = self.guess_circles[row][col]
                guess_circle.draw(self.win)
                answer_circle = self.answer_circles[row][col]
                answer_circle.draw(self.win)
        pygame.draw.line(self.win, BLACK, [125, 0], [125, HEIGHT], 3)

        if self.finish is True and self.current_row >= 0:
            self.win.blit(HAPPY, (13, 13))

        elif self.finish is True and self.current_row < 0:
            self.win.blit(DEAD, (13, 13))
        elif self.finish is False and self.current_row > 3:
            self.win.blit(SMILE, (13, 13))
        elif self.finish is False and self.current_row > 2:
            self.win.blit(CONFUSED, (13, 13))
        elif self.finish is False and self.current_row < 2:
            self.win.blit(SCARED, (13, 13))

        if self.finish is False:
            for code_circle in range(ANS_COLS):
                self.code[code_circle].draw(self.win, True)
        else:
            for code_circle in range(ANS_COLS):
                self.code[code_circle].draw(self.win)

    def create_board(self):
        for row in range(ROWS):
            self.guess_circles.append([])
            for col in range(4):
                self.guess_circles[row].append(GuessCircle(row, col))

        for row in range(ROWS):
            self.answer_circles.append([])
            for col in range(ANS_COLS):
                self.answer_circles[row].append(Circle(row, col, 7, 30 * col + 30 // 2, 100 + 55 * row + 55 // 2))

        for col in range(ANS_COLS):
            self.guess_circles[self.current_row][col].change_active()

        self._generate_code()

    def _generate_code(self):
        code_set = set([])
        while len( code_set) < 4:
            color_num = random.randint(0, 7)
            code_set.add(color_num)

        code_list = list(code_set)

        self.color_code_set = set([])
        for i in code_set:
            self.color_code_set.add(COLORS[i])

        random.shuffle(code_list)
        for i in range(ANS_COLS):
            self.code.append(Circle(0, i, 20, 47 * i + 160, 50, COLORS[code_list[i]]))

    def select_circle(self, row, col):
        x1 = row
        y1 = col
        selected = None
        for row in range(ROWS):
            for col in range(ANS_COLS):
                temp_circle = self.guess_circles[row][col]
                distance = math.hypot(x1 - temp_circle.centerX, y1 - temp_circle.centerY)
                if distance <= temp_circle.radius:
                    selected = temp_circle
                    break

        if selected != None:
            selected.change_color()

    def submit_guess(self):
        bulls, cows = self.check_guess()

        for col in range(ANS_COLS):
            self.guess_circles[self.current_row][col].change_active()

        for bull in range(bulls):
            self.answer_circles[self.current_row][bull].set_color(RED)

        if bulls == 4:
            self.button_active = False
            self.finish = True
            return
        for cow in range(cows):
            self.answer_circles[self.current_row][cow+bulls].set_color(YELLOW)

        self.current_row -= 1
        if self.current_row < 0:
            self.finish = True
            self.button_active = False
            return 0
        for col in range(ANS_COLS):
            self.guess_circles[self.current_row][col].change_active()

    def check_guess(self):
        bulls = 0
        cows = 0
        index = 0

        for guess_circle in self.guess_circles[self.current_row]:
             if guess_circle.color in  self.color_code_set:
                if guess_circle.color == self.code[index].color:
                    bulls += 1
                else:
                    cows += 1
             index += 1

        return bulls, cows

    def click_button(self):
        if self.button_active is False:
            self.draw_button(DARK_GREY)
            return 0

        pos = pygame.mouse.get_pos()
        if self.submit_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.button_clicked = True
                self.draw_button(BLUE_CLICK)
            elif pygame.mouse.get_pressed()[0] == 0 and self.button_clicked is True:
                self.button_clicked = False
                self.submit_guess()
                self.draw_circles()
                self.draw_button(BLUE_HOVER)
            else:
                self.draw_button(BLUE_HOVER)
        else:
            self.draw_button(BLUE)

    def draw_button(self, color):
        pygame.draw.rect(self.win, color, self.submit_button)
        font = pygame.font.SysFont("David", 29)
        outline_font = pygame.font.SysFont("David", 29)
        text = "Submit"
        # if color == DARK_GREY:
        #     text = "  Retry"
        outline_text = outline_font.render(text, True, BLACK)
        button_text = font.render(text, True, WHITE)
        self.win.blit(outline_text, (350, 449))
        self.win.blit(button_text, (348, 447))
        pygame.draw.line(self.win, BLACK, (340, 440), (340, 480), 2)
        pygame.draw.line(self.win, BLACK, (340, 440), (440, 440), 2)
        pygame.draw.line(self.win, BLACK, (340, 480), (440, 480), 2)
        pygame.draw.line(self.win, BLACK, (440, 440), (440, 480), 2)

