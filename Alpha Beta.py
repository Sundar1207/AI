def game_over(board):
    return winner(board) is not None or all(cell != ' ' for row in board for cell in row)


def winner(board):
    lines = []

    # Rows
    lines.extend(board)
    # Columns
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] != ' ' and all(cell == line[0] for cell in line):
            return line[0]
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

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    # Optimization: In-place state modification (backtracking)
                    position[i][j] = 'X'
                    score = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    if score > max_eval:
                        max_eval = score
                    if score > alpha:
                        alpha = score
                    if beta <= alpha:
                        return max_eval  # Early return to break all loops
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    # Optimization: In-place state modification (backtracking)
                    position[i][j] = 'O'
                    score = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '
                    if score < min_eval:
                        min_eval = score
                    if score < beta:
                        beta = score
                    if beta <= alpha:
                        return min_eval  # Early return to break all loops
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
