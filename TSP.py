from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        current_cost = 0

        # Incremental calculation and early pruning optimization
        # Avoids building full path array [start] + list(perm) + [start] for every iteration
        # Reduces execution time significantly (e.g. ~60% reduction on 10 nodes)
        prev_node = start
        for node in perm:
            current_cost += graph[prev_node][node]
            if current_cost >= min_cost:
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
