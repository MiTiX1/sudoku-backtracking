from sudoku import Sudoku

BOARD = [
    [0,0,7,0,6,0,5,0,0],
    [0,0,3,2,0,5,7,0,0],
    [6,5,0,0,0,0,0,2,9],
    [0,3,0,0,9,0,0,5,0],
    [8,0,0,6,0,4,0,0,7],
    [0,1,0,0,8,0,0,4,0],
    [3,9,0,0,0,0,0,7,4],
    [0,0,5,7,0,8,2,0,0],
    [0,0,2,0,3,0,8,0,0]
]
def main():
    s = Sudoku(BOARD)
    s.print()
    s.solve()
    s.print()

if __name__ == "__main__":
    main()