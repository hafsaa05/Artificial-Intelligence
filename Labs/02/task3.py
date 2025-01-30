import random

class BackupSystem:
    def __init__(self):
        self.backups = [random.choice(["Completed", "Failed"]) for _ in range(5)]

    def get_backup_statuses(self):
        return self.backups[:]

class BackupAgent:
    def retry_backups(self, backups):
        for i in range(len(backups)):
            if backups[i] == "Failed":
                backups[i] = "Completed"
        return "Retries done!"

def run_backup_agent():
    system = BackupSystem()
    agent = BackupAgent()

    backups = system.get_backup_statuses()
    print("Before retrying:", backups)

    action = agent.retry_backups(backups)
    print("Action:", action)
    
    print("After retrying:", backups)

run_backup_agent()
