import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
for i in range(0, 1000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)
p.disconnect()
