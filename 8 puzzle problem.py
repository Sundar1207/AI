from heapq import heappush, heappop

def solve_8_puzzle(start, goal):
    # Precompute goal positions for O(1) lookup in heuristic calculation.
    # This optimizes the nested loops in the original heuristic calculation,
    # dropping complexity per heuristic call.
    goal_pos = {val: (gi, gj) for gi, grow in enumerate(goal) for gj, val in enumerate(grow) if val != 0}

    def heuristic(state):
        return sum(abs(i - goal_pos[val][0]) + abs(j - goal_pos[val][1])
                   for i, row in enumerate(state)
                   for j, val in enumerate(row) if val != 0)

    open_list = []
    heappush(open_list, (0, start, []))
    closed_list = set()
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    move_names = ['Left', 'Right', 'Up', 'Down']
    
    while open_list:
        _, current, path = heappop(open_list)
        if current == goal:
            return path
        
        state_tuple = tuple(tuple(row) for row in current)
        if state_tuple in closed_list:
            continue
        closed_list.add(state_tuple)
        
        zero_pos = next((i, j) for i, row in enumerate(current) for j, val in enumerate(row) if val == 0)
        
        for move, name in zip(moves, move_names):
            new_i, new_j = zero_pos[0] + move[0], zero_pos[1] + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in current]
                new_state[zero_pos[0]][zero_pos[1]] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0

                new_state_tuple = tuple(tuple(row) for row in new_state)
                if new_state_tuple not in closed_list:
                    cost = len(path) + 1 + heuristic(new_state)
                    heappush(open_list, (cost, new_state, path + [name]))
    return None

# Example usage:
start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print(solve_8_puzzle(start, goal))
