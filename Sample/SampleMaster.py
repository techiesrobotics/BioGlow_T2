from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from SampleRun1 import *
from SampleRun2 import *

hub = PrimeHub()
sensor = ColorSensor(Port.B)

last_color = None
while True:
    current_color = sensor.color()
    if current_color != last_color:
        print("Detected:", current_color)

        if current_color == Color.RED:  #do run 1
            print("RED detected from Master, do SampleRun1")
            doRun1()
        elif current_color == Color.BLUE: #do run 2
            print("BLUE detected from Master, do SampleRun2")
            doRun2()
        last_color = current_color
    wait(50)
