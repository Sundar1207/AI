from heapq import heappush, heappop


def solve_8_puzzle(start, goal):
    goal_pos = {val: (i, j) for i, row in enumerate(goal) for j, val in enumerate(row) if val != 0}
    initial_h = heuristic(start, goal_pos)

    open_list = []
    heappush(open_list, (initial_h, start, []))
    closed_list = set()
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    move_names = ['Left', 'Right', 'Up', 'Down']

    while open_list:
        _, current, path = heappop(open_list)
        if current == goal:
            return path

        current_tuple = (tuple(current[0]), tuple(current[1]), tuple(current[2]))
        if current_tuple in closed_list:
            continue
        closed_list.add(current_tuple)

        zero_pos = None
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    zero_pos = (i, j)
                    break
            if zero_pos:
                break

        for move, name in zip(moves, move_names):
            new_i, new_j = zero_pos[0] + move[0], zero_pos[1] + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in current]
                new_state[zero_pos[0]][zero_pos[1]] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0

                new_tuple = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                if new_tuple not in closed_list:
                    cost = len(path) + 1 + heuristic(new_state, goal_pos)
                    heappush(open_list, (cost, new_state, path + [name]))
    return None


def heuristic(state, goal):
    # Support both 2D list and pre-calculated dict for backwards compatibility
    if isinstance(goal, dict):
        goal_pos = goal
    else:
        goal_pos = {val: (i, j) for i, row in enumerate(goal)
                    for j, val in enumerate(row) if val != 0}

    h = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gi, gj = goal_pos[val]
                h += abs(i - gi) + abs(j - gj)
    return h


if __name__ == '__main__':
    # Example usage:
    start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    print(solve_8_puzzle(start, goal))
