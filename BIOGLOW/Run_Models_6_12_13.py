from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from SetUp import*

StraightAcceleration(90)
TurnAcceleration(250)
TurnRate(100)
SetSpeed(100)

MoveForward(152)
small_motor.run_angle(26, -28)
MoveBackward(10)
TurnLeft(2)
TurnRight(2)
MoveBackward(15)
MoveBackward(20)
small_motor.run_angle(150,30)
small_motor.run_angle(150,-30)
small_motor.run_angle(20, 20)
TurnRight(10)
small_motor.run_angle(20, 15)
MoveBackward(50)
TurnLeft(16.1)
MoveForward(145)
small_motor.run_angle(90,-90)
TurnRight(30)
MoveForward(10)
TurnRight(7)
asmall_motor.run_angle(75,-75)
asmall_motor.run_angle(75,75)
MoveForward(20)
asmall_motor.run_angle(100,-80)
MoveBackward(25)
TurnLeft(128)
MoveForward(109)
TurnRight(125)
SetSpeed(30)
MoveForward(45)
MoveBackward(6)
SetSpeed(125)
TurnLeft(135)
MoveForward(159.6)
TurnLeft(30)
MoveForward(159.6)
TurnLeft(30)
MoveForward(106.4)
