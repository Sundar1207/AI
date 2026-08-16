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
    is_draw = True
    for i in range(3):
        for j in range(3):
            if position[i][j] == ' ':
                is_draw = False
                break
        if not is_draw:
            break
    if is_draw:
        return 0

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval_score = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '

                    if eval_score > max_eval:
                        max_eval = eval_score
                    if eval_score > alpha:
                        alpha = eval_score
                    if beta <= alpha:
                        return max_eval  # Early return beta cutoff to break out of nested loops
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval_score = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '

                    if eval_score < min_eval:
                        min_eval = eval_score
                    if eval_score < beta:
                        beta = eval_score
                    if beta <= alpha:
                        return min_eval  # Early return alpha cutoff
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
