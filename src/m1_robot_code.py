"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Deng Zou.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # TODO: Add methods here as needed.
    def forward(self,speed,inches):
        degree = inches * 90
        print_message_received("forward",[speed,inches])
        self.robot.drive_system.go(speed,speed)
        while True:
            if self.robot.drive_system.left_motor.get_position()>=degree \
                    and self.robot.drive_system.right_motor.get_position()>=degree:
                break
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.stop()

    def backward(self,speed,inches):
        degree=inches*90
        print_message_received("backward", [-speed, -inches])
        self.robot.drive_system.go(-speed,-speed)
        while True:
            if abs(self.robot.drive_system.left_motor.get_position())>=degree \
                    and abs(self.robot.drive_system.right_motor.get_position())>=degree:
                break
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.stop()

    def go_until_distance(self,X,speed):
        self.robot.drive_system.go(speed,speed)
        while True:
            list = []
            count_max=0
            count_min=0
            sum=0
            for k in range (5):
                num = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
                list=list+[num]
            for k in range(5):
                if list[count_max]>list[k]:
                    count_max=k
                if list[count_min]<list[k]:
                    count_min=k
            list.remove(list[count_min])
            list.remove(list[count_max-1])
            for k in range(3):
                sum=sum+list[k]
            average=sum/3
            print(average)

            if average <=X:
                break

        self.robot.drive_system.stop()

def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

