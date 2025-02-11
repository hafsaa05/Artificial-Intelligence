class GoalBasedAgentDFS:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return percept == self.goal

    def act(self, percept, environment):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} reached!"
        else:
            return environment.dfs_search(percept, self.goal)

class EnvironmentDFS:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dfs_search(self, start, goal):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            if node not in visited:
                visited.add(node)
                stack.extend(reversed(self.graph.get(node, [])))

        return "Goal not found"

def run_agent_dfs(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

graph_dfs = {
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
agent_dfs = GoalBasedAgentDFS(goal_node)
environment_dfs = EnvironmentDFS(graph_dfs)
run_agent_dfs(agent_dfs, environment_dfs, start_node)
