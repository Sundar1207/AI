## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-10-24 - TSP Brute-Force Early Pruning
**Learning:** For brute-force algorithms over permutations (like TSP), constructing full array representations inside the loop and blindly calculating the full path cost creates a massive overhead.
**Action:** Use early pruning (branch and bound) to exit the loop as soon as the current cost exceeds the best known minimum. Avoid constructing full explicit paths (`[start] + list(perm) + [start]`) inside the loop and increment path costs directly over the iterator.
