## 2024-05-18 - A* Heuristic Complexity
**Learning:** In A* implementations, calculating Manhattan distance via nested loops inside the heuristic function against the goal state is extremely slow and results in O(N^4) operations, creating a significant bottleneck. A static goal allows pre-calculating the goal tile positions.
**Action:** Always pre-calculate the goal target coordinate map `{val: (i, j)}` once outside the loop for static goals in A* search, and pass it into the heuristic to enable O(1) coordinate lookups per tile.
