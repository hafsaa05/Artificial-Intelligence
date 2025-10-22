% set member
set_member(X, [X|_]).
set_member(X, [_|T]) :-
    set_member(X, T).

% set union
set_union(S1, S2, S) :-
    sort(S1, A),
    sort(S2, B),
    union_sorted(A, B, S).

% set intersection
set_intersection(S1, S2, S) :-
    sort(S1, A),
    sort(S2, B),
    intersection_sorted(A, B, S).

% set cardinality
set_cardinality(S, N) :-
    sort(S, Sorted),          
    set_cardinality_count(Sorted, N).

% set difference
set_difference(S1, S2, S) :-
    sort(S1, A),
    sort(S2, B),
    difference_sorted(A, B, S).

% helper rules (for above sets) 
% union
union_sorted([], S, S).
union_sorted(S, [], S) :- S \= [].
union_sorted([X|TX], [X|TY], [X|TZ]) :-
    union_sorted(TX, TY, TZ).
union_sorted([X|TX], [Y|TY], [X|TZ]) :-
    X @< Y,
    union_sorted(TX, [Y|TY], TZ).
union_sorted([X|TX], [Y|TY], [Y|TZ]) :-
    X @> Y,
    union_sorted([X|TX], TY, TZ).

% intersection
intersection_sorted([], _, []).
intersection_sorted(_, [], []).
intersection_sorted([X|TX], [X|TY], [X|TZ]) :-
    intersection_sorted(TX, TY, TZ).
intersection_sorted([X|TX], [Y|TY], TZ) :-
    X @< Y,
    intersection_sorted(TX, [Y|TY], TZ).
intersection_sorted([X|TX], [Y|TY], TZ) :-
    X @> Y,
    intersection_sorted([X|TX], TY, TZ).

% cardinality 
set_cardinality_count([], 0).
set_cardinality_count([_|Tail], N) :-
    set_cardinality_count(Tail, N1),
    N is N1 + 1.

% difference
difference_sorted([], _, []).
difference_sorted(S, [], S) :- S \= [].
difference_sorted([X|TX], [X|TY], TZ) :-
    difference_sorted(TX, TY, TZ).
difference_sorted([X|TX], [Y|TY], [X|TZ]) :-
    X @< Y,
    difference_sorted(TX, [Y|TY], TZ).
difference_sorted([X|TX], [Y|TY], TZ) :-
    X @> Y,
    difference_sorted([X|TX], TY, TZ).

% operators
:- op(500, xfy, '∪').
:- op(500, xfy, '∩').

A ∪ B :- set_union(A, B, R), write(R).
A ∩ B :- set_intersection(A, B, R), write(R).


% power set  
set_power([], [[]]).
set_power([H|T], P) :-
    set_power(T, PT),
    add_all(H, PT, PH),
    append(PT, PH, P).

add_all(_, [], []).
add_all(H, [S|TS], [[H|S]|RS]) :-
    add_all(H, TS, RS).
