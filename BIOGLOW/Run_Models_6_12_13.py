from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from Setup import*

StraightAcceleration(240)
TurnAcceleration(250)
TurnRate(300)
SetSpeed(125)

MoveForward(100)
small_motor.run_angle(26,-26)
MoveBackward(45)
small_motor.run_angle(25,25)
MoveBackward(10)
TurnRight(15)
small_motor.run_angle(20,20)
MoveBackward(15)
MoveBackward(20)
small_motor.run_angle(90,-23)
MoveBackward(50)
small_motor.run_angle(90,-90)
TurnLeft(20)
MoveForward(212)
TurnRight(60)
MoveForward(20)
TurnLeft(6)
asmall_motor.run_angle(200,-64)
MoveBackward(20)
asmall_motor.run_angle(200,80)
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
