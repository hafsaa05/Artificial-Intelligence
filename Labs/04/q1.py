import heapq
import math

class Cell:
    def __init__(self):
        self.parent = None
        self.f = float('inf')  # Total cost (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost to destination

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

def heuristic(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def trace_path(cell_details, goal):
    path = []
    while goal:
        path.append(goal)
        goal = cell_details[goal].parent
    return path[::-1]

def a_star_multi_goal(grid, start, goals):
    open_list = []
    heapq.heappush(open_list, (0, start))
    cell_details = {start: Cell()}
    cell_details[start].g = 0
    cell_details[start].f = 0
    visited_goals = set()
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current in goals:
            visited_goals.add(current)
            if visited_goals == set(goals):
                return trace_path(cell_details, current)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(grid, neighbor[0], neighbor[1]):
                g_new = cell_details[current].g + 1
                if neighbor not in cell_details or g_new < cell_details[neighbor].g:
                    cell_details[neighbor] = Cell()
                    cell_details[neighbor].g = g_new
                    cell_details[neighbor].h = min(heuristic(neighbor, goal) for goal in goals if goal not in visited_goals)
                    cell_details[neighbor].f = cell_details[neighbor].g + cell_details[neighbor].h
                    cell_details[neighbor].parent = current
                    heapq.heappush(open_list, (cell_details[neighbor].f, neighbor))
    
    return None

grid = [
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1]
]

start = (0, 0)
goals = [(1, 3), (3, 1)]

path = a_star_multi_goal(grid, start, goals)
if path:
    print("Path found:", path)
else:
    print("No path found")
