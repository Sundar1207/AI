def alphabeta(position, depth, alpha, beta, maximizing_player):
    # Optimization: Inline evaluate and game_over directly to avoid function call overhead
    # Check rows
    for i in range(3):
        if position[i][0] != ' ' and position[i][0] == position[i][1] == position[i][2]:
            return 1 if position[i][0] == 'X' else -1

    # Check columns
    for j in range(3):
        if position[0][j] != ' ' and position[0][j] == position[1][j] == position[2][j]:
            return 1 if position[0][j] == 'X' else -1

    # Check diagonals
    if position[0][0] != ' ' and position[0][0] == position[1][1] == position[2][2]:
        return 1 if position[0][0] == 'X' else -1
    if position[0][2] != ' ' and position[0][2] == position[1][1] == position[2][0]:
        return 1 if position[0][2] == 'X' else -1

    is_full = True
    for i in range(3):
        if ' ' in position[i]:
            is_full = False
            break

    if depth == 0 or is_full:
        return 0

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    # Optimization: In-place state modification (backtracking) instead of copy
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    if eval > max_eval:
                        max_eval = eval
                    if max_eval > alpha:
                        alpha = max_eval
                    if beta <= alpha:
                        return max_eval  # Beta cutoff and early return
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    # Optimization: In-place state modification (backtracking) instead of copy
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '
                    if eval < min_eval:
                        min_eval = eval
                    if min_eval < beta:
                        beta = min_eval
                    if beta <= alpha:
                        return min_eval  # Alpha cutoff and early return
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
