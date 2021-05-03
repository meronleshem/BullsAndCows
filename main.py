import pygame
from Icons.constants import WIDTH, HEIGHT, WIN_FILL, COW, BULL, BLACK
from board import Board
import time

FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Bulls And Cows')


def get_row_col_from_mouse(pos):
    row, col = pos
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN)

    while run:
        clock.tick(FPS)

        if not board.get_finish():
            curr_time = time.time()
            exact_time = curr_time - board.start_time
            board.seconds = exact_time % 60
            board.minutes = exact_time / 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            board.click_button()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                board.select_circle(row, col)

        board.draw_board()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
