## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Early Pruning in Permutation Iterators
**Learning:** For algorithmic search implementations (like TSP or brute-force permutations), building full array representations (e.g., `list(perm)`) inside the main loop destroys performance due to object allocation overhead.
**Action:** Incrementally calculate metrics directly over the iterator elements and use early pruning (`if current_cost >= min_cost: break`) to exit loops immediately. Also, handle empty iterator edge cases (like 1-node graphs) before the loop to prevent `IndexError` on tuple indexing.
