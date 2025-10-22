% base case
convert([], 0).

% recursive case(process the first symbol and add/subtract its value)
convert([H|T], N) :-
    value(H, V1),             
    next_value(T, V2),        
    (
        V1 < V2              
        -> N1 is -V1
        ;  N1 is V1          
    ),
    convert(T, N2),           
    N is N1 + N2.            

% next value rule
next_value([], 0).
next_value([H|_], V) :- value(H, V).

% Roman Symbol Values
value(i, 1).
value(v, 5).
value(x, 10).
value(l, 50).
value(c, 100).
value(d, 500).
value(m, 1000).
