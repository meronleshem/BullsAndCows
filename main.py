import pygame
from pygame import mixer
import time
from Icons.constants import WIDTH, HEIGHT, WIN_FILL, COW, BULL, BLACK
from board import Board
from menu import Menu

FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Bulls And Cows')

def menu():

    run = True
    clock = pygame.time.Clock()
    menu = Menu(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if menu.start_game:
            main(menu.colors_num)
            break

        menu.run_menu()
        pygame.display.update()


def main(colors_num):
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN, colors_num)

    while run:
        clock.tick(FPS)

        if not board.get_finish():
            curr_time = time.time()
            exact_time = curr_time - board.start_time
            board.seconds = 60 - exact_time % 60
            board.minutes = 10 - exact_time / 60
            if int(board.minutes) == 0:
                if int(board.seconds) == 0:
                    board.finish = True
                    board.current_row = -1
                    mixer.music.load('Icons/Loser.mp3')
                    mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            board.click_button()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board.select_circle(pos)

        board.draw_board()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    menu()
