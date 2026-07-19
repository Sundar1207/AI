## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-07-19 - Avoid Generator Expressions with all()/any() in Recursive Search Checks
**Learning:** Using `all(cell != ' ' for row in board for cell in row)` for leaf-node evaluation checks (like `game_over`) creates significant generator instantiation overhead when called repeatedly in search trees like Alpha-Beta pruning.
**Action:** Replace generator expressions with explicit nested loops and early returns. This eliminates generator creation and provides immediate short-circuiting, resulting in ~4x overall speedup in `Alpha Beta.py`.
