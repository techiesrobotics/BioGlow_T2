################################################################
#         Techies Robotics team training purposes only         #
#   No sharing with or use by other teams without permission   #
#        Contact techiesrobotics@gmail.com for permission      #
################################################################


from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialize a motor on port E.

left_arm = Motor(Port.E)
 
def raiseArmUp(speed, angle):
    left_arm.run_angle(speed, angle) 

def lowerArmDown(speed, angle): 
    left_arm.run_angle(speed, -1*angle)


def testArm():
    print ("from SampleArm main method")
    raiseArmUp(100, 90)
    lowerArmDown(100, 90)
    
   
if __name__ == "__main__":
    testArm()
