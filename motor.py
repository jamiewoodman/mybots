import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        

    """
    def Prepare_To_Act(self):
        self.amplitude = numpy.pi / 6
        self.offset = 0

        if self.jointName == b'Torso_BackLeg':
            self.frequency = 10
        else:
            self.frequency = 5
            
        self.motorValues = numpy.zeros(1000)
        for i in range(1000):
            self.motorValues[i] = self.amplitude * numpy.sin(
                self.frequency * (i / (2 * numpy.pi) * 0.0395) + self.offset
            )
            """
        
    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,    
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 400)
        
"""
    def Save_Values(self):
        numpy.save('data/' + self.jointName + '_motorValues.npy', self.motorValues)
"""