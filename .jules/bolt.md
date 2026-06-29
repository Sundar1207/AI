## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Early Branch Pruning in Exhaustive TSP Search
**Learning:** Generating the full path array and unconditionally summing path costs inside permutation loops in `TSP.py` creates massive overhead. By accumulating the cost sequentially and applying early pruning (`if current_cost >= min_cost: break`), we can skip exploring the rest of a permutation branch as soon as it becomes sub-optimal. Note: this assumes all edge weights are non-negative.
**Action:** Use branch-and-bound logic directly within the permutation generator loop instead of list conversions and post-generation evaluation. Handle the 1-node graph edge case manually.
