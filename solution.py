import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import time as t
import os
import constants as c

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)*2-1

    def __init__(self, id):
        self.id = id
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1

    def Evaluate(self, directOrGui):
        #self.Create_World()
        #self.Create_Robot()
        self.Create_Brain()
        os.system("python3 simulate.py "+directOrGui+" "+str(self.id)+(" 2&>1 " if not c.debug else 
" ")+"&")

    def getFitness(self):
        while not os.path.exists('fitness'+str(self.id)+'.txt'):
            t.sleep(0.1)
        fitnessFile = open('fitness'+str(self.id)+'.txt','r')   
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system('rm fitness'+str(self.id)+'.txt')

    def Mutate(self):
        self.weights[r.randint(0,2)][r.randint(0,1)] = r.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box",pos=[-3,3,.5],size=[1,1,1])
        pyrosim.End()

    def Create_Robot(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",pos=[0,0,1],size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent=
    "Torso" , child =
    "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg",pos=[0,0.5,0],size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent=
    "FrontLeg" , child =
    "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg",pos=[0,0,-0.5],size=[0.2,0.2,1])


        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent=
    "Torso" , child =
    "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg",pos=[0,-0.5,0],size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent=
    "BackLeg" , child =
    "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg",pos=[0,0,-0.5],size=[0.2,0.2,1])


        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent=
    "Torso" , child =
    "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg",pos=[-0.5,0,0],size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent=
    "LeftLeg" , child =
    "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg",pos=[0,0,-0.5],size=[0.2,0.2,1])


        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent=
    "Torso" , child =
    "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg",pos=[0.5,0,0],size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent=
    "RightLeg" , child =
    "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg",pos=[0,0,-0.5],size=[0.2,0.2,1])


        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.id)+".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg") 
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeg_BackLowerLeg") 
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "LeftLeg_LeftLowerLeg") 
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "RightLeg_RightLowerLeg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = 
c.numSensorNeurons+currentColumn, weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()  

