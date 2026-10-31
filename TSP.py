from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    # Optimization: explicitly handle empty iterator edge cases for 1-node graphs
    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Optimization: Check if we can prune branches (verify edge weights are non-negative)
    can_prune = all(w >= 0 for u in graph for w in graph[u].values())

    for perm in permutations(nodes):
        # Optimization: Avoid constructing full current_path list on every iteration
        current_cost = graph[start][perm[0]]

        for i in range(len(perm) - 1):
            # Optimization: Early pruning if path cost exceeds best known minimum
            if can_prune and current_cost >= min_cost:
                break
            current_cost += graph[perm[i]][perm[i+1]]
        else:
            current_cost += graph[perm[-1]][start]

            if current_cost < min_cost:
                min_cost = current_cost
                # Optimization: Defer explicit path list construction until new minimum is found
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
