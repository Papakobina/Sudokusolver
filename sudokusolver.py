import numpy as np

sudoku = np.array([
    [0, 0, 2, 0, 1, 5, 0, 7, 8],
    [1, 8, 0, 0, 6, 3, 4, 0, 0],
    [0, 0, 4, 0, 2, 0, 5, 6, 1],
    [0, 9, 6, 0, 0, 7, 0, 3, 0],
    [0, 1, 0, 3, 0, 6, 0, 0, 5],
    [0, 0, 3, 2, 0, 4, 0, 9, 6],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [6, 4, 6, 8, 3, 0, 2, 0, 7],
    [0, 0, 7, 0, 0, 0, 0, 1, 0]
])


def possible(board, row, col, val):
    if board[row][col] != 0:
        return False
    if val in sudoku[row]:
        return False
    for i in range(9):
        if board[i][col] == val:
            return False
    sqrow = int(int(row) / 3) * 3
    sqcol = int(int(col) / 3) * 3
    for r in range(sqrow, sqrow + 3):
        for c in range(sqcol, sqcol + 3):
            if board[r][c] == val:
                return False
    return True


def solve_sudoku(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                for val in range(1, 10):
                    if possible(sudoku, row, col, val):
                        board[row][col] = val
                        if solve_sudoku(sudoku):
                            return True
                        board[row][col] = 0
                return False
    return True


solve_sudoku(sudoku)
print(sudoku)


