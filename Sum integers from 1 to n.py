sum_to_n(1, 1).
sum_to_n(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum_to_n(Prev, PrevSum),
    Sum is PrevSum + N.
