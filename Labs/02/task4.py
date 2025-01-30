import random

class SecuritySystem:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(["Safe", "Low Risk", "High Risk"]) for i in range(9)}

    def get_status(self):
        return self.components.copy()

class SecurityAgent:
    def scan_and_patch(self, system_status):
        print("\nSystem Scan Results:")
        for component, status in system_status.items():
            if status == "Safe":
                print(f"{component} is Safe.")
            elif status == "Low Risk":
                print(f"{component} has a Low Risk vulnerability. Patching...")
                system_status[component] = "Safe"
            elif status == "High Risk":
                print(f"{component} has a High Risk vulnerability. Premium service required for patching.")

        return "Low Risk vulnerabilities patched."

def run_security_check():
    system = SecuritySystem()
    agent = SecurityAgent()

    initial_status = system.get_status()
    print("Initial System Check:", initial_status)

    action = agent.scan_and_patch(initial_status)
    print("\nAction:", action)

    print("\nFinal System Check:", initial_status)

run_security_check()
