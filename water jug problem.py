from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0, [])])
    
    while queue:
        a, b, path = queue.popleft()
        
        if a == target or b == target:
            return path
        
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        # Fill jug A
        if (capacity_a, b) not in visited:
            queue.append((capacity_a, b, path + ["Fill A"]))
        
        # Fill jug B
        if (a, capacity_b) not in visited:
            queue.append((a, capacity_b, path + ["Fill B"]))
        
        # Empty jug A
        if (0, b) not in visited:
            queue.append((0, b, path + ["Empty A"]))
        
        # Empty jug B
        if (a, 0) not in visited:
            queue.append((a, 0, path + ["Empty B"]))
        
        # Pour from A to B
        pour_amount = min(a, capacity_b - b)
        if (a - pour_amount, b + pour_amount) not in visited:
            queue.append((a - pour_amount, b + pour_amount, path + ["Pour A to B"]))
        
        # Pour from B to A
        pour_amount = min(b, capacity_a - a)
        if (a + pour_amount, b - pour_amount) not in visited:
            queue.append((a + pour_amount, b - pour_amount, path + ["Pour B to A"]))
    
    return None

print(water_jug_bfs(4, 3, 2))  # Example: 4-gallon and 3-gallon jugs, target 2 gallons
