## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Early Branch Pruning and Loop Optimization in Permutation Search
**Learning:** For brute-force search implementations (like TSP permutations), creating full array representations inside the main loop adds significant memory allocation overhead. Also, without early pruning, the algorithm visits many unnecessary sub-optimal paths.
**Action:** Incrementally calculate the cost over the generator, use early branching (`break`) if the running cost exceeds the current minimum, and handle empty iterators before the loop to avoid IndexErrors.
