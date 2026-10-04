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

MoveForward(242)
MoveBackward(40)
MoveForward(30)
SetSpeed(150)
MoveBackward(18)
TurnLeft(90)
MoveBackward(19)
TurnLeft(110)
MoveForward(145)
