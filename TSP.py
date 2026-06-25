from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())

    # Handle the 1-node graph edgecase explicitly
    if len(nodes) <= 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        current_cost = 0
        prev_node = start

        # Incremental cost calculation and early pruning
        for next_node in perm:
            current_cost += graph[prev_node][next_node]
            # Prune early if the current path is already more expensive than the minimum found
            if current_cost >= min_cost:
                break
            prev_node = next_node
        else:
            # Re-connect to start if we didn't break early
            current_cost += graph[prev_node][start]
            if current_cost < min_cost:
                min_cost = current_cost
                # Avoid constructing the full list for every permutation
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
