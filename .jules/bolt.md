## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.
## 2024-05-18 - Optimize TSP loops
**Learning:** For algorithmic search implementations (like TSP or brute-force permutations), avoid constructing full array representations inside the main loop to reduce overhead.
**Action:** Incrementally calculate metrics over the iterator, use early pruning to exit loops immediately if the current path cost exceeds the best known minimum, and defer explicit path list construction until a new minimum is actually found.
