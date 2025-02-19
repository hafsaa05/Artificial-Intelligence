import heapq

def estimate_distance(pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

def optimized_route_finder(starting_point, drop_offs):
    path = []
    current_pos = starting_point
    queue = []
    processed = set()

    for location, time_frame in drop_offs:
        distance = estimate_distance(current_pos, location)
        priority = (time_frame, distance)
        heapq.heappush(queue, (priority, location, time_frame))  # Store time constraint

    while queue:
        _, next_stop, time_frame = heapq.heappop(queue)

        if next_stop not in processed:
            processed.add(next_stop)
            path.append(next_stop)
            current_pos = next_stop

            # Refresh queue to update distances dynamically
            updated_queue = []
            while queue:
                _, loc, loc_time_frame = heapq.heappop(queue)
                new_distance = estimate_distance(current_pos, loc)
                new_priority = (loc_time_frame, new_distance)
                heapq.heappush(updated_queue, (new_priority, loc, loc_time_frame))
            queue = updated_queue

    return path

start_location = (2, 2)
drop_locations = [
    ((6, 4), 2),
    ((3, 5), 4),
    ((7, 7), 1),
    ((5, 2), 3)
]

optimized_path = optimized_route_finder(start_location, drop_locations)
print("Optimized Delivery Route:", optimized_path)
