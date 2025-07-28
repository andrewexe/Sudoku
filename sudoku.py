import copy
import sys

import pygame
from constants import *
from board import Board

pygame.init()

#fuck
def draw_start(screen):
    screen.fill((25, 210, 255))

    # andrew
    title_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 75)

    title_text = title_font.render("Sudoku", True, WHITE)
    title_box = title_text.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 2 - 50))
    screen.blit(title_text, title_box)

    easy = button_font.render("Easy", True, WHITE)
    medium = button_font.render("Medium", True, WHITE)
    hard = button_font.render("Hard", True, WHITE)

    easy_box = easy.get_rect(center=(WIDTH // 4, HEIGHT // 4 + 450))
    screen.blit(easy, easy_box)

    medium_box = medium.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 4 + 450))
    screen.blit(medium, medium_box)

    hard_box = hard.get_rect(center=(WIDTH // 2 + 390, HEIGHT // 4 + 450))
    screen.blit(hard, hard_box)



    pygame.display.update()
    running = True
    while running:

        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_box.collidepoint(pos):
                    return 30
                elif medium_box.collidepoint(pos):
                    return 40
                elif hard_box.collidepoint(pos):
                    return 50

        # screen.fill((255, 255, 255))
        pygame.display.update()


def draw_win():
    screen = pygame.display.set_mode((800, 800))
    screen.fill((25, 210, 255))

    win_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 75)

    win_text = win_font.render("You Win!", True, WHITE)
    win_box = win_text.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 2 - 50))
    screen.blit(win_text, win_box)

    restart = button_font.render("Restart", True, WHITE)
    restart_box = restart.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 4 + 450))
    screen.blit(restart, restart_box)

    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_box.collidepoint(event.pos):
                    return 1


def draw_loss():
    screen = pygame.display.set_mode((800, 800))
    screen.fill((25, 210, 255))

    loss_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 75)

    loss_text = loss_font.render("You Lose :(", True, WHITE)
    loss_box = loss_text.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 2 - 50))
    screen.blit(loss_text, loss_box)

    quit = button_font.render("Quit", True, WHITE)
    quit_box = quit.get_rect(center=(WIDTH // 2 + 130, HEIGHT // 4 + 450))
    screen.blit(quit, quit_box)

    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_box.collidepoint(event.pos):
                    pygame.quit
                    sys.exit()


def play_game(difficulty):
    screen = pygame.display.set_mode((540, 640))
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    game_over = False
    while not game_over:
        board.draw()
        pygame.display.update()
        pygame.time.delay(10000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_over = True
        pygame.display.update()
        pygame.quit()


pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((800, 800))
# diff = draw_start(screen)

if __name__ == "__main__":
    while True:

        diff = draw_start(screen)

        restart = False

        screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
        board = Board(WIDTH, HEIGHT, screen, diff)


        # idk if work

        # rando
        screen.fill(WHITE)
        board.draw()

        button_font = pygame.font.Font(None, 75)

        reset_btn = button_font.render("Reset", True, (0, 0, 0))
        reset_box = reset_btn.get_rect(center=(WIDTH // 6, HEIGHT // 2 + 325))
        screen.blit(reset_btn, reset_box)

        restart_btn = button_font.render("Restart", True, (0, 0, 0))
        restart_box = restart_btn.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 325))
        screen.blit(restart_btn, restart_box)

        exit_btn = button_font.render("Exit", True, (0, 0, 0))
        exit_box = exit_btn.get_rect(center=(WIDTH // 2 + 175, HEIGHT // 2 + 325))
        screen.blit(exit_btn, exit_box)

        pygame.display.update()

        # pos = pygame.mouse.get_pos()
        # pygame.time.delay(3000)

        while restart == False:

            if board.is_full():
                if board.check_board():
                    if draw_win() == 1:
                        restart = True
                else:
                    draw_loss()

            for event in pygame.event.get():
                pygame.init()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = event.pos
                    g_row = int(row // SQUARE_SIZE)
                    g_col = int(col // SQUARE_SIZE)
                    if exit_box.collidepoint(event.pos):
                        pygame.quit()
                    if restart_box.collidepoint(event.pos):
                        screen = pygame.display.set_mode((800, 800))
                        restart = True
                    if reset_box.collidepoint(event.pos):
                        board.reset_to_original()
                        board.update_board()
                        pygame.draw.rect(screen, BG_COLOR,
                                         pygame.Rect(0, 0, 540, 540), 400)
                        board.draw()

                    row, col = event.pos
                    g_row = int(row // SQUARE_SIZE)
                    g_col = int(col // SQUARE_SIZE)

                    print(g_row, g_col)

                    if pygame.Rect(g_row, g_col, board.width, board.height).collidepoint(event.pos) \
                            and g_col < 9 and g_row < 9:
                        board.select(g_row, g_col)

                if event.type == pygame.KEYDOWN and board.get_selected()[g_row][g_col]:
                    if event.key == pygame.K_1:
                        num = 1
                        board.cell[g_row][g_col].set_sketched_value(num)
                        print(num)
                    if event.key == pygame.K_2:
                        num = 2
                        board.cell[g_row][g_col].set_sketched_value(num)
                        print(num)
                    if event.key == pygame.K_3:
                        num = 3
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_4:
                        num = 4
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_5:
                        num = 5
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_6:
                        num = 6
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_7:
                        num = 7
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_8:
                        num = 8
                        board.cell[g_row][g_col].set_sketched_value(num)
                    if event.key == pygame.K_9:
                        num = 9
                        board.cell[g_row][g_col].set_sketched_value(num)

                    if event.key == pygame.K_RETURN:
                        board.cell[g_row][g_col].set_cell_value(board.cell[g_row][g_col].get_sketch())
                        board.board[g_row][g_col] = board.cell[g_row][g_col].get_value()
                        num = None

                    if event.key == pygame.K_BACKSPACE:
                        board.cell[g_row][g_col].set_cell_value(0)
                        board.board[g_row][g_col] = 0

                    board.current_cell.draw()



                pygame.display.update()