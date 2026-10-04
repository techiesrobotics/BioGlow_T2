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

MoveForward(260)
MoveBackward(50)
MoveForward(30)
MoveBackward(39)
TurnLeft(190)
MoveForward(150)
