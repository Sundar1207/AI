## 2024-06-06 - Tic-Tac-Toe heuristic evaluation optimization
**Learning:** In 3x3 static grid evaluations (like Tic-Tac-Toe), highly recursive algorithms (such as Minimax or Alpha-Beta pruning) incur significant memory allocation and processing overhead when using generalized array manipulations like list comprehensions to check for winners.
**Action:** Use direct index checking rather than array manipulations to avoid memory allocation overhead in frequently called heuristic functions for these grid sizes. This can dramatically reduce the computation time.
