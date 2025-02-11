def find_shortest_route(current_city, visited, cities, cost_map, current_cost, best_cost, current_path, best_path):
    if len(visited) == len(cities):  
        round_trip_cost = current_cost + cost_map[current_city][cities[0]]
        if round_trip_cost < best_cost[0]:
            best_cost[0] = round_trip_cost
            best_path[:] = current_path[:] + [cities[0]]
        return

    for next_city in cities:
        if next_city not in visited:
            visited.add(next_city)
            current_path.append(next_city)

            find_shortest_route(next_city, visited, cities, cost_map, 
                                current_cost + cost_map[current_city][next_city], 
                                best_cost, current_path, best_path)

            visited.remove(next_city)
            current_path.pop()


def solve_tsp(cities, cost_map):
    best_cost = [float('inf')]  
    best_path = []  

    visited = {cities[0]}  
    find_shortest_route(cities[0], visited, cities, cost_map, 0, best_cost, [cities[0]], best_path)

    return best_path, best_cost[0]


cities = ['A', 'B', 'C', 'D']
travel_costs = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

optimal_route, minimal_cost = solve_tsp(cities, travel_costs)
print(f"Optimal Route: {optimal_route}\nMinimal Travel Cost: {minimal_cost}")
