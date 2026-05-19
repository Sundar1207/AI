## 2024-05-18 - Optimize A* Heuristic Lookups
**Learning:** In A* pathfinding problems with coordinate-based heuristics (like Manhattan distance) and static goal states, nesting the heuristic loop recalculates goal positions for every state evaluation, resulting in O(N^2) complexity where N is the grid size.
**Action:** Pre-calculate the goal positions into a hash map / dictionary for O(1) lookups before starting the A* search loop, dropping heuristic evaluation complexity to O(N).
