def game_over(board):
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def winner(board):
    # Rows
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # Columns
    for j in range(3):
        if board[0][j] != ' ' and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
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
