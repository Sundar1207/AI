## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Avoid Functional Map for Tuple Conversions in Hot Loops
**Learning:** In A* search or algorithms evaluating grid states continuously, using `tuple(map(tuple, state))` to create immutable hashable states for caching in `closed_list` generates significant object allocation overhead. In `8 puzzle problem.py`, explicit tuple conversions per row provide a large performance boost.
**Action:** Unroll nested tuple creations for small fixed-size grids, e.g., `(tuple(state[0]), tuple(state[1]), tuple(state[2]))`.
