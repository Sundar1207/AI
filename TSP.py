from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    # Check if all weights are non-negative for early pruning
    all_non_negative = all(
        weight >= 0
        for edges in graph.values()
        for weight in edges.values()
    )

    for perm in permutations(nodes):
        current_cost = 0
        valid_path = True

        curr_node = start
        for next_node in perm:
            current_cost += graph[curr_node][next_node]
            # Early pruning if cost exceeds minimum and weights are non-negative
            if all_non_negative and current_cost >= min_cost:
                valid_path = False
                break
            curr_node = next_node

        if valid_path:
            current_cost += graph[curr_node][start]
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
