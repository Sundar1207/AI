from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')
    can_prune = all(w >= 0 for edges in graph.values() for w in edges.values())

    for perm in permutations(nodes):
        current_cost = 0
        curr_node = start
        pruned = False

        for next_node in perm:
            current_cost += graph[curr_node][next_node]
            if can_prune and current_cost >= min_cost:
                pruned = True
                break
            curr_node = next_node

        if not pruned:
            current_cost += graph[curr_node][start]
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
