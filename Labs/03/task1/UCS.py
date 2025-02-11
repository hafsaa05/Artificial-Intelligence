import heapq

class UCSUtilityBasedAgent:
    def __init__(self, goal):
        self.goal = goal
    
    def formulate_goal(self, percept):
        return percept == self.goal
    
    def act(self, percept, environment):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} found!"
        return environment.ucs_search(percept, self.goal)

class UCSEnvironment:
    def __init__(self, graph):
        self.graph = graph
    
    def get_percept(self, node):
        return node
    
    def ucs_search(self, start, goal):
        frontier = [(0, start)]  # (cost, node)
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                return f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}"
            
            for neighbor, cost in self.graph.get(current_node, {}).items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    heapq.heappush(frontier, (new_cost, neighbor))
        
        return "Goal not found"

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

start_node = 'A'
goal_node = 'I'

ucs_agent = UCSUtilityBasedAgent(goal_node)
ucs_environment = UCSEnvironment(graph)
print("\nRunning UCS Agent:")
run_agent(ucs_agent, ucs_environment, start_node)
