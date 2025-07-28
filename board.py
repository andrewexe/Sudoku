#imports packages
import pygame
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator, generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.current_cell = None
        self.difficulty = difficulty


        # sets a 2d list of cell objects correspondent to board size
        #this gonna create them all with a dash instead of creating the board-samir-so its shit
        #self.cells = [[Cell('-', i, j, self.screen) for i in range(10)] for j in range(10)]
        self.selected = [[False for i in range(9)] for j in range(9)]
        self.board = generate_sudoku(9, self.difficulty)
        self.cell = [[Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)] #add in sudoku generated numbers into each corresponding cell

    def draw(self):
        # draw lines

        for i in range(10):
            # defined box lines horizontal
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                                 (WIDTH, SQUARE_SIZE * i), LINE_WIDTH * 2)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                                 (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(10):
            # defined box line vertical
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH * 2)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
#prints out all the cells
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cell[i][j].draw()

    def select(self, row, col):
#sets all selected to false and the selected cell to True
        if not self.cell[row][col].get_locked():
            for i in range(9):
                for j in range(9):
                    self.cell[i][j].selected = False
                    self.selected[i][j] = False
            self.cell[row][col].selected = True
            self.selected[row][col] = True
        self.current_cell = self.cell[row][col]
        clock = pygame.time.Clock()

        pygame.init()
        self.draw()
        #draws the board again to clear past red cells
        pygame.draw.rect(self.screen, RED, pygame.Rect(row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE+2, SQUARE_SIZE+2), 2)
        #draws the red box for the selected cell



        #pygame.display.update()
        pygame.display.flip()


    def get_selected(self):
        return self.selected
    #returns if the cell is True
    def click(self, x, y):
        #fix after making board not take up the entire screen
        row = int(y // (self.height / 9))
        col = int(x // (self.height / 9))
        return row, col
    #we aint use this

    def clear(self):
        for i in range(9):
            for j in range(9):
                if not self.cell[i][j].get_locked():
                    self.current_cell.set_cell_value(0)
                    self.current_cell.set_sketched_value(0)
    #sets all not locked cells to 0 so when it redraws they dont show

    def sketch(self, value):
        #Currently  NOT DISPLAYED USING DRAW FUNCTION-dont matter ;)
        if self.selected and not self.current_cell.get_locked():
            self.current_cell.set_sketch_value(value)

    def place_number(self, value):
        #this seems fine-sets stuff
        if self.selected and not self.current_cell.get_locked():
            self.current_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cell:
            for cell in row:
                if not cell.get_locked():
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)
    #i dont think we used this either

    def is_full(self):
        for row in self.cell:
            for cell in row:
                if cell.get_value() == 0:
                    return False
        return True
    #checks if the board is full

    def update_board(self):
        for row in range(9):
            for cell in range(9):
                self.board[row][cell] = self.cell[row][cell].get_value()
    #makes the board 2d list indices equal to the cell value


    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
    #checks if there any empty cells

    def check_board(self):




        # row
        for row in self.board:
            print(len(set(row)))
            if len(set(row)) != 9 or 0 in set(row):
                return False

        # col
        for col in range(9):
            col_set = set(self.board[row][col] for row in range(9))
            print(len(col_set))
            if len(col_set) != 9 or (0 in col_set and len(col_set) > 1):
                return False

        # box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sq = [self.board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                sq_set = set(sq)
                print(len(set(sq_set)))
                if len(sq_set) != 9 or (0 in sq_set and len(sq_set) > 1):
                    return False
        return True

#test
