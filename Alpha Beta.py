def winner(board):
    # Rows
    if board[0][0] != ' ' and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] != ' ' and board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] != ' ' and board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    # Columns
    if board[0][0] != ' ' and board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] != ' ' and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] != ' ' and board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    # Diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def game_over(board):
    if winner(board) is not None:
        return True

    if board[0][0] == ' ' or board[0][1] == ' ' or board[0][2] == ' ' or \
       board[1][0] == ' ' or board[1][1] == ' ' or board[1][2] == ' ' or \
       board[2][0] == ' ' or board[2][1] == ' ' or board[2][2] == ' ':
        return False
    return True


def evaluate(board):
    w = winner(board)
    if w == 'X':
        return 1   # Maximizing player wins
    elif w == 'O':
        return -1  # Minimizing player wins
    else:
        return 0   # Draw or game not finished


def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player  # Make move
                    eval_score = alphabeta(board, depth - 1, alpha, beta, False)
                    board[i][j] = ' '  # Undo move
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        return max_eval  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player  # Make move
                    eval_score = alphabeta(board, depth - 1, alpha, beta, True)
                    board[i][j] = ' '  # Undo move
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
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
