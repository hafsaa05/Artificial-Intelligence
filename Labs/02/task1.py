import random

class Environment:
    def __init__(self):
        self.components = {chr(i): random.choice(['Safe', 'Vulnerable']) for i in range(65, 74)} 
    
    def get_percept(self):
        return self.components

    def patch_component(self, component):
        if self.components[component] == 'Vulnerable':
            self.components[component] = 'Safe'

class SecurityAgent:
    def __init__(self):
        self.warnings = []
        self.success_logs = []
    
    def scan_system(self, environment):
        """Scans the environment for vulnerabilities."""
        for component, status in environment.get_percept().items():
            if status == 'Vulnerable':
                self.warnings.append(f"Warning: Component {component} is Vulnerable!")
            else:
                self.success_logs.append(f"Success: Component {component} is Safe.")
    
    def patch_vulnerabilities(self, environment):
        """Patches all vulnerable components."""
        patched_components = []
        for component in environment.components.keys():
            if environment.components[component] == 'Vulnerable':
                environment.patch_component(component)
                patched_components.append(component)
        return patched_components

def run_simulation():
    environment = Environment()
    agent = SecurityAgent()
    
    print("Initial System State:")
    for component, status in environment.get_percept().items():
        print(f"Component {component}: {status}")
    
    agent.scan_system(environment)
    print("\nSystem Scan Results:")
    for warning in agent.warnings:
        print(warning)
    for success in agent.success_logs:
        print(success)
    
    patched_components = agent.patch_vulnerabilities(environment)
    print("\nPatching Vulnerabilities:")
    for component in patched_components:
        print(f"Component {component} has been patched to Safe.")
    
    print("\nFinal System State:")
    for component, status in environment.get_percept().items():
        print(f"Component {component}: {status}")

run_simulation()
