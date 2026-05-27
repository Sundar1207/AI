## 2024-05-14 - [O(1) Heuristic Lookup in A* Search]
**Learning:** For coordinate-based heuristics (like Manhattan distance) where the goal state is static, searching for the goal position within the heuristic calculation creates a massive O(N^2) bottleneck for every state evaluated.
**Action:** Pre-calculate static goal positions into a dictionary before the search loop begins, replacing O(N^2) search loops with O(1) dictionary lookups. Additionally, always initialize the A* open list with the heuristic value `f = g + h` for the start state instead of `0` to ensure optimal search ordering.
