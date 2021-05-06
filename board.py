import math
from pygame.locals import *
from Icons.constants import *
from guess_circle import GuessCircle
from circle import Circle
import random
from pygame import mixer
import time


class Board:
    def __init__(self, win, colors_num):
        self.win = win
        self.colors_num = colors_num
        self.current_row = ROWS - 1
        self.guess_circles = []
        self.clue_circles = []
        self.code = []
        self.submit_button = Rect(SUBMIT_BUTTON)
        self.button_clicked = False
        self.button_active = False
        self.finish = False
        self.create_board()
        self.start_time = time.time()
        self.minutes = 0
        self.seconds = 0

    def reset(self):
        self.__init__(self.win, self.colors_num)

    def draw_board(self):
        self.win.fill(WIN_FILL)
        self.win.blit(COW, (350, 12))
        self.win.blit(BULL, (400, 10))
        self.draw_circles()
        self.draw_face()
        self.click_button()
        self.draw_timer(self.minutes, self.seconds)

    def draw_circles(self):
        for row in range(ROWS):
            for col in range(4):
                guess_circle = self.guess_circles[row][col]
                guess_circle.draw(self.win)
                answer_circle = self.clue_circles[row][col]
                answer_circle.draw(self.win)
        pygame.draw.line(self.win, BLACK, [125, 0], [125, HEIGHT], 3)

        if self.finish is False:
            for code_circle in range(COLS):
                self.code[code_circle].draw(self.win, True)
        else:
            for code_circle in range(COLS):
                self.code[code_circle].draw(self.win)

    def draw_face(self):
        if self.finish is True and self.current_row >= 0:
            self.win.blit(HAPPY, (13, 13))

        elif self.finish is True and self.current_row < 0:
            self.win.blit(DEAD, (13, 13))
        elif self.finish is False and self.current_row > 3:
            self.win.blit(SMILE, (13, 13))
        elif self.finish is False and self.current_row >= 2:
            self.win.blit(CONFUSED, (13, 13))
        elif self.finish is False and self.current_row < 2:
            self.win.blit(SCARED, (13, 13))

    def create_board(self):
        for row in range(ROWS):
            self.guess_circles.append([])
            for col in range(4):
                self.guess_circles[row].append(GuessCircle(row, col))

        for row in range(ROWS):
            self.clue_circles.append([])
            for col in range(COLS):
                self.clue_circles[row].append(Circle(row, col, 7, 30 * col + 30 // 2, 100 + 55 * row + 55 // 2))

        for col in range(COLS):
            self.guess_circles[self.current_row][col].change_active()

        self._generate_code()

    def _generate_code(self):
        # code_set = set()
        # while len(code_set) < 4:
        #     color_num = random.randint(0, 7)
        #     code_set.add(color_num)
        self.color_code_set = set()
        while len(self.color_code_set) < 4:
            color_num = random.randint(0, self.colors_num - 1)
            self.color_code_set.add(COLORS[color_num])

        code_list = list(self.color_code_set)

        # self.color_code_set = set()
        # for i in code_set:
        #     self.color_code_set.add(COLORS[i])

        random.shuffle(code_list)
        for i in range(COLS):
            self.code.append(Circle(0, i, 20, 47 * i + 160, 50, code_list[i]))

    def select_circle(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        selected = None
        for row in range(ROWS):
            for col in range(COLS):
                temp_circle = self.guess_circles[row][col]
                distance = math.hypot(x1 - temp_circle.centerX, y1 - temp_circle.centerY)
                if distance <= temp_circle.radius:
                    selected = temp_circle
                    break

        if selected:
            selected.change_color(self.colors_num)

    def submit_guess(self):
        bulls, cows = self.check_guess()

        for col in range(COLS):
            self.guess_circles[self.current_row][col].change_active()

        for bull in range(bulls):
            self.clue_circles[self.current_row][bull].set_color(RED)

        if bulls == 4:
            self.button_active = True
            self.finish = True
            mixer.music.load('Icons/Winner.mp3')
            mixer.music.play()
            return
        for cow in range(cows):
            self.clue_circles[self.current_row][cow + bulls].set_color(YELLOW)

        self.current_row -= 1
        if self.current_row < 0:
            self.finish = True
            mixer.music.load('Icons/Loser.mp3')
            mixer.music.play()
            self.button_active = True
            return 0
        for col in range(COLS):
            self.guess_circles[self.current_row][col].change_active()

    def check_guess(self):
        bulls = 0
        cows = 0
        index = 0

        for guess_circle in self.guess_circles[self.current_row]:
             if guess_circle.color in self.color_code_set:
                if guess_circle.color == self.code[index].color:
                    bulls += 1
                else:
                    cows += 1
             index += 1

        return bulls, cows

    def draw_timer(self, minuets, seconds):
        font = pygame.font.SysFont("David", 29)
        timer = "{:02d}:{:02d}".format(int(minuets), int(seconds))
        timer_text = font.render(timer, True, BLACK)
        timer_x = 365
        timer_y = 80
        self.win.blit(timer_text, (timer_x, timer_y))

        pygame.draw.line(self.win, BLACK, (timer_x - 5, timer_y - 5), (timer_x + 68, timer_y - 5), 2)
        pygame.draw.line(self.win, BLACK, (timer_x - 5, timer_y - 5), (timer_x - 5, timer_y + 25), 2)
        pygame.draw.line(self.win, BLACK, (timer_x - 5, timer_y + 25), (timer_x + 68, timer_y + 25), 2)
        pygame.draw.line(self.win, BLACK, (timer_x + 68, timer_y - 5), (timer_x + 68, timer_y + 25), 2)

    def click_button(self):
        self.check_guess_is_vaild()

        if self.button_active is False:
            self.draw_button(BLUE_HOVER)
            return

        pos = pygame.mouse.get_pos()
        if self.submit_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.button_clicked = True
                self.draw_button(BLUE_CLICK)
            elif pygame.mouse.get_pressed()[0] == 0 and self.button_clicked is True:
                self.button_clicked = False
                if self.button_active is True and self.finish is False:
                    self.submit_guess()
                  #  self.draw_board()
                    self.draw_button(BLUE_HOVER)
                else:
                    self.reset()
            else:
                self.draw_button(BLUE_HOVER)
        else:
            self.draw_button(BLUE)

    def check_guess_is_vaild(self):
        valid_guess = set()
        for col in range(COLS):
            color = self.guess_circles[self.current_row][col].color
            if color == WHITE:
                break
            valid_guess.add(color)

        if len(valid_guess) < 4:
            self.button_active = False
        else:
            self.button_active = True

    def draw_button(self, color):
        pygame.draw.rect(self.win, color, self.submit_button)
        text = "Submit"
        if self.finish:
            text = "  Reset  "
        font = pygame.font.SysFont("David", 29)
        outline_font = pygame.font.SysFont("David", 29)

        outline_text = outline_font.render(text, True, BLACK)
        button_text = font.render(text, True, WHITE)
        self.win.blit(outline_text, (350, 449))
        self.win.blit(button_text, (348, 447))
        pygame.draw.line(self.win, BLACK, (340, 440), (340, 480), 2)
        pygame.draw.line(self.win, BLACK, (340, 440), (440, 440), 2)
        pygame.draw.line(self.win, BLACK, (340, 480), (440, 480), 2)
        pygame.draw.line(self.win, BLACK, (440, 440), (440, 480), 2)

    def get_finish(self):
        return self.finish