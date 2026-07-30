from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())

    if not nodes:
        return [], 0

    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Verify non-negative weights for early pruning (branch and bound)
    can_prune = all(weight >= 0 for edges in graph.values() for weight in edges.values())

    for perm in permutations(nodes):
        current_cost = 0
        prev_node = start
        possible = True

        for node in perm:
            current_cost += graph[prev_node][node]
            # Early pruning: break if current cost exceeds minimum found so far
            if can_prune and current_cost >= min_cost:
                possible = False
                break
            prev_node = node

        if possible:
            current_cost += graph[prev_node][start]
            if current_cost < min_cost:
                min_cost = current_cost
                # Avoid constructing full path array until a new minimum is found
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
