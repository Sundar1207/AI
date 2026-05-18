## 2024-06-13 - [Precomputing heuristics for static goals]
**Learning:** For coordinate-based heuristics (like Manhattan distance in A* Search) where the goal state is static, comparing every element against every element in the goal state leads to an O(N^2) inner loop.
**Action:** Always pre-calculate static goal positions into a hash map / dictionary to replace O(N^2) loops with O(1) lookups.
