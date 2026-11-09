def winner(board):
    # Optimization: Hardcoded array index comparisons instead of dynamic list comprehensions
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


def minimax(position, depth, maximizing_player):
    # Optimization: Inline evaluate logic to avoid extra game_over checks
    w = winner(position)
    if w is not None:
        return 1 if w == 'X' else -1
    is_full = True
    for row in position:
        if ' ' in row:
            is_full = False
            break
    if depth == 0 or is_full:
        return 0

    player = 'X' if maximizing_player else 'O'

    if maximizing_player:
        max_eval = float('-inf')
        # Optimization: Inline get_children and use backtracking to avoid copying
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = minimax(position, depth - 1, False)
                    position[i][j] = ' '
                    if eval > max_eval:
                        max_eval = eval
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if position[i][j] == ' ':
                    position[i][j] = player
                    eval = minimax(position, depth - 1, True)
                    position[i][j] = ' '
                    if eval < min_eval:
                        min_eval = eval
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
