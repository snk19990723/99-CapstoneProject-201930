"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Deng Zou.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Deng Zou")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    go_forward_button = ttk.Button(frame, text='RUSH B, RUSH B！')
    go_forward_button.grid()
    go_backward_button= ttk.Button(frame, text='RETREAT！')
    go_backward_button.grid()


    speed=ttk.Entry(frame)
    speed.insert(0,'50')
    speed.grid()

    inches=ttk.Entry(frame)
    inches.insert(0,'360')
    inches.grid()

    go_forward_button["command"]= lambda: forward(speed,inches,mqtt_sender)
    go_backward_button["command"]= lambda: backward(speed,inches,mqtt_sender)

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
def forward(speed,inches,mqtt_sender):
    norm_speed = int(speed.get())
    norm_inches = int(inches.get())
    print('Rush B! Rush B!')
    print('motor message:', speed.get())
    print('target distance:', inches.get())
    mqtt_sender.send_message('forward',[norm_speed,norm_inches])

def backward(speed,inches,mqtt_sender):
    norm_speed=int(speed.get())
    norm_inches=int(inches.get())
    print('Fall back! Fall back!')
    print('motor message:', -norm_speed)
    print('target distance:', -norm_inches)
    mqtt_sender.send_message('backward', [norm_speed, norm_inches])

