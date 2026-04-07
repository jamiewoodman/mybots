import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI +" "+ str(self.myID) + " &")
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI +" "+ str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        print(self.fitness)
        os.system("rm fitness"+str(self.myID)+".txt")
        fitnessFile.close()
        

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[10,10,1] , size=[1, 1, 1])
        pyrosim.End()
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)
    
    def Generate_Body(self):
        pyrosim.Start_URDF("body2.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,2,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[.2,1,.2]) 
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,-.5,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,-.5,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[.2,0.2,1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0.5,-0.5] , size=[.2,0.2,1])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0.5,-0.5] , size=[.2,0.2,1])


        pyrosim.Send_Joint( name = "Torso_Mid1Leg" , parent= "Torso" , child = "Mid1Leg" , type = "revolute", position = [-.5,0,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Mid1Leg", pos=[-.5,.5,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_Mid2Leg" , parent= "Torso" , child = "Mid2Leg" , type = "revolute", position = [.5,0,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Mid2Leg", pos=[.5,.5,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Mid1Leg_Mid1LowerLeg" , parent= "Mid1Leg" , child = "Mid1LowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Mid1LowerLeg", pos=[0,-0.5,-0.5] , size=[.2,0.2,1])
        pyrosim.Send_Joint( name = "Mid2Leg_Mid2LowerLeg" , parent= "Mid2Leg" , child = "Mid2LowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Mid2LowerLeg", pos=[0,-0.5,-0.5] , size=[.2,0.2,1])
        
        pyrosim.End()
        while not os.path.exists("body2.urdf"):
            time.sleep(0.01)
        

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        linkNames  = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg", "FrontLowerLeg", "BackLowerLeg", "LeftLowerLeg", "RightLowerLeg", "Mid1Leg", "Mid2Leg", "Mid1LowerLeg", "Mid2LowerLeg"]
        jointNames = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", "FrontLeg_FrontLowerLeg", "BackLeg_BackLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg", "Torso_Mid1Leg", "Torso_Mid2Leg", "Mid1Leg_Mid1LowerLeg", "Mid2Leg_Mid2LowerLeg"]
        for i in range(c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = linkNames[i])
        for i in range(c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron(name = c.numSensorNeurons + i, jointName = jointNames[i])
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
        while not os.path.exists("brain" + str(self.myID) + ".nndf"):
            time.sleep(0.01)
        

    def Mutate(self):
        randomRow    = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, newID):
        self.myID = newID