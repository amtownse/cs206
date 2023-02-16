from solution import SOLUTION
import constants as c
import copy

import os
import sys

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableId = 0
        self.parents = {}
        for i in range(c.ps):
            self.parents[i]=SOLUTION(self.nextAvailableId)
            self.nextAvailableId += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate("DIRECT")
        for i in self.parents:
            self.parents[i].getFitness()
        self.showBest()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.showBest()

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
            print('c'+str(i)+':',cfitness,'\t\tp'+str(i)+':',pfitness, end='|')
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
