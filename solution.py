import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import time as t
import os
import constants as c

class SOLUTION:

    def __init__(self, id, loadStr):
        self.id = id
        if loadStr!="":
            self.fitness = float(loadStr.split("@")[0])
            loadWrk = loadStr.split("@")[1].split("%")
            self.sensorweights = []
            for row in loadWrk[0].split("$"):
                self.sensorweights.append([])
                for col in row.split("#"):
                    self.sensorweights[-1].append(float(col))
            self.innerweights = []
            for row in loadWrk[1].split("$"):
                self.innerweights.append([])
                for col in row.split("#"):
                    self.innerweights[-1].append(float(col))
            self.motorweights = []
            for row in loadWrk[2].split("$"):
                self.motorweights.append([])
                for col in row.split("#"):
                    self.motorweights[-1].append(float(col))
            self.sensorparams = []
            for row in loadWrk[3].split("$"):
                self.sensorparams.append([])
                for col in row.split("#"):
                    self.sensorparams[-1].append(float(col))
            self.innerparams = []
            for row in loadWrk[4].split("$"):
                self.innerparams.append([])
                for col in row.split("#"):
                    self.innerparams[-1].append(float(col))
            self.motorparams = []
            for row in loadWrk[5].split("$"):
                self.motorparams.append([])
                for col in row.split("#"):
                    self.motorparams[-1].append(float(col))
        else:
            self.id = id
            self.sensorweights = np.random.rand(c.numSensorNeurons,c.numInnerNeurons)*2-1
            self.innerweights = np.random.rand(c.numInnerNeurons,c.numInnerNeurons)*2-1
            self.motorweights = np.random.rand(c.numInnerNeurons,c.numMotorNeurons)*2-1
            self.sensorparams = np.random.rand(c.numSensorNeurons,4)*2-1
            self.innerparams = np.random.rand(c.numInnerNeurons,4)*2-1
            self.motorparams = np.random.rand(c.numMotorNeurons,4)*2-1
            if False:
                #			  rf	    lf	
                self.sensorweights = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.innerweights = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.motorweights = [[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
                self.sensorparams = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.innerparams = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                #				  										  
                self.motorparams = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

                #                     rf        lf
                self.sensorweights = [[1,0,-1,0],[-1,1,0,-1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.innerweights = [[1,0,1,0],[0,1,0,1],[1,0,1,1],[1,1,0,1]]
                self.motorweights = [[1,1,1,1,1,-1,1,0,1,0],[0,0,1,0,0,-1,0,1,0,-1],[0,0,0,-1,1,0,0,1,1,-1],[0,0,0,-1,0,0,0,1,0,-1]]
                self.sensorparams = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.innerparams = [[-.5,0,1,0],[-.5,0,1,1],[-.5,1,1,0],[-.5,1,1,1]]
                #
                self.motorparams = [[-.5,1,0,0],[-.5,-1,0,0],[1,1,0,0],[-.5,-1,0,0],[-.5,1,0,0],[-.5,-1,0,0],[1,-1,0,0],[1,1,0,0],[1,-1,0,0],[1,1,0,0]]



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
        pyrosim.Send_Cube(name="Torso",pos=[0,0,6.5],size=[2,1,4])


        pyrosim.Send_Joint( name = "Torso_LeftUpperLeg" , parent=
    "Torso" , child =
    "LeftUpperLeg" , type = "revolute", position = [0.75,0,4.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftUpperLeg",pos=[0,0,-1],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "LeftUpperLeg_LeftLowerLeg" , parent=
    "LeftUpperLeg" , child =
    "LeftLowerLeg" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLowerLeg",pos=[0,0,-1],size=[1,1,2])

        pyrosim.Send_Joint( name = "LeftLowerLeg_LeftFoot" , parent=
    "LeftLowerLeg" , child =
    "LeftFoot" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftFoot",pos=[0,0.25,-0.25],size=[1,1.5,0.5])
 

    
        pyrosim.Send_Joint( name = "Torso_RightUpperLeg" , parent=
    "Torso" , child =
    "RightUpperLeg" , type = "revolute", position = [-0.75,0,4.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightUpperLeg",pos=[0,0,-1],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "RightUpperLeg_RightLowerLeg" , parent=
    "RightUpperLeg" , child =
    "RightLowerLeg" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLowerLeg",pos=[0,0,-1],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "RightLowerLeg_RightFoot" , parent=
    "RightLowerLeg" , child =
    "RightFoot" , type = "revolute", position = [0,0,-2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightFoot",pos=[0,0.25,-0.25],size=[1,1.5,0.5])       


                
        pyrosim.Send_Joint( name = "Torso_LeftUpperArm" , parent=
    "Torso" , child =
    "LeftUpperArm" , type = "revolute", position = [1,0,8], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftUpperArm",pos=[0.5,0,-0.75],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "LeftUpperArm_LeftLowerArm" , parent=
    "LeftUpperArm" , child =
    "LeftLowerArm" , type = "revolute", position = [0.5,0,-1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLowerArm",pos=[0,0,-1],size=[1,1,2])
        
        
        
        pyrosim.Send_Joint( name = "Torso_RightUpperArm" , parent=
    "Torso" , child =
    "RightUpperArm" , type = "revolute", position = [-1,0,8], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightUpperArm",pos=[-0.5,0,-0.75],size=[1,1,2])
        
        pyrosim.Send_Joint( name = "RightUpperArm_RightLowerArm" , parent=
    "RightUpperArm" , child =
    "RightLowerArm" , type = "revolute", position = [-0.5,0,-1.5], jointAxis = "1 0 0") 
        pyrosim.Send_Cube(name="RightLowerArm",pos=[0,0,-1],size=[1,1,2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.id)+".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LeftFoot", T=self.sensorparams[0][0], Y=self.sensorparams[0][1], 
G=self.sensorparams[0][2], Z=self.sensorparams[0][3])
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "RightFoot", T=self.sensorparams[1][0], Y=self.sensorparams[1][1], 
G=self.sensorparams[1][2], Z=self.sensorparams[1][3])
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "zzzzz1", T=(self.sensorparams[2][0]/2+0.5)*10, Y=self.sensorparams[2][1],
G=self.sensorparams[2][2], Z=self.sensorparams[2][3])
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "zzzzz2", T=self.sensorparams[3][0], Y=self.sensorparams[3][1],
G=self.sensorparams[3][2], Z=self.sensorparams[3][3])
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "zzzzz3", T=self.sensorparams[4][0], Y=self.sensorparams[4][1],
G=self.sensorparams[4][2], Z=self.sensorparams[4][3])
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "zzzzz4", T=self.sensorparams[5][0], Y=self.sensorparams[5][1],
G=self.sensorparams[5][2], Z=self.sensorparams[5][3])

        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_RightUpperLeg", T=self.motorparams[0][0], Y=self.motorparams[0][1],
G=self.motorparams[0][2], Z=self.motorparams[0][3])
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LeftUpperLeg", T=self.motorparams[1][0], Y=self.motorparams[1][1],
G=self.motorparams[1][2], Z=self.motorparams[1][3])
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "RightUpperLeg_RightLowerLeg", T=self.motorparams[2][0], Y=self.motorparams[2][1],
G=self.motorparams[2][2], Z=self.motorparams[2][3])
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftUpperLeg_LeftLowerLeg", T=self.motorparams[3][0], Y=self.motorparams[3][1],
G=self.motorparams[3][2], Z=self.motorparams[3][3])
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "RightLowerLeg_RightFoot", T=self.motorparams[4][0], Y=self.motorparams[4][1],
G=self.motorparams[4][2], Z=self.motorparams[4][3])
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "LeftLowerLeg_LeftFoot", T=self.motorparams[5][0], Y=self.motorparams[5][1],
G=self.motorparams[5][2], Z=self.motorparams[5][3]) 
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_LeftUpperArm", T=self.motorparams[6][0], Y=self.motorparams[6][1],
G=self.motorparams[6][2], Z=self.motorparams[6][3])
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_RightUpperArm", T=self.motorparams[7][0], Y=self.motorparams[7][1],
G=self.motorparams[7][2], Z=self.motorparams[7][3])
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "LeftUpperArm_LeftLowerArm", T=self.motorparams[8][0], Y=self.motorparams[8][1],
	G=self.motorparams[8][2], Z=self.motorparams[8][3])
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightUpperArm_RightLowerArm", T=self.motorparams[9][0], Y=self.motorparams[9][1],
G=self.motorparams[9][2], Z=self.motorparams[9][3])



        for i in range(c.numInnerNeurons):
            pyrosim.Send_Hidden_Neuron( name = 16+i, linkName = "null", T=self.innerparams[i][0], Y=self.innerparams[i][1], 
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

