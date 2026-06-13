def is_safe(board, row, col):
    # check column
    for i in range(row):
        if board[i] == col:
            return False
    # check diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(row, n, board, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, n, board, solutions)

if __name__ == "__main__":
    n = 4
    board = [-1] * n
    solutions = []
    solve_nqueens(0, n, board, solutions)

    print("Solutions for", n, "queens (row -> col):")
    for sol in solutions:
       print(sol)
