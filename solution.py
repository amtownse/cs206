import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import time as t
import os
import constants as c

class SOLUTION:
    def __init__(self, id):
        self.id = id
        self.sensorweights = np.random.rand(c.numSensorNeurons,c.numInnerNeurons)*2-1
        self.innerweights = np.random.rand(c.numInnerNeurons,c.numInnerNeurons)*2-1
        self.motorweights = np.random.rand(c.numInnerNeurons,c.numMotorNeurons)*2-1
        self.sensorparams = np.random.rand(c.numSensorNeurons,4)*2-1
        self.innerparams = np.random.rand(c.numInnerNeurons,4)*2-1
        self.motorparams = np.random.rand(c.numMotorNeurons,4)*2-1

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
        if r.random()>0.5:
            self.sensorweights[r.randint(0,c.numSensorNeurons-1)][r.randint(0,c.numInnerNeurons-1)] = r.random()*2-1
        if r.random()>0.5:
            self.innerweights[r.randint(0,c.numInnerNeurons-1)][r.randint(0,c.numInnerNeurons-1)] = r.random()*2-1
        if r.random()>0.5:
            self.motorweights[r.randint(0,c.numInnerNeurons-1)][r.randint(0,c.numMotorNeurons-1)] = r.random()*2-1
        if r.random()>0.5:
            self.sensorparams[r.randint(0,c.numSensorNeurons-1)][r.randint(0,3)] = r.random()*2-1
        if r.random()>0.5:
            self.innerparams[r.randint(0,c.numInnerNeurons-1)][r.randint(0,3)] = r.random()*2-1
        if r.random()>0.5:
            self.motorparams[r.randint(0,c.numMotorNeurons-1)][r.randint(0,3)] = r.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box",pos=[-3,3,.5],size=[1,1,1])
        pyrosim.End()

    def Create_Robot(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",pos=[0,0,5],size=[2,1,4])


        pyrosim.Send_Joint( name = "Torso_LeftUpperLeg" , parent=
    "Torso" , child =
    "LeftUpperLeg" , type = "revolute", position = [0.75,0,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftUpperLeg",pos=[0,0,-1],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "LeftUpperLeg_LeftLowerLeg" , parent=
    "LeftUpperLeg" , child =
    "LeftLowerLeg" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg",pos=[0,0,1],size=[1,1,2])

        pyrosim.Send_Joint( name = "LeftLowerLeg_LeftFoot" , parent=
    "LeftLowerLeg" , child =
    "LeftFoot" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg",pos=[0,0.25,-0.25],size=[1,1.5,0.5])
        

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
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "RightLowerLeg", T=self.sensorparams[0][0], Y=self.sensorparams[0][1], 
G=self.sensorparams[0][2], Z=self.sensorparams[0][3])
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg", T=self.sensorparams[1][0], Y=self.sensorparams[1][1], 
G=self.sensorparams[1][2], Z=self.sensorparams[1][3])
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg", T=self.sensorparams[2][0], Y=self.sensorparams[2][1], 
G=self.sensorparams[2][2], Z=self.sensorparams[2][3])
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLowerLeg", T=self.sensorparams[3][0], Y=self.sensorparams[3][1], 
G=self.sensorparams[3][2], Z=self.sensorparams[3][3])
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg", T=self.motorparams[0][0], Y=self.motorparams[0][1], 
G=self.motorparams[0][2], Z=self.motorparams[0][3])
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg", T=self.motorparams[1][0], Y=self.motorparams[1][1],
G=self.motorparams[1][2], Z=self.motorparams[1][3])
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg", T=self.motorparams[2][0], Y=self.motorparams[2][1],
G=self.motorparams[2][2], Z=self.motorparams[2][3]) 
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg", T=self.motorparams[3][0], Y=self.motorparams[3][1],
G=self.motorparams[3][2], Z=self.motorparams[3][3])
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeg_BackLowerLeg", T=self.motorparams[4][0], Y=self.motorparams[4][1],
G=self.motorparams[4][2], Z=self.motorparams[4][3]) 
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "FrontLeg_FrontLowerLeg", T=self.motorparams[5][0], Y=self.motorparams[5][1],
G=self.motorparams[5][2], Z=self.motorparams[5][3])
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "LeftLeg_LeftLowerLeg", T=self.motorparams[6][0], Y=self.motorparams[6][1],
G=self.motorparams[6][2], Z=self.motorparams[6][3]) 
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "RightLeg_RightLowerLeg", T=self.motorparams[7][0], Y=self.motorparams[7][1],
G=self.motorparams[7][2], Z=self.motorparams[7][3])
        for i in range(c.numInnerNeurons):
            pyrosim.Send_Hidden_Neuron( name = 12+i, linkName = "null", T=self.innerparams[i][0], Y=self.innerparams[i][1], 
G=self.innerparams[i][2], Z=self.innerparams[i][3])
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numInnerNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = 
c.numSensorNeurons+currentColumn, weight = self.sensorweights[currentRow][currentColumn] )
        for currentRow in range(c.numInnerNeurons):
            for currentColumn in range(c.numInnerNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = c.numSensorNeurons+currentRow, targetNeuronName =
c.numSensorNeurons+currentColumn, weight = self.innerweights[currentRow][currentColumn] )
        for currentRow in range(c.numInnerNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = c.numSensorNeurons+currentRow, targetNeuronName =
c.numSensorNeurons+c.numInnerNeurons+currentColumn, weight = self.motorweights[currentRow][currentColumn] )
        pyrosim.End()  

