from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Handle empty permutations edge case (e.g. 1-node graph)
    if not nodes:
        return [start, start], graph[start].get(start, 0)

    # Check if we can safely use branch and bound (all weights >= 0)
    can_prune = True
    for u in graph.values():
        for weight in u.values():
            if weight < 0:
                can_prune = False
                break
        if not can_prune:
            break

    # Cache start edges for faster lookup
    start_edges = graph[start]

    for perm in permutations(nodes):
        current_cost = start_edges[perm[0]]

        # Early pruning: exit loops immediately if the current path cost exceeds the best
        # known minimum
        if can_prune and current_cost >= min_cost:
            continue

        pruned = False
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                pruned = True
                break

        if pruned:
            continue

        current_cost += graph[perm[-1]][start]

        if current_cost < min_cost:
            min_cost = current_cost
            # Defer explicit path list construction until a new minimum is actually found
            min_path = perm

    if min_path is None:
        return None, float('inf')

    return [start] + list(min_path) + [start], min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
