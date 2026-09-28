from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    # Handle 1-node graph edge case
    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    # Pre-check if all weights are non-negative to allow for early pruning (branch and bound)
    can_prune = all(w >= 0 for edges in graph.values() for w in edges.values())

    for perm in permutations(nodes):
        current_cost = graph[start][perm[0]]

        # Early pruning if cost already exceeds minimum
        if can_prune and current_cost >= min_cost:
            continue

        pruned = False
        prev = perm[0]

        # Incrementally calculate cost to avoid creating full path list on every iteration
        for node in perm[1:]:
            current_cost += graph[prev][node]
            if can_prune and current_cost >= min_cost:
                pruned = True
                break
            prev = node

        if pruned:
            continue

        current_cost += graph[prev][start]

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
