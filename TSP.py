from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Handle edge case for 1-node or empty graphs
    if not nodes:
        return [start, start], graph[start][start] if start in graph and start in graph[start] else float('inf')

    for perm in permutations(nodes):
        current_cost = graph[start][perm[0]]

        # Early pruning: stop if cost already exceeds minimum
        if current_cost >= min_cost:
            continue

        is_valid = True
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if current_cost >= min_cost:
                is_valid = False
                break

        if not is_valid:
            continue

        current_cost += graph[perm[-1]][start]

        if current_cost < min_cost:
            min_cost = current_cost
            # Construct path only when we find a new minimum
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
