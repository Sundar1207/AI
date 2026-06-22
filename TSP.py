from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        # ⚡ Bolt Optimization: Early pruning and incremental cost calculation.
        # Avoid creating the full list representation of the path inside the loop.
        current_cost = graph[start][perm[0]]

        # Early pruning for first edge
        if current_cost >= min_cost:
            continue

        possible = True
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            # Prune path if it already exceeds or equals min_cost
            if current_cost >= min_cost:
                possible = False
                break

        if possible:
            current_cost += graph[perm[-1]][start]
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
