from itertools import permutations


def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    # Check if all edges are non-negative for branch and bound pruning
    all_non_negative = True
    for edges in graph.values():
        for weight in edges.values():
            if weight < 0:
                all_non_negative = False
                break
        if not all_non_negative:
            break

    num_nodes_minus_one = len(nodes) - 1
    start_edges = graph[start]

    if all_non_negative:
        for perm in permutations(nodes):
            current_cost = start_edges[perm[0]]

            for i in range(num_nodes_minus_one):
                # Branch and bound early pruning
                if current_cost >= min_cost:
                    break
                current_cost += graph[perm[i]][perm[i+1]]
            else:
                current_cost += graph[perm[-1]][start]
                if current_cost < min_cost:
                    min_cost = current_cost
                    # Avoid constructing the path list until a new minimum is actually found
                    min_path = [start] + list(perm) + [start]
    else:
        for perm in permutations(nodes):
            current_cost = start_edges[perm[0]]

            for i in range(num_nodes_minus_one):
                current_cost += graph[perm[i]][perm[i+1]]
            else:
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
