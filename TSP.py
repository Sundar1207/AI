from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    can_prune = True
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                can_prune = False
                break
        if not can_prune:
            break

    min_path_tuple = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        current_cost = graph[start][perm[0]]

        if can_prune and current_cost >= min_cost:
            continue

        valid = True
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                valid = False
                break

        if not valid:
            continue

        current_cost += graph[perm[-1]][start]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path_tuple = perm

    if min_path_tuple is None:
        return None, float('inf')

    min_path = [start] + list(min_path_tuple) + [start]
    return min_path, min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
