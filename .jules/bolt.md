## 2024-05-11 - [O(1) Map Lookups for Heuristic Targets]
**Learning:** In search algorithms (like A* in `8 puzzle problem.py`), recalculating target positions during heuristic evaluation is a major bottleneck because the heuristic is called for every generated child state.
**Action:** Always precompute static goal coordinates into a hash map before initiating the search loop to change target lookups from O(N^2) to O(1).
