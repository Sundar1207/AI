from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    # Handle 1-node graph edge case
    if not nodes:
        return [start, start], graph[start].get(start, 0)

    min_path = None
    min_cost = float('inf')

    # Check if all weights are non-negative for branch and bound
    can_prune = all(weight >= 0 for edges in graph.values() for weight in edges.values())

    for perm in permutations(nodes):
        current_cost = 0
        prev_node = start

        for node in perm:
            current_cost += graph[prev_node][node]
            if can_prune and current_cost >= min_cost:
                break
            prev_node = node
        else:
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
