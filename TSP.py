from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Optimization: Check for negative weights to safely apply branch and bound pruning
    has_negative = any(weight < 0 for edges in graph.values() for weight in edges.values())

    # Optimization: Explicitly handle empty iterator edge case (1-node graph)
    if not nodes:
        return [start, start], graph[start][start]

    for perm in permutations(nodes):
        # Optimization: Incrementally calculate metrics over the iterator
        current_cost = graph[start][perm[0]]

        # Optimization: Early pruning (branch and bound)
        if not has_negative and current_cost >= min_cost:
            continue

        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if not has_negative and current_cost >= min_cost:
                break
        else:
            current_cost += graph[perm[-1]][start]
            if current_cost < min_cost:
                min_cost = current_cost
                # Optimization: Defer explicit path list construction until
                # a new minimum is actually found
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
