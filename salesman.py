from collections import deque

def best_ksp():
    n = int(input("Enter the number of cities: "))

    distances = []
    print("Enter the distance matrix (each row separated by spaces):")
    for i in range(n):
        row = list(map(int, input(f"Distance from city {i+1}: ").split()))
        distances.append(row)

    start_city = int(input(f"Enter the starting city (1 to {n}): ")) - 1

    queue = deque([(start_city, [start_city], 0)])
    min_cost = float('inf')
    best_path = []

    while queue:
        current_city, path, current_cost = queue.popleft()

        if len(path) == n:
            total_cost = current_cost + distances[current_city][start_city]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start_city]
            continue

        for next_city in range(n):
            if next_city not in path:
                queue.append((next_city, path + [next_city], current_cost + distances[current_city][next_city]))

    best_path = [city + 1 for city in best_path]
    print("Best route:", best_path)
    print("Minimum cost:", min_cost)

best_ksp()
