def winner(board):
    # Optimization: Hardcoded array index comparisons instead of dynamic list comprehensions
    for r in range(3):
        if board[r][0] != ' ' and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    for c in range(3):
        if board[0][c] != ' ' and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def alphabeta(position, depth, alpha, beta, maximizing_player):
    # Optimization: Inline evaluate logic to avoid extra game_over checks
    w = winner(position)
    if w is not None:
        return 1 if w == 'X' else -1
    is_full = True
    for row in position:
        if ' ' in row:
            is_full = False
            break
    if depth == 0 or is_full:
        return 0

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        # Optimization: Inline get_children and use backtracking to avoid copying
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    if eval > max_eval:
                        max_eval = eval
                    if eval > alpha:
                        alpha = eval
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
                    if eval < min_eval:
                        min_eval = eval
                    if eval < beta:
                        beta = eval
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
