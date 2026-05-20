## 2026-05-20 - Pre-calculate static goals for O(1) heuristic lookups
**Learning:** For coordinate-based heuristics (like Manhattan distance) where the goal state is static, computing the target coordinates dynamically inside the search loop results in O(N^2) inner lookups (or O(N^4) overall).
**Action:** Pre-calculate goal positions into a dictionary before starting the search to replace O(N^2) inner search loops with O(1) lookups.
