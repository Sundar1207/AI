from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())

    # Handle edgecase for 1-node graph
    if len(nodes) <= 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Pre-verify non-negative weights for safe early pruning
    can_prune = all(weight >= 0 for u in graph for weight in graph[u].values())

    for perm in permutations(nodes):
        current_cost = 0
        curr_node = start
        pruned = False

        # Incrementally calculate cost and check against min_cost
        for next_node in perm:
            current_cost += graph[curr_node][next_node]
            # Early pruning (branch and bound)
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
if __name__ == '__main__':
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    print(traveling_salesman(graph, 'A'))
