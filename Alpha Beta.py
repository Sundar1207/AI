# Optimization: Inline evaluate and game_over to remove function overhead.
# Optimization: Use in-place backtracking array updates instead of deep copying
# arrays for each child state.
def alphabeta(position, depth, alpha, beta, maximizing_player):
    # evaluate inlined
    val = 0
    # Rows
    for i in range(3):
        if position[i][0] != ' ' and position[i][0] == position[i][1] == position[i][2]:
            val = 1 if position[i][0] == 'X' else -1
            break
    else:
        # Columns
        for j in range(3):
            if position[0][j] != ' ' and position[0][j] == position[1][j] == position[2][j]:
                val = 1 if position[0][j] == 'X' else -1
                break
        else:
            # Diagonals
            if position[0][0] != ' ' and position[0][0] == position[1][1] == position[2][2]:
                val = 1 if position[0][0] == 'X' else -1
            elif position[0][2] != ' ' and position[0][2] == position[1][1] == position[2][0]:
                val = 1 if position[0][2] == 'X' else -1

    if val != 0 or depth == 0:
        return val

    game_over_bool = True
    for row in position:
        if ' ' in row:
            game_over_bool = False
            break

    if game_over_bool:
        return val

    if maximizing_player:
        max_eval = float('-inf')
        player = 'X'
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
                        return max_eval
        return max_eval
    else:
        min_eval = float('inf')
        player = 'O'
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
