from typing import Tuple

class Sudoku:
    """
    Sudoku solver using the backtracking algorithm
    The board must be a 2d array, the 'empty space' must be 0
    """
    def __init__(self, board):
        self.board = board

    def print(self):
        for row in range(9):
            if row % 3 == 0 and row != 0:
                print("- "*11)
            for col in range(9):
                if col % 3 == 0 and col != 0:
                    print('|', end=' ')
                if col == 8:
                    print(self.board[row][col])
                else:
                    print(self.board[row][col], end=' ')
        print()

    def find_empty(self) -> Tuple[int]:
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)

    def isValid(self, n, pos) -> bool:
        #check the row
        for row in range(9):
            if self.board[row][pos[1]] == n:
                return False

        #check the column
        for col in range(9):
            if self.board[pos[0]][col] == n:
                return False

        x = pos[1] // 3
        y = pos[0] // 3

        #check the cell
        for row in range(y*3, y*3+3):
            for col in range(x*3,x*3+3):
                if self.board[row][col] == n and (row,col) != pos:
                    return False
        return True
    
    def solve(self) -> bool:
        empty = self.find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for n in range(1, 10):
            if self.isValid(n, (row, col)):
                self.board[row][col] = n
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
