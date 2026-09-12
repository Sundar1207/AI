from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Check if there are edges with negative weights for safety
    has_negative = any(cost < 0 for u in graph for cost in graph[u].values())

    # Handle single node case gracefully
    if not nodes:
        return [start, start], graph[start].get(start, 0)

    for perm in permutations(nodes):
        current_cost = 0
        u = start

        # Calculate cost incrementally with branch and bound pruning
        for v in perm:
            current_cost += graph[u][v]
            if not has_negative and current_cost >= min_cost:
                break
            u = v

        if not has_negative and current_cost >= min_cost:
            continue

        current_cost += graph[u][start]

        if current_cost < min_cost:
            min_cost = current_cost
            # Defer explicit path list construction until a new minimum is found
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
