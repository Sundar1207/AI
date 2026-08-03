from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())

    # Handle empty iterator edge case (1-node graph)
    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Verify non-negative weights for safe early pruning
    can_prune = all(w >= 0 for edges in graph.values() for w in edges.values())

    for perm in permutations(nodes):
        current_cost = graph[start][perm[0]]

        # Early pruning: if initial edge cost exceeds min_cost
        if can_prune and current_cost >= min_cost:
            continue

        pruned = False
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            # Early pruning: break if current partial cost exceeds min_cost
            if can_prune and current_cost >= min_cost:
                pruned = True
                break

        if pruned:
            continue

        current_cost += graph[perm[-1]][start]

        if current_cost < min_cost:
            min_cost = current_cost
            # Defer path list construction until a new minimum is found
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
