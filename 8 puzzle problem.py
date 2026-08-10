from heapq import heappush, heappop


def solve_8_puzzle(start, goal):
    open_list = []
    # Pre-calculate goal positions for O(1) heuristic lookups
    goal_positions = {val: (i, j) for i, row in enumerate(goal)
                      for j, val in enumerate(row) if val != 0}

    def heuristic(state):
        return sum(abs(i - goal_positions[val][0]) + abs(j - goal_positions[val][1])
                   for i, row in enumerate(state)
                   for j, val in enumerate(row) if val != 0)

    # Initialize queue with heuristic value
    heappush(open_list, (0 + heuristic(start), start, []))
    closed_list = set()
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    move_names = ['Left', 'Right', 'Up', 'Down']

    while open_list:
        _, current, path = heappop(open_list)
        if current == goal:
            return path

        # Unroll tuple conversion to reduce overhead
        state_tuple = (tuple(current[0]), tuple(current[1]), tuple(current[2]))
        if state_tuple in closed_list:
            continue
        closed_list.add(state_tuple)

        zero_pos = next((i, j) for i, row in enumerate(current)
                        for j, val in enumerate(row) if val == 0)

        for move, name in zip(moves, move_names):
            new_i, new_j = zero_pos[0] + move[0], zero_pos[1] + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in current]
                new_state[zero_pos[0]][zero_pos[1]] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0

                # Unroll tuple conversion to reduce overhead
                new_state_tuple = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                if new_state_tuple not in closed_list:
                    cost = len(path) + 1 + heuristic(new_state)
                    heappush(open_list, (cost, new_state, path + [name]))
    return None


# Example usage:
start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print(solve_8_puzzle(start, goal))
