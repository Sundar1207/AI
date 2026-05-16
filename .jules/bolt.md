
## 2024-05-24 - [O(1) Heuristic Pre-calculation for A* Search]
**Learning:** For coordinate-based heuristics (like Manhattan distance) where the goal state is static, repeatedly scanning the goal state during evaluation causes O(N^2) inner search loops.
**Action:** Optimize performance by pre-calculating goal positions into a dictionary once at the start of the search to replace O(N^2) inner loops with O(1) lookups.
