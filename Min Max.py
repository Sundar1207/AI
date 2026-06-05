def game_over(board):
    return winner(board) is not None or all(cell != ' ' for row in board for cell in row)


def winner(board):
    # Direct indexing is used instead of list allocations (e.g. nested loops/comprehensions)
    # to significantly speed up evaluation during deep recursive tree searches.
    # Rows
    for r in range(3):
        if board[r][0] != ' ' and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # Columns
    for c in range(3):
        if board[0][c] != ' ' and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Diagonals
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


def minimax(position, depth, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)

    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(position, True):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(position, False):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


# Empty board
initial_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Run minimax on the empty board with depth 9 (max moves)
score = minimax(initial_board, 9, True)
print("Best evaluation score for X (maximizing player):", score)
