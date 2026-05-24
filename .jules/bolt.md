## 2024-05-24 - A* Heuristic Goal Pre-calculation
**Learning:** In A* search problems like the 8-puzzle where the goal state is static, calculating Manhattan Distance by iterating over both state and goal arrays on every step creates a massive O(N^2) bottleneck inside the inner loop.
**Action:** Always pre-calculate static goal states into a lookup dictionary {value: (row, col)} to turn O(N^2) search loops into O(1) hash map lookups.
