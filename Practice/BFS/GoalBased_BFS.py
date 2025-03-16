'''
A rescue robot is deployed in a grid-based environment to locate and rescue a lost individual.
The terrain consists of different types of obstacles:

O; represents open paths that can be traversed.
X; represents obstacles that cannot be crossed.
P; represents the starting position of the robot.
T; represents the target location where the lost individual is located.
The robot can move in four directions: up, down, left, and right.
implement Breadth-First Search (BFS) find a path from P to T
consider this grid
O O X O T
O X O O X
P O O X O
X X O O O
O O O X O
'''
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return environment.bfs_search(percept, self.goal)

class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.graph = self.create_graph()

    def create_graph(self):
        rows, cols = len(self.grid), len(self.grid[0])
        graph = {}
        
        # Directions for movement: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] != 'X':  # Only consider traversable cells
                    neighbors = []
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and self.grid[nx][ny] != 'X':
                            neighbors.append((nx, ny))
                    graph[(i, j)] = neighbors

        return graph

    def get_percept(self, node):
        return node

    def bfs_search(self, start, goal):
        visited = []  # Track visited nodes
        queue = []    # Queue for BFS
        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)  # Dequeue the first element (FIFO)
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        
        return "Goal not found"

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

# Grid Layout
grid = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'X', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O'],
]

# Identify Start and Goal Nodes
start_node = (2, 0)  # Position of 'P'
goal_node = (0, 4)   # Position of 'T'

# Create instances
agent = GoalBasedAgent(goal_node)
environment = Environment(grid)

# Run the agent
run_agent(agent, environment, start_node)
