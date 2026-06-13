## 2024-05-24 - TSP Optimization
**Learning:** For algorithmic search implementations like TSP, calculating metrics incrementally over an iterator and applying early pruning (`if current_cost >= min_cost: break`) combined with avoiding full array instantiations speeds up execution significantly (~3x faster). Empty iterator cases for 1-node graphs should be handled explicitly.
**Action:** Apply early pruning and avoid full sequence list conversion inside iterative permutations to optimize exhaustive search algorithms.
