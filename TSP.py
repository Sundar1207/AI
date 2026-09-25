from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    # Handle 1-node edge case properly
    if not nodes:
        return [start, start], graph.get(start, {}).get(start, 0)

    min_path = None
    min_cost = float('inf')

    # Check if all weights are non-negative to safely apply branch and bound pruning
    can_prune = True
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                can_prune = False
                break
        if not can_prune:
            break

    for perm in permutations(nodes):
        # Calculate initial cost to first permutation node
        current_cost = graph[start][perm[0]]

        # Early pruning: break out if cost already exceeds minimum
        if can_prune and current_cost >= min_cost:
            continue

        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]
            if can_prune and current_cost >= min_cost:
                break
        else:
            # If the loop didn't break, add the cost of returning to start
            current_cost += graph[perm[-1]][start]
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
