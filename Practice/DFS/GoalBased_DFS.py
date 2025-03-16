'''
A rescue robot is deployed in a grid-based environment to locate and rescue a lost individual.
The terrain consists of different types of obstacles:

O; represents open paths that can be traversed.
X; represents obstacles that cannot be crossed.
P; represents the starting position of the robot.
T; represents the target location where the lost individual is located.
The robot can move in four directions: up, down, left, and right.
implement Depth-First Search (DFS) find a path from P to T
consider this grid
O O X O T
O X O O X
P O O X O
X X O O O
O O O X O
'''

# Rescue Robot using BFS and DFS
class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_start_and_goal(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'P':
                    start = (i, j)
                if self.grid[i][j] == 'T':
                    goal = (i, j)
        return start, goal

    # BFS Search Implementation
    def bfs_search(self, start, goal):
        visited = []
        queue = [(start, [start])]

        # Directions for movement: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            node, path = queue.pop(0)  # FIFO Queue
            x, y = node

            if node == goal:
                return f"Goal {goal} found! Path: {path}"

            if node not in visited:
                visited.append(node)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols:
                        if self.grid[nx][ny] != 'X' and (nx, ny) not in visited:
                            queue.append(((nx, ny), path + [(nx, ny)]))

        return "Goal not found"

    # DFS Search Implementation
    def dfs_search(self, start, goal):
        visited = []
        stack = [(start, [start])]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            node, path = stack.pop()  # LIFO Stack
            x, y = node

            if node == goal:
                return f"Goal {goal} found! Path: {path}"

            if node not in visited:
                visited.append(node)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols:
                        if self.grid[nx][ny] != 'X' and (nx, ny) not in visited:
                            stack.append(((nx, ny), path + [(nx, ny)]))

        return "Goal not found"

# Grid Representation
grid = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'O', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O']
]

# Create environment and get start/goal positions
environment = Environment(grid)
start_node, goal_node = environment.get_start_and_goal()

# Run BFS search
print("\nFollowing is the Breadth-First Search (BFS):")
print(environment.bfs_search(start_node, goal_node))

# Run DFS search
print("\nFollowing is the Depth-First Search (DFS):")
print(environment.dfs_search(start_node, goal_node))
