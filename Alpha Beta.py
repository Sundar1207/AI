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

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, False)
                    position[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        return max_eval  # Early return breaks all loop levels
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = alphabeta(position, depth - 1, alpha, beta, True)
                    position[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        return min_eval  # Early return breaks all loop levels
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
