def vacuum_cleaner_world():
    from collections import deque
    
    class State:
        def __init__(self, vacuum_pos, room_a, room_b, cost, path):
            self.vacuum_pos = vacuum_pos
            self.room_a = room_a
            self.room_b = room_b
            self.cost = cost
            self.path = path
        
        def __lt__(self, other):
            return self.cost < other.cost
    
    start = State('A', True, True, 0, [])
    queue = deque([start])
    visited = set()
    
    while queue:
        current = queue.popleft()
        state_key = (current.vacuum_pos, current.room_a, current.room_b)
        
        if state_key in visited:
            continue
        visited.add(state_key)
        
        if not current.room_a and not current.room_b:
            return current.path
        
        if current.vacuum_pos == 'A':
            # Clean A
            new_state = State('A', False, current.room_b, current.cost + 1, current.path + ["Clean A"])
            queue.append(new_state)
            # Move to B
            new_state = State('B', current.room_a, current.room_b, current.cost + 1, current.path + ["Move to B"])
            queue.append(new_state)
        else:
            # Clean B
            new_state = State('B', current.room_a, False, current.cost + 1, current.path + ["Clean B"])
            queue.append(new_state)
            # Move to A
            new_state = State('A', current.room_a, current.room_b, current.cost + 1, current.path + ["Move to A"])
            queue.append(new_state)
    
    return None

print("\n".join(vacuum_cleaner_world()))
