from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    # Pre-check if early pruning is safe (no negative weights)
    can_prune = all(cost >= 0 for edges in graph.values() for cost in edges.values())

    for perm in permutations(nodes):
        # Calculate initial step cost
        current_cost = graph[start][perm[0]]
        if can_prune and current_cost >= min_cost:
            continue

        # Accumulate cost and prune early if cost exceeds min_cost
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                break
        else:
            # If loop completes without breaking, calculate return to start
            current_cost += graph[perm[-1]][start]
            if current_cost < min_cost:
                min_cost = current_cost
                # Only construct the full path list when a new minimum is found
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
