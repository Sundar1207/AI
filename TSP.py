from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Handle empty iterator edge case (1-node graph)
    if not nodes:
        return [start, start], graph[start][start]

    # Check for negative weights to determine if early pruning is safe
    has_negative_weights = any(weight < 0 for edges in graph.values() for weight in edges.values())

    for perm in permutations(nodes):
        current_cost = 0
        current_node = start

        # Calculate cost incrementally without building full path list
        for next_node in perm:
            current_cost += graph[current_node][next_node]
            # Early pruning (branch and bound)
            if not has_negative_weights and current_cost >= min_cost:
                break
            current_node = next_node
        else:
            # Add cost to return to start
            current_cost += graph[current_node][start]
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
