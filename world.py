import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):
        pyrosim.Start_SDF("world.sdf")
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = p.loadURDF("plane.urdf")
