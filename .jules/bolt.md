## 2024-05-10 - O(N^2) to O(N) Heuristic Optimization in Search Algorithms
**Learning:** In combinatorial search algorithms like A* for the 8-puzzle, calculating the Manhattan distance heuristic can be a significant bottleneck if the goal state is iterated over repeatedly (resulting in an O(N^2) operation per node evaluation).
**Action:** When working with search algorithms that repeatedly compute a distance metric against a fixed goal state, always precompute the goal state coordinates into a hash map or lookup table before the search loop begins, reducing the heuristic calculation to O(N).
