## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Avoid Generator overhead in highly recursive tree search
**Learning:** Generator expressions inside built-in functions like `all()` (e.g., `all(cell != ' ' for row in board for cell in row)`) in hot loops of highly recursive search trees (like Alpha-Beta Pruning) incur significant generator initialization overhead and function call overhead.
**Action:** Replace `all()` checks containing generator expressions with explicit, nested `for` loops and early returns in hot paths to completely bypass object allocation and generator overhead.
