from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from Setup import*
StraightAcceleration(100)
TurnAcceleration(100)
TurnRate(100)

MoveForward(100)
small_motor.run_angle(26,26)
MoveBackward(50)
small_motor.run_angle(26,-26)
MoveBackward(20)
TurnRight(10)
small_motor.run_angle(15,-15)
TurnLeft(75)
