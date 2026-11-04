def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    # Edge case for 1-node graphs
    if not nodes:
        return [start, start], graph[start][start]

    min_path = None
    min_cost = float('inf')

    # Check for negative weights for valid pruning
    has_negative = False
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                has_negative = True
                break
        if has_negative:
            break

    # Optimization: DFS backtracking to completely prune branches
    def dfs(current_node, visited_count, current_cost, path):
        nonlocal min_cost, min_path

        # Pruning
        if not has_negative and current_cost >= min_cost:
            return

        if visited_count == len(nodes):
            total_cost = current_cost + graph[current_node][start]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = list(path) + [start]
            return

        for next_node in nodes:
            if not visited[next_node]:
                visited[next_node] = True
                path.append(next_node)
                dfs(next_node, visited_count + 1, current_cost +
                    graph[current_node][next_node], path)
                path.pop()
                visited[next_node] = False

    visited = {node: False for node in nodes}
    dfs(start, 0, 0, [start])

    return min_path, min_cost


# Example usage:
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(traveling_salesman(graph, 'A'))
