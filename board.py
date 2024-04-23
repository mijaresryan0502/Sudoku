import pygame
from cell import Cell
from constants import *
from sudoku_generator import *

class Board:
    #Consructor
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = generate_sudoku(9, difficulty)
        self.start = self.board
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(len(self.board))] for i in range(len(self.board))]

    #Draws the grid
    def draw(self):
        #Draws the cells
        for cell in self.cells:
            for i in cell:
                i.draw()
        #Draws the Boxes
        for i in range(0, BOARD_ROWS + 1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH * 3)
        for i in range(0, BOARD_COLS +1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE,0), (i * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH * 3)
        pygame.display.update()

    #Select cell
    def select(self, row, col):
        self.row, self.col = row, col
        for cell in self.cells:
            for i in cell:
                i.draw()
        self.cell = Cell(self.board[self.row][self.col], self.row, self.col, self.screen)
        self.cell.red = True
        self.cell.draw()

    #Returns the click location
    def click(self, x, y):
        if x <= self.width and y <= self.height - 100:
            return x // SQUARE_SIZE, y // SQUARE_SIZE

    #Clears cell
    def clear(self):
        self.cells[self.row][self.col].sketched_value = 0
        self.cells[self.row][self.col].cell_value = 0
        self.cells[self.row][self.col].draw()
        pygame.display.update()
        #Resets the values of sketched_value and cell_value to have
        self.cells[self.row][self.col].sketched_value = 0.1
        self.cells[self.row][self.col].cell_value = 0.1

    #Sets value of selected cell equal to typed number
    def sketch(self, value):
        self.cells[self.row][self.col].sketched_value = value
        self.cells[self.row][self.col].draw()

    #Sets value of selected cell to the number when user presses enter
    def place_number(self, value):
        self.cells[self.row][self.col].set_cell_value(value)
        self.cells[self.row][self.col].draw()

    #Resets the board to its original form
    def reset_to_original(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(len(self.board))] for i in range(len(self.board))]
        Board.draw(self)

    #Returns a Bolean if the board is full or not
    def is_full(self):
        for cell in self.cells:
            for i in cell:
                if i.cell_value == 0.1 and i.value == 0:
                    return False
        return True

    #Updates the board with the values in all cells
    def update_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    self.board[i][j] = self.cells[i][j].cell_value

    #Located the empty cell and returns a tuple
    def find_empty(self):
        for cell in self.cells:
            for i in cell:
                if i.cell_value == 0.1 and i.value == 0:
                    return (self.cells.index(cell), cell.index(i))


    #Checks the validity of the board
    def check_board(self):
        for i in self.board:
            for j in range(1, 10):
                if i.count(j) >= 2:
                    return False
        return True
