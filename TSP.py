from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    if len(nodes) <= 1:
        return [start, start] if nodes else [], graph[start][start] if nodes else 0

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        # Initial cost from start node to the first node in the permutation
        current_cost = graph[start][perm[0]]
        if current_cost >= min_cost:
            continue

        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            # Early pruning: if path cost already exceeds minimum, abandon this path
            if current_cost >= min_cost:
                break
        else:
            # Add cost to return to start node
            current_cost += graph[perm[-1]][start]
            if current_cost < min_cost:
                min_cost = current_cost
                # Defer explicit path list construction until a new minimum is actually found
                min_path = [start] + list(perm) + [start]

    return min_path, min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
