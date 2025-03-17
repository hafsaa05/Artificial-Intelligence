''' 
A courier robot needs to deliver a package from the top-left corner (0,0) to the bottom-right
corner (N-1, M-1) of an N x M weighted grid. The grid contains different terrain costs
represented by positive integers. Some cells are impassable and marked as &#39;#&#39;.
Implement the A search algorithm to find the optimal path from (0,0) to (N-1,M-1).
1 2 3 # 4
1 # 1 2 2
2 3 1 # 1
# # 2 1 1
1 1 2 2 1
'''

from queue import PriorityQueue

# Grid representation
grid = [
    [1, 2, 3, '#', 4],
    [1, '#', 1, 2, 2],
    [2, 3, 1, '#', 1],
    ['#', '#', 2, 1, 1],
    [1, 1, 2, 2, 1]
]

# Goal coordinates (bottom-right corner)
goal = (4, 4)

# Manhattan distance heuristic
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Graph conversion function
def build_graph(grid):
    graph = {}
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == '#':
                continue  # Skip impassable cells
            
            node = (x, y)
            graph[node] = []

            # Possible moves (Up, Down, Left, Right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                    graph[node].append(((nx, ny), grid[nx][ny]))

    return graph

# Build and print the graph
graph = build_graph(grid)

def astar_search(graph, start, goal):
    visited = set()                     # Track visited nodes
    pq = PriorityQueue()                # Priority queue for f-value sorting
    pq.put((heuristic(start, goal), 0, start))  # Enqueue start node with f-value

    while not pq.empty():
        _, cost, node = pq.get()        # Dequeue node with the lowest f-value

        if node not in visited:
            print(node, end=' ')        # Print current node
            visited.add(node)           # Mark current node as visited
            
            if node == goal:            # Goal node found
                print("\nGoal reached!")
                return True
            
            # Explore neighbors
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    # Calculate f-value for the neighbor
                    f_value = cost + edge_cost + heuristic(neighbor, goal)
                    pq.put((f_value, cost + edge_cost, neighbor))  

    print("\nGoal not reachable!")
    return False

# Example usage
print("A* Search Path:")
astar_search(graph, (0, 0), (4, 4))
