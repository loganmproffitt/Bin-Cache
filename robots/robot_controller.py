import uuid
from warehouse.grid import Grid
from robots.robot import Robot

class RobotController:
    def __init__(self):
        self.robots = {} # {robot_id: robot_obj}
        self.grid = Grid() # Get grid singleton

    def add_robot(self, x, y):
        robot_id = str(uuid.uuid4())
        robot = Robot(robot_id, x, y, self.grid)
        self.robots[robot_id] = robot
        return robot_id

    def get_robot(self, robot_id):
        return self.robots(robot_id, None)
    
    def list_robots(self):
        """Prints all active robots."""
        for robot_id, robot in self.robots.items():
            print(f"Robot {robot_id}: Position ({robot.x}, {robot.y})")