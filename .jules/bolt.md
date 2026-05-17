## 2024-06-25 - [Precomputing Goal Positions for 8-Puzzle]
**Learning:** The A* heuristic calculation (Manhattan distance) inside the inner search loop was re-evaluating the goal position for every tile in every state O(N^2), causing significant overhead.
**Action:** Precompute goal positions into a hash map before the search loop, turning coordinate lookups into O(1).
