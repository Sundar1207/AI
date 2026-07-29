from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    # Handle single node case explicitly to avoid IndexError on perm[0]
    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Verify if all weights are non-negative to safely apply early pruning
    can_prune = all(weight >= 0 for edges in graph.values() for weight in edges.values())

    for perm in permutations(nodes):
        # Calculate cost incrementally, starting with the edge from start to first node in perm
        current_cost = graph[start][perm[0]]

        # Early pruning: if cost already exceeds min_cost, skip this permutation
        if can_prune and current_cost >= min_cost:
            continue

        possible = True
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                possible = False
                break

        if not possible:
            continue

        current_cost += graph[perm[-1]][start]

        # Only construct full path array if we found a new minimum
        if current_cost < min_cost:
            min_cost = current_cost
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
