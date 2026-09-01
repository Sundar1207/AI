## 2024-05-18 - Avoid Generalized List Comprehensions in Tic-Tac-Toe Minimax Heuristics
**Learning:** For static grid evaluations (like 3x3 Tic-Tac-Toe) in highly recursive algorithms, generating lines dynamically using list comprehensions (`[[board[r][c] for r in range(3)] for c in range(3)]`) in leaf-node heuristics results in massive object allocation overhead and slows down search trees. Profiling showed `winner` taking >50% of runtime due to list allocations in `Min Max.py`.
**Action:** Replace dynamic line generation and generalized `all()` checks with hardcoded array index comparisons. A simple O(1) manual comparison per line (`board[0][0] == board[1][1] == board[2][2]`) provides a ~3.7x speedup for the full Minimax pass.

## 2024-05-18 - Ensure Code Optimization Guidelines Include Documentation
**Learning:** During the performance optimization pass for the Alpha-Beta algorithm, while the functional O(1) optimization was correctly applied (improving speed by removing list creations in the inner loop), a key agent boundary to "Always do: Add comments explaining the optimization" was missed in the initial submission.
**Action:** When implementing code changes as the Bolt agent, always ensure the final patched code includes explicit, inline code comments detailing the rationale for the optimization before requesting a review.
