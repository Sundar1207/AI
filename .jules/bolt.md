## 2024-06-25 - A* Heuristic Loop Bottleneck
**Learning:** In grid-based pathfinding algorithms like the 8-puzzle A* search, calculating Manhattan distance dynamically by iterating over both the current state and the goal state creates an O(N^2) inner loop.
**Action:** Always pre-compute static goal positions into a hash map (dictionary) before starting the search loop. This allows O(1) coordinate lookups for the heuristic, dramatically improving performance (e.g., 2x speedup on hard puzzles). Also ensure priority queues are initialized with their correct heuristic values instead of `0`.
