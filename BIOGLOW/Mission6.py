from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
from Setup import*
SetSpeed(175)
MoveForward(150)
TurnLeft(85)
MoveForward(100)
TurnRight(60)
MoveForward(30)
SetSpeed(50)
TurnRight(77.5)
MoveForward(50)
wait(100)
MoveBackward(50)
TurnLeft(77.5)
MoveBackward(30)
TurnLeft(60)
MoveBackward(100)
TurnRight(85)
MoveBackward(150)
