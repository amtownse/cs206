import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os
import math

from motor import MOTOR
from sensor import SENSOR

class ROBOT:

    def __init__(self, id):
        self.sensors={}
        self.motors={}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+id+".nndf")
        os.system("rm brain"+id+".nndf")
        self.brainId = id
        self.nn.Print_Structure()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, tc):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(tc)

    
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.robotId)
    
    def Act(self, tc):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = c.motorJointRange * math.tanh(self.nn.Get_Value_Of(neuronName))
                self.motors[bytes(jointName, 'utf-8')].Set_Value(desiredAngle)


    def Think(self, tc):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        yCoordinateOfLinkZero = positionOfLinkZero[1]
        outfile = open('fitness'+self.brainId+'.txt','w')
        outfile.write(str(-yCoordinateOfLinkZero))
        outfile.close()
