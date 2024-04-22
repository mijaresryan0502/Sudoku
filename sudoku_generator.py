import random

class SudokuGenerator:
    #Constructor
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board =[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.box_length = row_length ** 0.5

    #Gettter
    def get_board(self):
        return self.board

    #Prints the board
    def print_board(self):
        for i in self.board:
            print(*i)

    #Checks within one list if the numbers of the list are all different from 1-9
    def valid_in_row(self, row, num):
        for i in range(int(len(self.board[row]))):
            if self.board[row][i] == num:
                return False
        return True

    #Checks down the lists if the number in the column are all different from 1-9
    def valid_in_col(self, col, num):
        for row in range(int(len(self.board))):
            if self.board[row][int(col)] == num:
                return False
        return True

    #Checks all the numbers within the box different for every box
    def valid_in_box(self, row_start, col_start, num):
        box_row = 1 + (row_start // 3)
        box_col = 1 + (col_start // 3)
        if box_row == 1 and box_col == 1:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == num:
                        return False
        elif box_row == 1 and box_col == 2:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j + 3] == num:
                        return False
        elif box_row == 1 and box_col == 3:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j + 6] == num:
                        return False
        elif box_row == 2 and box_col == 1:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 3][j] == num:
                        return False
        elif box_row == 2 and box_col == 2:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 3][j + 3] == num:
                        return False
        elif box_row == 2 and box_col == 3:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 3][j + 6] == num:
                        return False
        elif box_row == 3 and box_col == 1:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 6][j] == num:
                        return False
        elif box_row == 3 and box_col == 2:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 6][j + 3] == num:
                        return False
        elif box_row == 3 and box_col == 3:
            for i in range(3):
                for j in range(3):
                    if self.board[i + 6][j + 6] == num:
                        return False
        return True

    #Uses the valid methods to return if the number can be inputed in the place
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)

    #Fills the box with #1-9
    def fill_box(self, row_start, col_start):
        box = set()
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while True:
                    value = random.randint(1,9)
                    if value not in box:
                        box.add(value)
                        self.board[i][j] = value
                        break

    #Fills the 3 boxes in the main diagonal with numbers
    def fill_diagonal(self):
        box = set()
        for i in range(3):
            for j in range(3):
                while True:
                    value = random.randint(1,9)
                    if value not in box:
                        box.add(value)
                        self.board[i][j] = value
                        break
        box = set()
        for i in range(3,6):
            for j in range(3,6):
                while True:
                    value = random.randint(1,9)
                    if value not in box:
                        box.add(value)
                        self.board[i][j] = value
                        break
        box = set()
        for i in range(6,9):
            for j in range(6,9):
                while True:
                    value = random.randint(1,9)
                    if value not in box:
                        box.add(value)
                        self.board[i][j] = value
                        break

    #Provided
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, int(self.row_length + 1)):
            if self.is_valid(row, int(col), num):
                self.board[int(row)][int(col)] = num
                if self.fill_remaining(row, int(col) + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    #Provided
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    #Changes the number of the cordinate given to 0 basically removing it
    def remove_cells(self):
        cords_set = set()
        while len(cords_set) < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)\

            cords = (row, col)

            if cords not in cords_set:
                cords_set.add(cords)

        for row, col in cords_set:
            self.board[row][col] = 0

#Provided
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
