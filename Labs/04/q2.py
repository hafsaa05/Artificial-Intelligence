import heapq
import random
import time

def modify_weights(network, cost_map, queue):
    for point in network:
        for i in range(len(network[point])):
            neighbor, _, estimate = network[point][i]
            new_weight = random.randint(1, 10)
            network[point][i] = (neighbor, new_weight, estimate)
            
            if neighbor in cost_map and cost_map[point] + new_weight < cost_map[neighbor]:
                updated_cost = cost_map[point] + new_weight
                priority = updated_cost + estimate
                heapq.heappush(queue, (priority, neighbor, updated_cost))
                cost_map[neighbor] = updated_cost

def dynamic_astar(network, origin, destination, refresh_rate=3):
    queue = []
    heapq.heappush(queue, (0, origin, 0))
    
    path_trace = {}
    cost_map = {origin: 0}
    explored = set()
    iteration = 0

    while queue:
        if iteration % refresh_rate == 0:
            modify_weights(network, cost_map, queue)

        priority, node, travel_cost = heapq.heappop(queue)

        if node in explored and travel_cost >= cost_map[node]:
            continue

        explored.add(node)
        print(f"Processing: {node}, Travel Cost: {travel_cost}, Priority: {priority}")

        if node == destination:
            print("Target Reached!")
            route = []
            while node in path_trace:
                route.append(node)
                node = path_trace[node]
            route.append(origin)
            return route[::-1]

        for neighbor, weight, estimate in network.get(node, []):
            new_cost = travel_cost + weight

            if neighbor not in cost_map or new_cost < cost_map[neighbor]:
                cost_map[neighbor] = new_cost
                priority = new_cost + estimate
                heapq.heappush(queue, (priority, neighbor, new_cost))
                path_trace[neighbor] = node

        iteration += 1

    print("Target Unreachable!")
    return None

network = {
    'X': [('Y', 4, 8), ('Z', 7, 6)],
    'Y': [('P', 9, 3)],
    'Z': [('Q', 2, 6)],
    'P': [('R', 5, 4)],
    'Q': [('R', 1, 2)],
    'R': []
}

print("\nExecuting Dynamic A* Algorithm:")
route = dynamic_astar(network, 'X', 'R')
if route:
    print("Shortest Route Identified:", route)
else:
    print("No Feasible Route Found")
