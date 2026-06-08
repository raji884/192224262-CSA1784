from collections import deque

def solve():
    start = (3, 3, 'Left')
    goal = (0, 0, 'Right')

    queue = deque([(start, [])])
    visited = set()

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        m, c, side = state

        for dm, dc in moves:
            if side == 'Left':
                new = (m-dm, c-dc, 'Right')
            else:
                new = (m+dm, c+dc, 'Left')

            nm, nc, _ = new

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and ((3-nm) == 0 or (3-nm) >= (3-nc)):
                    queue.append((new, path + [state]))

solution = solve()

print("Missionaries and Cannibals Solution:\n")
for step in solution:
    m, c, side = step
    print(f"Missionaries = {m}, Cannibals = {c}, Boat = {side}")
