from collections import deque

def is_valid(state):
    ml, cl, mr, cr, _ = state
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
        return False
    return True

def solve_missionaries_cannibals():
    start = (3, 3, 0, 0, 'L')  # boat starts on left
    goal = (0, 0, 3, 3, 'R')   # goal includes boat on right
    visited = set()
    queue = deque([(start, [])])
    
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        
        if state in visited:
            continue
        visited.add(state)
        
        ml, cl, mr, cr, boat = state
        
        if boat == 'L':
            # Move boat from left to right
            for m, c in moves:
                new_state = (ml - m, cl - c, mr + m, cr + c, 'R')
                if is_valid(new_state):
                    action = f"Move {m} missionaries and {c} cannibals from left to right"
                    queue.append((new_state, path + [action]))
        else:
            # Move boat from right to left
            for m, c in moves:
                new_state = (ml + m, cl + c, mr - m, cr - c, 'L')
                if is_valid(new_state):
                    action = f"Move {m} missionaries and {c} cannibals from right to left"
                    queue.append((new_state, path + [action]))
    
    return None

result = solve_missionaries_cannibals()
if result:
    print("\n".join(result))
else:
    print("No solution found.")
