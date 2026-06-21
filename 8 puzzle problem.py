from heapq import heappush, heappop


def solve_8_puzzle(start, goal):
    open_list = []

    # Pre-calculate goal positions for O(1) lookups
    goal_positions = {val: (i, j) for i, row in enumerate(goal)
                      for j, val in enumerate(row) if val != 0}

    def calc_heuristic(state):
        h = 0
        for i in range(3):
            for j in range(3):
                val = state[i][j]
                if val != 0:
                    gi, gj = goal_positions[val]
                    h += abs(i - gi) + abs(j - gj)
        return h

    # Initialize priority queue with heuristic value (f = g + h)
    start_cost = calc_heuristic(start)
    heappush(open_list, (start_cost, start, []))

    closed_list = set()
    moves = [(0, -1, 'Left'), (0, 1, 'Right'), (-1, 0, 'Up'), (1, 0, 'Down')]

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

        zi, zj = zero_pos

        for di, dj, name in moves:
            new_i, new_j = zi + di, zj + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [current[0][:], current[1][:], current[2][:]]
                new_state[zi][zj] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0

                new_tuple = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                if new_tuple not in closed_list:
                    cost = len(path) + 1 + calc_heuristic(new_state)
                    heappush(open_list, (cost, new_state, path + [name]))
    return None


# Example usage:
start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print(solve_8_puzzle(start, goal))
