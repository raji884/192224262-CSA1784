from itertools import permutations
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(graph)
cities = list(range(n))

min_cost = float('inf')
best_path = []
for path in permutations(cities[1:]):
    current_cost = 0
    k = 0

    for city in path:
        current_cost += graph[k][city]
        k = city

    current_cost += graph[k][0]  
    if current_cost < min_cost:
        min_cost = current_cost
        best_path = [0] + list(path) + [0]

print("Optimal Path:", best_path)
print("Minimum Cost:", min_cost)
