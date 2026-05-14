
## 2024-05-14 - Avoiding dynamic list allocations in recursive search trees
**Learning:** In highly recursive structures like minimax search trees (used in `Min Max.py` and `Alpha Beta.py`), seemingly small operations like allocating lists (e.g., `lines.extend(board)` or generator comprehensions inside loops) create massive memory and CPU overhead because they are called millions of times.
**Action:** When optimizing tight loops or recursive evaluation functions, replace dynamic list/array creation with direct index lookups and explicit conditionals (e.g., checking `board[r][0] == board[r][1] == board[r][2] != ' '`). This dramatically reduces search time (e.g., Minimax execution from 7.8s to 1.8s).
