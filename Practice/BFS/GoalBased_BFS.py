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
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_percept(self, node):
        return node

    # BFS Search Implementation
    def bfs_search(self, start, goal):
        visited = []
        queue = [(start, [start])]  # Queue holds (node, path)

        # Directions for movement: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            node, path = queue.pop(0)  # FIFO Queue
            x, y = node

            if node == goal:  # ✅ Correct Goal Check
                return f"Goal found! Path: {path}"

            if node not in visited:
                visited.append(node)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols:
                        if self.grid[nx][ny] != 'X' and (nx, ny) not in visited:
                            queue.append(((nx, ny), path + [(nx, ny)]))

        return "Goal not found"

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

# Grid Layout
grid = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'O', 'O', 'X'],
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
