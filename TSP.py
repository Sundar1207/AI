from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    # Handle empty iterator edge case (1-node graph)
    if not nodes:
        return [start, start], graph[start][start]

    # Dynamically verify all edge weights are non-negative for early pruning
    all_non_negative = True
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                all_non_negative = False
                break
        if not all_non_negative:
            break

    min_path = None
    min_cost = float('inf')

    # Avoid constructing full array representations inside the main loop
    for perm in permutations(nodes):
        current_cost = 0
        prev_node = start
        pruned = False

        # Incrementally calculate metrics over the iterator
        for node in perm:
            current_cost += graph[prev_node][node]
            # Early pruning: exit loop if path cost exceeds the best known minimum
            if all_non_negative and current_cost >= min_cost:
                pruned = True
                break
            prev_node = node

        if not pruned:
            current_cost += graph[prev_node][start]
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
