from itertools import permutations

def traveling_salesman_orig(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        current_cost = 0
        current_path = [start] + list(perm) + [start]

        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i+1]]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path

    return min_path, min_cost

def traveling_salesman_opt(graph, start):
    nodes = list(graph.keys())
    if len(nodes) == 1:
        return [start, start], graph[start][start]

    nodes.remove(start)
    min_path = None
    min_cost = float('inf')

    can_prune = all(w >= 0 for u in graph for w in graph[u].values())

    for perm in permutations(nodes):
        current_cost = graph[start][perm[0]]

        for i in range(len(perm) - 1):
            if can_prune and current_cost >= min_cost:
                break
            current_cost += graph[perm[i]][perm[i+1]]
        else:
            current_cost += graph[perm[-1]][start]

            if current_cost < min_cost:
                min_cost = current_cost
                min_path = [start] + list(perm) + [start]

    return min_path, min_cost

import time
import random

random.seed(42)

# Generate a slightly larger graph
n = 10
graph = {i: {j: random.randint(10, 100) if i != j else 0 for j in range(n)} for i in range(n)}

start_time = time.time()
ans_orig = traveling_salesman_orig(graph, 0)
orig_time = time.time() - start_time

start_time = time.time()
ans_opt = traveling_salesman_opt(graph, 0)
opt_time = time.time() - start_time

print("Orig ans:", ans_orig)
print("Opt ans:", ans_opt)
print("Orig time:", orig_time)
print("Opt time:", opt_time)

# test 1 node
graph_1 = {0: {0: 42}}
print("Orig 1:", traveling_salesman_orig(graph_1, 0))
print("Opt 1:", traveling_salesman_opt(graph_1, 0))
