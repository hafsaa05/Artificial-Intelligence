import random

class Environment:
    def __init__(self):
    # Initialize the system with 9 components labeled 'A' to 'I',
    # each randomly set as vulnerable (True) or safe (False)
        self.state = {chr(65 + i): random.choice([True, False]) for i in range(9)}

    def get_state(self):
        return self.state.copy()

class Agent:
    def act(self, state):
        vulnerable = [c for c, v in state.items() if v]
        return f"Patch: {', '.join(vulnerable)}" if vulnerable else "No issues"

def run_agent(agent, env):
    state = env.get_state()
    action = agent.act(state)
    print(f"State: {state}\nAction: {action}")

env = Environment()
agent = Agent()
run_agent(agent, env)
