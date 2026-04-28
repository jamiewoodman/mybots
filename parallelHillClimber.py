from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        """
        self.parent = SOLUTION()
        """
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self, showBest=True):
        
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        if showBest:
            self.Show_Best()
        
        

    def Evolve_For_One_Generation(self):
        
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()

        self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in range(c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            print(self.parents[key].fitness, self.children[key].fitness)
        print()

    def Show_Best(self):
        bestFitness = float('inf')
        bestID = 0
        for key in self.parents:
            if self.parents[key].fitness < bestFitness:
                bestFitness = self.parents[key].fitness
                bestID = key
        self.parents[bestID].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
    
