## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-08-06 - In-place Backtracking for Tree Search
**Learning:** In highly recursive tree searches (like Minimax and Alpha-Beta), avoiding full copies of state arrays for each child state significantly reduces object allocation overhead. Profiling showed that eliminating `[row[:] for row in board]` and using in-place state modification (backtracking) provides a ~6x speedup.
**Action:** When implementing or optimizing recursive tree search algorithms, use in-place state modification (backtracking) within the recursive loop to eliminate object allocation overhead and garbage collection pressure.
