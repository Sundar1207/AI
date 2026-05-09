from ttt_utils import game_over, evaluate, get_children

def minimax(position, depth, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(position, True):
            eval_score = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(position, False):
            eval_score = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval_score)
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
