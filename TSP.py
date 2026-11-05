def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    # Optimization: Handle edge cases like 1-node graphs
    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    # Optimization: Check for negative weights to safely apply branch and bound pruning
    has_negative_weights = any(
        weight < 0 for edges in graph.values() for weight in edges.values()
    )

    # Optimization: Use DFS backtracking with branch-and-bound
    def dfs(curr_node, current_cost, path):
        nonlocal min_cost, min_path

        # Optimization: Early pruning (branch and bound)
        if not has_negative_weights and current_cost >= min_cost:
            return

        if len(path) == len(nodes) + 1:
            total_cost = current_cost + graph[curr_node][start]
            if total_cost < min_cost:
                min_cost = total_cost
                # Optimization: Defer explicit path list construction
                min_path = path + [start]
            return

        for next_node in nodes:
            if next_node not in path:
                dfs(
                    next_node,
                    current_cost + graph[curr_node][next_node],
                    path + [next_node]
                )

    dfs(start, 0, [start])
    return min_path, min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
