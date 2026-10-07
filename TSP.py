from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Dynamically verify all edge weights are non-negative to safely apply early pruning
    can_prune = True
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                can_prune = False
                break
        if not can_prune:
            break

    for perm in permutations(nodes):
        if not perm:
            current_cost = graph[start][start]
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = [start, start]
            continue

        current_cost = graph[start][perm[0]]
        if can_prune and current_cost >= min_cost:
            continue

        pruned = False
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                pruned = True
                break

        if not pruned:
            current_cost += graph[perm[-1]][start]
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
