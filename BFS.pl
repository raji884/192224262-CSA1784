% Graph edges with heuristic values

edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 1).
edge(c, e, 3).
edge(d, goal, 0).
edge(e, goal, 0).

% Best First Search
bestfs(Node, Goal) :-
    Node = Goal,
    write('Reached Goal: '), write(Goal), nl.

bestfs(Node, Goal) :-
    edge(Node, Next, _),
    write(Node), write(' -> '), write(Next), nl,
    bestfs(Next, Goal).
