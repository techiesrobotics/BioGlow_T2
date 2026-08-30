################################################################
#         Techies Robotics team training purposes only         #
#   No sharing with or use by other teams without permission   #
#        Contact techiesrobotics@gmail.com for permission      #
################################################################

#these are importsfor functions=============
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#=========start==================================

hub = PrimeHub() #define hub
#hub.light.on(Color.RED)

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE) #set the motor and ports
right_motor = Motor(Port.D)
##color_sensor = ColorSensor(Port.E)
#color_sensor_side = ColorSensor(Port.B)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110) #drivebase = motors + wheel dimensions + distance between wheels
drive_base.use_gyro(True) #use gyro when driving

def SetGyro(truefalse):
    drive_base.use_gyro(truefalse)

def SetSpeed(speed): #set the speed
    drive_base.settings(straight_speed=speed)

def MoveForward(distance): #move
    drive_base.straight(distance)

def MoveBackward(distance):
    drive_base.straight(-1* distance)

def TurnRight(degrees):
    drive_base.turn(degrees)

def TurnLeft(degrees):
    drive_base.turn(-1* degrees)


def testDriveBase():
    
    MoveForward(200)
    MoveBackward(200)
    '''
    lowerArmDown(100, 90)
    raiseArmUp(100, 90)
    '''
    
    
if __name__ == "__main__":
    testDriveBase()
