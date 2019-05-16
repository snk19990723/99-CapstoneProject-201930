"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Haozhe Wu.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Haozhe_Wu")
    frame_label.grid()
    # TODO 2: Put your name in the above.
    spin_left_button=ttk.Button(frame,text="spin_left")
    spin_left_button.grid()
    spin_right_button=ttk.Button(frame,text='spin right')
    spin_right_button.grid()
    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    speed_entry=ttk.Entry(frame,width=8)
    speed_entry.insert(0,"100")
    speed_entry.grid()
    distance_entry=ttk.Entry(frame,width=8)
    distance_entry.insert(0,'')
    distance_entry.grid()
    spin_left_button["command"]=lambda:spin_left(speed_entry,distance_entry,mqtt_sender)
    spin_right_button["command"]=lambda:spin_right(speed_entry,distance_entry,mqtt_sender)
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def spin_left(speed_entry,distance_entry,mqtt_sender):
        speed=int(speed_entry.get())
        distance=int(distance_entry.get())
        left_motor_distance=distance
        right_motor_distance=distance
        left_motor_speed = -speed
        right_motor_speed=speed
        mqtt_sender.send_message('spin_left',[left_motor_speed,right_motor_speed,left_motor_distance,right_motor_distance])
        print('left motor speed is', left_motor_speed)
        print('right motor speed is', right_motor_speed)
        print('distance traveled is', distance)
def spin_right(speed_entry,distance_entry,mqtt_sender):
        speed=int(speed_entry.get())
        distance = int(distance_entry.get())
        left_motor_distance = distance
        right_motor_distance = distance
        left_motor_speed=speed
        right_motor_speed=-speed
        mqtt_sender.send_message('spin_right',[left_motor_speed,right_motor_speed,left_motor_distance,right_motor_distance])
        print('left motor speed is',left_motor_speed)
        print('right motor speed is', right_motor_speed)
        print('distance traveled is', distance)