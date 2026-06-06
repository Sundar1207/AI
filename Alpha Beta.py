def game_over(board):
    if winner(board) is not None:
        return True
    for row in board:
        if ' ' in row:
            return False
    return True


def winner(board):
    # Check rows
    for r in range(3):
        if board[r][0] != ' ' and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # Check columns
    for c in range(3):
        if board[0][c] != ' ' and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def evaluate(board):
    w = winner(board)
    if w == 'X':
        return 1   # Maximizing player wins
    elif w == 'O':
        return -1  # Minimizing player wins
    else:
        return 0   # Draw or game not finished


def get_children(board, maximizing_player):
    children = []
    player = 'X' if maximizing_player else 'O'

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                children.append(new_board)
    return children


def alphabeta(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)

    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(position, True):
            eval = alphabeta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(position, False):
            eval = alphabeta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval


# Example usage
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

score = alphabeta(initial_board, 9, float('-inf'), float('inf'), True)
print("Best evaluation score for X (maximizing player):", score)
