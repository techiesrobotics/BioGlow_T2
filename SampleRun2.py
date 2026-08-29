from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from SampleDriveBase import *
from SampleArm import *

hub = PrimeHub()

def mission3():
    print ("Doing mission3")
    raiseArmUp(10, 90)
    lowerArmDown(10, 90)

def doRun2():
    mission3()

if __name__ == "__main__":
    print("from run2")
    doRun2()
