## 2024-05-24 - [Winner Evaluation Bottleneck]
**Learning:** Generalized list comprehensions for evaluating 3x3 static grids (like in Tic-Tac-Toe Minimax) generate massive overhead due to array allocations.
**Action:** Use direct index checking for static grid evaluations rather than allocating lists dynamically inside recursive functions.
