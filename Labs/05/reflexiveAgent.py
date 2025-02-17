class Environment:
    def __init__(self, temp):
        self.temp = temp

    def get_percept(self):
        return self.temp


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, temp):
        if temp >= 100:
            bill = temp * 100
        else:
            bill = temp * 15
        
        print(f'Your bill is: {bill} per unit')
        return bill


def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept}, Action: {action}")


temp = 120 
agent = SimpleReflexAgent()
environment = Environment(temp)

run_agent(agent, environment)
