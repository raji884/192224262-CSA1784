from queue import PriorityQueue

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(
        abs(i // 3 - (tile - 1) // 3) +
        abs(i % 3 - (tile - 1) % 3)
        for i, tile in enumerate(state)
        if tile != 0
    )

def solve(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), start))
    visited = set()

    while not pq.empty():
        _, state = pq.get()

        if state == goal:
            return state

        visited.add(state)

        zero = state.index(0)
        moves = []

        if zero > 2:
            moves.append(zero - 3)
        if zero < 6:
            moves.append(zero + 3)
        if zero % 3 > 0:
            moves.append(zero - 1)
        if zero % 3 < 2:
            moves.append(zero + 1)

        for move in moves:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                pq.put((heuristic(new_state), new_state))

    return None

initial = (1, 2, 3, 4, 5, 6, 7, 0, 8)

result = solve(initial)

if result:
    print("Puzzle Solved!")
    for i in range(0, 9, 3):
        print(result[i], result[i+1], result[i+2])
else:
    print("No Solution Found")
