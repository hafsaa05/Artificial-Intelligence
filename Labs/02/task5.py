import random
import time

class HospitalEnvironment:
    def __init__(self, num_rooms=3):
        self.rooms = {}
        self.medicine_storage = ["A", "B", "C", "D"]
        self.robot_position = "storage"

        for i in range(1, num_rooms + 1):
            room_number = 100 + i
            medicine = random.choice(self.medicine_storage)
            schedule = f"{random.randint(8, 10)}:{random.choice(['00', '30'])} AM"
            needs_attention = random.choice([True, False])
            self.rooms[room_number] = {"medicine": medicine, "schedule": schedule, "needs_attention": needs_attention}

    def display_status(self):
        print(f"Robot position: {self.robot_position}")
        for room, info in self.rooms.items():
            print(f"Room {room}: Medicine {info['medicine']}, Schedule {info['schedule']}, Needs Attention: {info['needs_attention']}")

class DeliveryRobot:
    def __init__(self, environment):
        self.environment = environment
        self.picked_medicine = None
        self.delivered = False

    def move_to(self, location):
        print(f"Moving to {location}...")
        self.environment.robot_position = location
        time.sleep(1)

    def pick_medicine(self, medicine):
        if medicine in self.environment.medicine_storage:
            self.picked_medicine = medicine
            self.environment.medicine_storage.remove(medicine)
            print(f"Picked up medicine: {medicine}")
        else:
            print(f"Medicine {medicine} not available in storage.")

    def deliver_medicine(self, room):
        if room in self.environment.rooms:
            room_info = self.environment.rooms[room]
            if self.picked_medicine == room_info["medicine"]:
                print(f"Delivering {self.picked_medicine} to room {room}.")
                self.delivered = True
                room_info["medicine"] = None
            else:
                print(f"Incorrect medicine for room {room}. Need {room_info['medicine']}.")

    def scan_patient_id(self, room):
        if self.delivered:
            print(f"Scanning patient ID in room {room}.")
        else:
            print("Medicine delivery not completed. Cannot scan patient ID.")

    def alert_staff(self, room):
        if self.environment.rooms[room]["needs_attention"]:
            print(f"Alerting staff for assistance in room {room}.")
        else:
            print(f"No immediate attention needed in room {room}.")

    def perform_delivery_task(self, room):
        print(f"Starting delivery to room {room}.")
        room_info = self.environment.rooms[room]
        self.move_to("storage")
        self.pick_medicine(room_info["medicine"])
        self.move_to(room)
        self.deliver_medicine(room)
        self.scan_patient_id(room)
        self.alert_staff(room)
        print("\n--- Delivery Task Completed ---\n")

    def system_scan(self):
        print("\nPerforming system scan...")
        for room, info in self.environment.rooms.items():
            if info["needs_attention"]:
                print(f"Warning: Room {room} needs attention!")
            else:
                print(f"Room {room} is all set.")

environment = HospitalEnvironment()
robot = DeliveryRobot(environment)

robot.display_status()
robot.perform_delivery_task(101)
robot.perform_delivery_task(102)
robot.system_scan()
