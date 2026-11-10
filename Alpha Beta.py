def alphabeta(position, depth, alpha, beta, maximizing_player):
    # Inline game_over, winner, and evaluate check for performance
    # Rows
    for i in range(3):
        if position[i][0] != ' ' and position[i][0] == position[i][1] == position[i][2]:
            return 1 if position[i][0] == 'X' else -1
    # Columns
    for j in range(3):
        if position[0][j] != ' ' and position[0][j] == position[1][j] == position[2][j]:
            return 1 if position[0][j] == 'X' else -1
    # Diagonals
    if position[0][0] != ' ' and position[0][0] == position[1][1] == position[2][2]:
        return 1 if position[0][0] == 'X' else -1
    if position[0][2] != ' ' and position[0][2] == position[1][1] == position[2][0]:
        return 1 if position[0][2] == 'X' else -1

    # Check for empty cells directly
    if depth == 0 or not (' ' in position[0] or ' ' in position[1] or ' ' in position[2]):
        return 0

    if maximizing_player:
        max_eval = -100
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = 'X'
                    eval_score = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    if eval_score > max_eval:
                        max_eval = eval_score
                    if max_eval > alpha:
                        alpha = max_eval
                    if beta <= alpha:
                        return max_eval
        return max_eval
    else:
        min_eval = 100
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = 'O'
                    eval_score = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '
                    if eval_score < min_eval:
                        min_eval = eval_score
                    if min_eval < beta:
                        beta = min_eval
                    if beta <= alpha:
                        return min_eval
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
