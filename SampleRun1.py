from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from SampleDriveBase import *

hub = PrimeHub()

def mission1(): # run square  
    print("Doing mission1")
    MoveForward(200)
    TurnLeft(90)
    TurnRight(90)
   
def mission2(): # run straight line and  raise arm
    print("Doing mission2")
    MoveBackward(200)
    TurnRight(90)

def doRun1():
    mission1()
    mission2()

if __name__ == "__main__":
    print("From Run1")
    doRun1()
