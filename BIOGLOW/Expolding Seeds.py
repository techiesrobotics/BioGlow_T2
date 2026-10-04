from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from setup import*

SetSpeed(90)
StraightAcceleration(75)
TurnRate(140)

MoveForward(133)
right_small_motor.run_angle(45,-45)
MoveBackward(135)



