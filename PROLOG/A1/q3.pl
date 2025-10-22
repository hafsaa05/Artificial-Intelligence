:- use_module(library(lists)).

get_nth(0, [H|_], H).       % n = 0 means first element
get_nth(N, [_|T], X) :-     
    N > 0,
    N1 is N - 1,
    get_nth(N1, T, X).

replace_nth(0, Val, [_|T], [Val|T]).              % replace n-th element in a list with Val
replace_nth(N, Val, [H|T], [H|R]) :-
    N > 0,
    N1 is N - 1,
    replace_nth(N1, Val, T, R).

cell_value(Grid, Row, Col, Val) :-
    ( Row < 0 -> Val = 0
    ; Col < 0 -> Val = 0
    ; get_nth(Row, Grid, R) -> get_nth(Col, R, Val)
    ; Val = 0 ).

mark_cell(Grid, Row, Col, NewGrid) :-            % mark a cell as visited by setting it to 0
    get_nth(Row, Grid, R),
    replace_nth(Col, 0, R, NewR),
    replace_nth(Row, NewR, Grid, NewGrid).

explore(Grid, Row, Col, NewGrid) :-               % explore all connected land cells while visiting up, down, left, right recursively
    cell_value(Grid, Row, Col, 1),
    mark_cell(Grid, Row, Col, Temp),
    explore_dir(Temp, Row-1, Col, G1),
    explore_dir(G1, Row+1, Col, G2),
    explore_dir(G2, Row, Col-1, G3),
    explore_dir(G3, Row, Col+1, NewGrid).
explore(_, _, _, Grid) :- true.                  % if not land, do nothing

explore_dir(Grid, Row, Col, NewGrid) :-          % only explores if the cell is land
    cell_value(Grid, Row, Col, 1) -> explore(Grid, Row, Col, NewGrid)
    ; NewGrid = Grid.

count_islands(Grid, Count) :-                     % When a land cell 1 is found, explore all connected land
    traverse_grid(Grid, 0, 0, 0, Count).

traverse_grid(Grid, Row, Col, Acc, Count) :-
    length(Grid, NumRows),
    ( Row >= NumRows -> Count = Acc
    ; get_nth(Row, Grid, R), length(R, NumCols),
      ( Col >= NumCols ->
            NextRow is Row + 1,
            traverse_grid(Grid, NextRow, 0, Acc, Count)
      ; cell_value(Grid, Row, Col, Val),
        ( Val = 1 ->
            explore(Grid, Row, Col, NewGrid),
            Acc1 is Acc + 1
        ; NewGrid = Grid, Acc1 = Acc ),
        NextCol is Col + 1,
        traverse_grid(NewGrid, Row, NextCol, Acc1, Count)
      )
    ).
