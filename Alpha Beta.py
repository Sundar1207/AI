def game_over(board):
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def winner(board):
    # Rows
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # Columns
    for j in range(3):
        if board[0][j] != ' ' and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    # Diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def evaluate(board):
    w = winner(board)
    if w == 'X':
        return 1   # Maximizing player wins
    elif w == 'O':
        return -1  # Minimizing player wins
    else:
        return 0   # Draw or game not finished


def alphabeta(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '

                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        return max_eval  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '

                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        return min_eval  # Alpha cutoff
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
