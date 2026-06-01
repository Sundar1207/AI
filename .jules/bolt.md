## 2024-05-24 - Pre-calculate goal positions in A* heuristics
**Learning:** O(N^2) inner loops in heuristic calculations for A* search (like finding Manhattan distance in sliding puzzles) cause massive overhead because the heuristic is called for every generated node.
**Action:** Always pre-calculate static goal positions into a dictionary for O(1) lookups before starting the search loop. Also initialize priority queues with the proper heuristic value (`f = g + h`) for the start state to ensure proper first-node ordering.
