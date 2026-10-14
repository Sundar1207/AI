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


def alphabeta(position, depth, alpha, beta, maximizing_player):
    w = winner(position)
    if w == 'X':
        return 1   # Maximizing player wins
    elif w == 'O':
        return -1  # Minimizing player wins

    is_draw = True
    for row in position:
        if ' ' in row:
            is_draw = False
            break

    if depth == 0 or is_draw:
        return 0   # Draw or game not finished

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        # Optimized: In-place state modification (backtracking) avoids full board cloning overhead
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '  # Backtrack
                    if eval > max_eval:
                        max_eval = eval
                    if eval > alpha:
                        alpha = eval
                    if beta <= alpha:
                        return max_eval  # Beta cutoff breaks out of nested loops
        return max_eval
    else:
        min_eval = float('inf')
        # Optimized: In-place state modification (backtracking) avoids full board cloning overhead
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '  # Backtrack
                    if eval < min_eval:
                        min_eval = eval
                    if eval < beta:
                        beta = eval
                    if beta <= alpha:
                        return min_eval  # Alpha cutoff breaks out of nested loops
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
