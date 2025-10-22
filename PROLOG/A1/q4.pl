:- use_module(library(lists)).

digits([1,2,3,4,5,6,7,8,9]).

kakuro([[_,C1,C2],
     [R1,A,B],
     [R2,C,D]]) :-
digits(Vals),
member(A, Vals), member(B, Vals),
member(C, Vals), member(D, Vals),

A \= C, B \= D,
R1 =:= A + B, R2 =:= C + D,
C1 =:= A + C, C2 =:= B + D,

nl, write('2x2 Kakuro Solution:'), nl,
write([A,B]), write('  Row sum='), write(R1), nl,
write([C,D]), write('  Row sum='), write(R2), nl,
write('Column sums: '), write([C1,C2]), nl.
