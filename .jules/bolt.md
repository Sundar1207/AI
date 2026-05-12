## 2024-05-24 - Precomputing Goal State for A* Heuristics
**Learning:** In A* search algorithms (like 8-puzzle), the heuristic function is called thousands of times. Calculating goal distances by scanning the entire goal state for every heuristic call creates a massive O(N^4) bottleneck.
**Action:** Always precompute static target states into O(1) lookup tables (like a hash map of value -> coordinates) before starting the search loop.
