import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1)) + distance(route[-1], route[0])

def hill_climbing(points, max_iterations=1000):
    current_route = points[:]
    random.shuffle(current_route)
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        new_route = current_route[:]
        i, j = random.sample(range(len(points)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap two points

        new_distance = total_distance(new_route)
        if new_distance < current_distance:  # Accept only if distance improves
            current_route = new_route
            current_distance = new_distance

    return current_route, current_distance

delivery_points = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 2)]
optimized_route, min_distance = hill_climbing(delivery_points)
print(f"Optimized Route: {optimized_route}")
print(f"Total Distance: {min_distance:.2f}")
