from itertools import permutations


def traveling_salesman(graph, start):
    """
    Solves the Traveling Salesman Problem using brute force.
    Includes memory optimizations and branch and bound pruning for non-negative edge weights.
    """
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Handle edge case where there's only 1 node in the graph
    if not nodes:
        return [start, start], graph[start][start]

    # Pruning is only safe if there are no negative edge weights in the graph
    has_negative_weights = any(
        weight < 0 for row in graph.values() for weight in row.values()
    )

    for perm in permutations(nodes):
        current_cost = 0
        prev_node = start

        # Incrementally calculate cost
        for node in perm:
            current_cost += graph[prev_node][node]
            # Prune if cost exceeds min_cost and we are guaranteed it won't decrease
            if not has_negative_weights and current_cost >= min_cost:
                break
            prev_node = node

        if not has_negative_weights and current_cost >= min_cost:
            continue

        current_cost += graph[prev_node][start]

        if current_cost < min_cost:
            min_cost = current_cost
            # Construct the path only when a new minimum is found
            min_path = [start] + list(perm) + [start]

    return min_path, min_cost


if __name__ == '__main__':
    # Example usage:
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    print(traveling_salesman(graph, 'A'))
