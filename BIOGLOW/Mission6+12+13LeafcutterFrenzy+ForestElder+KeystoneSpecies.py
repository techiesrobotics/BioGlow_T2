from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from Setup import*

StraightAcceleration(200)
TurnAcceleration(100)
TurnRate(200)
SetSpeed(80)

MoveForward(100)
small_motor.run_angle(26,26)
MoveBackward(45)
small_motor.run_angle(25,-25)
MoveBackward(10)
TurnRight(15.5174875)
small_motor.run_angle(20,-20)
MoveBackward(15)
wait(0.05)
MoveBackward(20)
small_motor.run_angle(15,23)
MoveBackward(50)
small_motor.run_angle(90,90)
TurnLeft(20)
MoveForward(225)
TurnRight(60)
MoveForward(10)
asmall_motor.run_angle(200,-75)
MoveBackward(20)
asmall_motor.run_angle(200,80)
MoveBackward(50)
TurnLeft(46)
TurnLeft(136)
