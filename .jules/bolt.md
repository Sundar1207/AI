## 2024-05-24 - Early Pruning in Search Algorithms
**Learning:** When calculating the minimum cost across multiple permutations or paths, computing the entire cost for a suboptimal path is wasteful.
**Action:** Always add early exits (e.g., `if current_cost >= min_cost: break`) inside cost calculation loops to immediately abandon suboptimal paths as soon as they exceed the known minimum.
