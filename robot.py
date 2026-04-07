from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.nn = NEURAL_NETWORK("brain"+solutionID+".nndf")
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body2.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("rm brain"+solutionID+".nndf")

    def Prepare_To_Sense(self):
        # self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        if t == 0:
            return
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        # self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        # print(self.motors.keys()) 
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                jointName = jointName.encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        # f = open("fitness"+solutionID+".txt", "w")
        f = open("tmp"+solutionID+".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("mv tmp"+solutionID+".txt fitness"+solutionID+".txt")