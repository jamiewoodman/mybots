import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body2.urdf")
p.loadSDF("world.sdf")
for i in range(0, 2000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)
p.disconnect()
