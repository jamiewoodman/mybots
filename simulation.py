from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8,self.physicsClient)

        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()

    def Run(self):
        for t in range(0, 1000):
            
            p.stepSimulation()
            self.robot.Sense(t)
            '''
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
                maxForce = 400)'''
            time.sleep(1/600)
        
            print(t)

    def __del__(self):
        p.disconnect()