def game_over(board):
    return winner(board) is not None or all(cell != ' ' for row in board for cell in row)


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


def alphabeta(position, depth, alpha, beta, maximizing_player):
    w = winner(position)
    if w == 'X':
        return 1
    elif w == 'O':
        return -1

    if depth == 0:
        return 0

    is_full = True
    for row in position:
        for cell in row:
            if cell == ' ':
                is_full = False
                break
        if not is_full:
            break
    if is_full:
        return 0

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval_score = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '  # Backtrack
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        return max_eval  # Cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval_score = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '  # Backtrack
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        return min_eval  # Cutoff
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
