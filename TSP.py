def traveling_salesman(graph, start):
    # Optimization: Use DFS backtracking with branch-and-bound pruning
    # to avoid memory allocation overhead and skip pruned branches.
    nodes = list(graph.keys())

    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)

    can_prune = True
    for edges in graph.values():
        for weight in edges.values():
            if weight < 0:
                can_prune = False
                break
        if not can_prune:
            break

    min_cost = float('inf')
    min_path = None

    current_path = [start]
    visited = {start}

    def dfs(current_node, current_cost):
        nonlocal min_cost, min_path

        if can_prune and current_cost >= min_cost:
            return

        if len(current_path) == len(graph):
            total_cost = current_cost + graph[current_node][start]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = current_path + [start]
            return

        for next_node in nodes:
            if next_node not in visited:
                visited.add(next_node)
                current_path.append(next_node)

                dfs(next_node, current_cost + graph[current_node][next_node])

                current_path.pop()
                visited.remove(next_node)

    dfs(start, 0)

    return min_path, min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
