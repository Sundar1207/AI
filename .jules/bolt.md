## 2024-06-09 - Optimize algorithmic search loops
**Learning:** For algorithmic search implementations (like TSP or brute-force permutations), avoid constructing full array representations (e.g., `[start] + list(perm) + [start]`) inside the main loop. These dynamic list allocations introduce unnecessary overhead.
**Action:** Instead, incrementally calculate metrics over the iterator and use early pruning to exit loops immediately if the current path cost exceeds the best known minimum cost (`if current_cost >= min_cost: break`).
