## 2024-05-24 - TSP Early Pruning
**Learning:** In permutation-based algorithms like TSP, constructing the full path array and calculating the total cost on every iteration is slow.
**Action:** Incrementally calculate the cost and prune the path early if it exceeds the current known minimum cost to speed up evaluation without sacrificing correctness.
