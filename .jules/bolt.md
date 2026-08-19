## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-08-19 - Branch and Bound Pruning in TSP
**Learning:** Generating full array representations and summing edges unconditionally in permutation-based TSP implementations leads to high object allocation overhead and O(N!) unnecessary additions.
**Action:** Incrementally calculate paths inside the permutation iterator and use early branch-and-bound pruning (breaking if `current_cost >= min_cost` when no negative weights exist) to exit early, avoiding both array creation and further summation.
