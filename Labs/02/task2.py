import random

class DataCenter:
    def __init__(self):
        self.servers = {f"Server {i+1}": random.choice(["Underloaded", "Balanced", "Overloaded"]) for i in range(5)}

    def get_server_loads(self):
        return self.servers.copy()

class LoadBalancer:
    def balance_load(self, server_loads):
        overloaded_servers = [server for server, load in server_loads.items() if load == "Overloaded"]
        underloaded_servers = [server for server, load in server_loads.items() if load == "Underloaded"]
        
        if overloaded_servers and underloaded_servers:
            for overloaded, underloaded in zip(overloaded_servers, underloaded_servers):
                server_loads[overloaded] = "Balanced"
                server_loads[underloaded] = "Balanced"
            return "Load Balanced!"
        return "No balancing needed"

def run_balancer(agent, data_center):
    server_loads = data_center.get_server_loads()
    print("Initial Load State:", server_loads)
    action = agent.balance_load(server_loads)
    print("Action:", action)
    print("Final Load State:", server_loads)

data_center = DataCenter()
load_balancer = LoadBalancer()
run_balancer(load_balancer, data_center) 
