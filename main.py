import pygame
from Icons.constants import WIDTH, HEIGHT, WIN_FILL, COW, BULL
from board import Board

FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Bulls And Cows')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = x
    col = y
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(WIN_FILL)
    WIN.blit(COW, (350, 12))
    WIN.blit(BULL, (400, 10))
    board = Board(WIN)

    while run:
        clock.tick(FPS)

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
