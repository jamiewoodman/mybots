import numpy
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act
        

    def Prepare_To_Act(self):
        self.amplitude = numpy.pi / 6
        self.frequency = 10
        self.offset = 0
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,    
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = BLtargetAngles[i],
            maxForce = 400)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,    
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = FLtargetAngles[i],
            maxForce = 400)
        
