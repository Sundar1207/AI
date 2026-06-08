## 2024-05-24 - Traveling Salesman Early Pruning
**Learning:** The brute-force Traveling Salesman implementation constructed full arrays `[start] + list(perm) + [start]` for O(N!) combinations before evaluating cost.
**Action:** When calculating optimal combinatorial sequences, incrementally accumulate the path cost over the sequence iterator and use early termination (`break`) immediately when cost exceeds the best known global minimum, avoiding O(N!) object constructions and loop checks.
