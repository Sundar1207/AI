def alphabeta(position, depth, alpha, beta, maximizing_player):
    # Optimization: Inline winner evaluation and use hardcoded index comparisons to bypass function call overhead and allocations.
    w = None
    if position[0][0] != ' ' and position[0][0] == position[0][1] == position[0][2]:
        w = position[0][0]
    elif position[1][0] != ' ' and position[1][0] == position[1][1] == position[1][2]:
        w = position[1][0]
    elif position[2][0] != ' ' and position[2][0] == position[2][1] == position[2][2]:
        w = position[2][0]
    elif position[0][0] != ' ' and position[0][0] == position[1][0] == position[2][0]:
        w = position[0][0]
    elif position[0][1] != ' ' and position[0][1] == position[1][1] == position[2][1]:
        w = position[0][1]
    elif position[0][2] != ' ' and position[0][2] == position[1][2] == position[2][2]:
        w = position[0][2]
    elif position[0][0] != ' ' and position[0][0] == position[1][1] == position[2][2]:
        w = position[0][0]
    elif position[0][2] != ' ' and position[0][2] == position[1][1] == position[2][0]:
        w = position[0][2]

    if w == 'X':
        return 1
    elif w == 'O':
        return -1
    elif depth == 0 or (' ' not in position[0] and ' ' not in position[1] and ' ' not in position[2]):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    # Optimization: Use in-place backtracking instead of creating full copies of the board array for each child state.
                    position[i][j] = 'X'
                    eval_val = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    if eval_val > max_eval:
                        max_eval = eval_val
                    if eval_val > alpha:
                        alpha = eval_val
                    if beta <= alpha:
                        return max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = 'O'
                    eval_val = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '
                    if eval_val < min_eval:
                        min_eval = eval_val
                    if eval_val < beta:
                        beta = eval_val
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
