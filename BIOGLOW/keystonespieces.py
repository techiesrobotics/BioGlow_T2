from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from setup import* 
SetSpeed(100)
StraightAcceleration(300)
TurnRate(300)
MoveForward(250)
TurnRight(45)
MoveForward(57)
