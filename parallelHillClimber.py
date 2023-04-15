from solution import SOLUTION
import constants as c
import copy

import os
import sys

class PARALLEL_HILL_CLIMBER:
    def __init__(self, loadOrRun):
        os.system("rm fitness*")
        self.nextAvailableId = 0
        self.parents = {}
        self.loadOrRun = loadOrRun
        if loadOrRun == "R":
            for i in range(c.ps):
                self.parents[i]=SOLUTION(self.nextAvailableId, "")
                self.nextAvailableId += 1
            self.startGen = 0
        else:#L
            loadFile = open('save.txt','r')
            loadWrk = loadFile.read()
            loadFile.close()
            loadWrk = loadWrk.split("!")
            self.startGen = int(loadWrk[0])
            loadWrk=loadWrk[1].split("^")
            for i in range(len(loadWrk)):
                self.parents[i]=SOLUTION(self.nextAvailableId, loadWrk[i])
                self.nextAvailableId += 1 
        self.BuildRobotAndWorld()

    def BuildRobotAndWorld(self):
        self.parents[list(self.parents.keys())[0]].Create_World()
        self.parents[list(self.parents.keys())[0]].Create_Robot()

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate("DIRECT")
        for i in self.parents:
            self.parents[i].getFitness()
        if self.loadOrRun == "R":
            self.showBest()
        for currentGeneration in range(self.startGen, c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.save(currentGeneration)
        temp = input("show best?:")
        self.showBest()

    def save(self, curGen):
        outstr=str(curGen)+"!"
        for parent in self.parents:
            outstr+=str(self.parents[parent].fitness)+"@"
            weights=[self.parents[parent].sensorweights,self.parents[parent].innerweights,self.parents[parent].motorweights,self.parents[parent].sensorparams,self.parents[parent].innerparams,self.parents[parent].motorparams]
            for weight in weights:
                for row in weight:
                    for col in row:
                        outstr+=str(col)+"#"
                    outstr=outstr[:-1]+"$"
                outstr=outstr[:-1]+"%"
            outstr=outstr[:-1]+"^"
        outstr=outstr[:-1]
        saveFile = open('save.txt','w')
        saveFile.write(outstr)
        saveFile.close()

    def Evolve_For_One_Generation(self):
        # silence command-line output temporarily
        sys.stdout, sys.stderr = os.devnull, os.devnull
        self.Spawn()
        self.Mutate()
        for child in self.children:
            self.children[child].Evaluate("DIRECT")
        for child in self.children:  
            self.children[child].getFitness()
        # unsilence command-line output
        sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
        self.Select()
        

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            child = copy.deepcopy(self.parents[parent])
            self.children[parent] = child
            self.children[parent].id = self.nextAvailableId
            self.nextAvailableId += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for i in self.parents:
            cfitness = self.children[i].fitness
            pfitness = self.parents[i].fitness
            print('c'+str(i)+' :',format(cfitness,'.2f'),' | p'+str(i)+' :',format(pfitness,'.2f'), 
end='\t')
            if cfitness>pfitness:
                self.parents[i] = self.children[i]
        print()

    def showBest(self):
        best = list(self.parents.keys())[0]
        for parent in self.parents:
            if self.parents[parent].fitness>self.parents[best].fitness:
                best = parent
        self.parents[best].Evaluate("GUI")
        self.parents[best].getFitness()
