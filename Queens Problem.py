def solve_8_queens():
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, 8), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True
    
    def solve(board, col):
        if col >= 8:
            return True
        for i in range(8):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        return False
    
    board = [[0 for _ in range(8)] for _ in range(8)]
    if solve(board, 0):
        for row in board:
            print(row)
    else:
        print("No solution exists")

solve_8_queens()
