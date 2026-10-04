from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_large_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
right_large_motor = Motor(Port.A)
right_small_motor = Motor(Port.C)
left_small_motor = Motor(Port.D)



 
drive_base = DriveBase(
    left_large_motor,
    right_large_motor,
    wheel_diameter=17.5,
    axle_track=112)

drive_base.use_gyro(True)

def TurnAcceleration(acceleration):
    drive_base.settings(turn_acceleration=acceleration)
def SetGyro(truefalse):
    drive_base.use_gyro(truefalse)

def SetSpeed(speed):
    drive_base.settings(straight_speed=speed)

def TurnRate(rate):
    drive_base.settings(turn_rate=rate)

def StraightAcceleration(acceleration):
    drive_base.settings(straight_acceleration=acceleration)

def MoveForward(distance):
    drive_base.straight(distance)

def MoveBackward(distance):
    drive_base.straight(-1* distance)

def TurnRight(degrees):
    drive_base.turn(degrees)

def TurnLeft(degrees):
    drive_base.turn(-1* degrees)
