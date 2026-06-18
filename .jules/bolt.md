## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Early pruning and reducing allocation in TSP permutations
**Learning:** In combinatorial searches like TSP iterating over `permutations()`, constructing full array representations inside the loop (e.g., `list(perm)`) and fully summing costs before comparison creates significant CPU overhead and memory allocation delays.
**Action:** Use an incremental cost summation approach with early exit conditions (`if current_cost >= min_cost: break`). Avoid generating full sub-arrays when traversing nodes. This simple early pruning step yielded a ~40% speedup in `TSP.py`.
