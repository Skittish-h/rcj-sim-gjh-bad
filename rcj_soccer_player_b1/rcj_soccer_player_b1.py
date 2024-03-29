# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils


class MyRobot(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()

                # Get the position of our robot
                
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']
                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # Compute the speed for motors
                direction = utils.get_direction(ball_angle)

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = -10
                    right_speed = -10
                else:
                    left_speed = direction * 10 + -10
                    right_speed = direction * -10 + -10

                # Set the speed to motors
                self.left_motor.setVelocity(-10)
                self.right_motor.setVelocity(10)


my_robot = MyRobot()
my_robot.run()
