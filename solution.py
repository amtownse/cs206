import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import os

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)*2-1

    def Evaluate(self, directOrGui):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        os.system("python3 simulate.py "+directOrGui)
        fitnessFile = open('fitness.txt','r')
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Mutate(self):
        self.weights[r.randint(0,2)][r.randint(0,1)] = r.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box",pos=[-3,3,.5],size=[1,1,1])
        pyrosim.End()

    def Create_Robot(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",pos=[0,0,1.5],size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent=
    "Torso" , child =
    "FrontLeg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg",pos=[0.5,0,-0.5],size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent=
    "Torso" , child =
    "BackLeg" , type = "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg",pos=[-0.5,0,-0.5],size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = 3+currentColumn, weight = 
self.weights[currentRow][currentColumn] )
        pyrosim.End()  

