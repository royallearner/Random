# Lab 9: Sudoku Solver – Backtracking (9x9)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_safe(board, r, c, num):
    # row
    for j in range(9):
        if board[r][j] == num:
            return False
    # column
    for i in range(9):
        if board[i][c] == num:
            return False
    # 3x3 box
    sr = (r // 3) * 3
    sc = (c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    r, c = find_empty(board)
    if r is None:   # no empty cell
        return True
    for num in range(1, 10):
        if is_safe(board, r, c, num):
            board[r][c] = num
            if solve_sudoku(board):
                return True
            board[r][c] = 0
    return False

# 0 means empty
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Solved Sudoku:")
    for row in board:
        print(row)
else:
    print("No solution")
