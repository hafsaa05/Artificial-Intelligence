class Building:
    def __init__(self):
        self.grid = {
            'a': ' ', 'b': ' ', 'c': '🔥',
            'd': ' ', 'e': '🔥', 'f': ' ',
            'g': ' ', 'h': ' ', 'j': '🔥'
        }
        self.robot_position = 'a'

    def display_status(self):
        print("Current building status:")
        for room in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']:
            status = self.grid[room]
            print(f"Room {room}: {'🔥' if status == '🔥' else ' '}")
        print()

    def move_robot(self, next_room):
        self.robot_position = next_room
        if self.grid[self.robot_position] == '🔥':
            self.extinguish_fire()

    def extinguish_fire(self):
        print(f"Fire detected and extinguished in room {self.robot_position}.")
        self.grid[self.robot_position] = ' '

class FirefightingRobot:
    def __init__(self, building):
        self.building = building

    def follow_path(self, path):
        self.building.display_status()  
        for room in path:
            self.building.move_robot(room)
            self.building.display_status()

building = Building()
robot = FirefightingRobot(building)
path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
robot.follow_path(path)
