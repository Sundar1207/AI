## 2024-05-14 - A* Search Heuristic Optimization
**Learning:** In A* search algorithms (like the 8-puzzle solver) where the goal state is static, recalculating the target coordinate for every node evaluation using an inner search loop creates a significant O(N^2) bottleneck.
**Action:** Always pre-calculate static goal positions into a hash map/dictionary at the start of the search to enable O(1) coordinate lookups during heuristic calculation (e.g., Manhattan distance).
