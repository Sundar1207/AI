## 2024-05-24 - O(n) Heuristic Optimization in A* Search
**Learning:** Nested loops checking element positions in a 2D array (e.g., Manhattan distance in 8-puzzle) can be extremely expensive when called frequently inside pathfinding loops.
**Action:** When a static reference grid (like a goal state) is used repeatedly inside an inner loop, pre-compute its coordinates into an O(1) lookup dictionary (hash map) before the loop starts.
