class GoalBasedAgentDLS:
    def __init__(self, goal, depth_limit):
        self.goal = goal
        self.depth_limit = depth_limit

    def formulate_goal(self, percept):
        return percept == self.goal

    def act(self, percept, environment):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} reached!"
        else:
            return environment.dls_search(percept, self.goal, self.depth_limit)

class EnvironmentDLS:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dls_search(self, start, goal, depth_limit):
        def dfs(node, depth, visited):
            if depth > depth_limit:
                return None  
            visited.append(node)
            print(f"Visiting: {node}, Depth: {depth}")

            if node == goal:
                print(f"Goal found with DLS. Path: {visited}")
                return visited

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    path = dfs(neighbor, depth + 1, visited)
                    if path:
                        return path

            visited.pop()  
            return None

        visited = []
        result = dfs(start, 0, visited)
        return "Goal not found" if result is None else result

def run_agent_dls(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

graph_dls = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'
depth_limit = 3
agent_dls = GoalBasedAgentDLS(goal_node, depth_limit)
environment_dls = EnvironmentDLS(graph_dls)
run_agent_dls(agent_dls, environment_dls, start_node)
