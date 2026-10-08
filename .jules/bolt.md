## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Early exit `in` operator avoids nested generator overhead
**Learning:** Using `all(cell != ' ' for row in board for cell in row)` for game-over checks dynamically creates generators per check. In hot recursive tree loops (e.g., `Alpha Beta.py`), replacing this with explicit `if ' ' in row: return False` using Python's highly optimized, C-level `in` operator avoids instantiation overhead and reduces game-over check time significantly.
**Action:** Replace generator `all()` or `any()` usage in matrix empty-checking functions with nested loops testing `if item in row`.
