## 2024-06-25 - Tic-Tac-Toe Win Evaluation Overhead
**Learning:** Statically evaluating 3x3 grids recursively using array manipulations and list comprehensions (e.g., dynamically building a list of all lines) incurs significant overhead in highly recursive algorithms like Minimax and Alpha-Beta pruning due to constant memory allocation.
**Action:** Use direct index checking for static 3x3 grid evaluations instead of generalized array manipulations to drastically reduce evaluation time and garbage collection overhead in game tree searches.
