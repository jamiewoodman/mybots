import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

BLamplitude = numpy.pi / 6
BLfrequency = 10
BLphaseOffset = 0

FLamplitude = numpy.pi / 6
FLfrequency = 10
FLphaseOffset = numpy.pi / 2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body2.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)
BLtargetAngles = numpy.zeros(1000)
FLtargetAngles = numpy.zeros(1000)
for i in range(0, 1000):
    BLtargetAngles[i] = BLamplitude * numpy.sin(BLfrequency * ((i / (2 * numpy.pi) * .0395)) + BLphaseOffset)
    FLtargetAngles[i] = FLamplitude * numpy.sin(FLfrequency * ((i / (2 * numpy.pi) * .0395)) + FLphaseOffset)
# targetAngles = numpy.sin(input * numpy.pi / 180. ) * numpy.pi / 4
# numpy.save('data/targetAngles2.npy', targetAngles)
numpy.save('data/targetAnglesBL.npy', BLtargetAngles)
numpy.save('data/targetAnglesFL.npy', FLtargetAngles)
for i in range(0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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
    time.sleep(1/600)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)