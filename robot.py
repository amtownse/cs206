import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os
import math
import numpy as np

from motor import MOTOR
from sensor import SENSOR

class ROBOT:

    def __init__(self, id):
        self.sensors={}
        self.motors={}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense(id)
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+id+".nndf", self.robotId)
        os.system("rm brain"+id+".nndf")
        self.brainId = id
#        self.nn.Print_Structure()

    def Prepare_To_Sense(self, brainid):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, brainid)

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
                if jointName in c.ranges.keys():
                    desiredAngle = c.ranges[jointName][0]+c.ranges[jointName][1]*(math.tanh(self.nn.Get_Value_Of(neuronName))/2+0.5)
                self.motors[bytes(jointName, 'utf-8')].Set_Value(desiredAngle)


    def Think(self, tc):
        self.nn.Update()
#        if c.debug:
#            self.nn.Print()

    def Get_Fitness(self, curGen):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        yCoordinateOfLinkZero = positionOfLinkZero[1]
        zminTorso = p.getBasePositionAndOrientation(self.robotId)[0][2]
        angle1 = p.getBasePositionAndOrientation(self.robotId)[1][0]
        angle2 = p.getBasePositionAndOrientation(self.robotId)[1][1]
        outfile = open('fitness'+self.brainId+'.txt','w')
#        if int(curGen) < c.numberOfGenerations/2:
#        outfile.write(str(zminTorso))
#        outfile.write(str(zminTorso*yCoordinateOfLinkZero))
        outfile.write(str(zminTorso*yCoordinateOfLinkZero/(abs(angle1)+abs(angle2)+1)))
#        else:
#            outfile.write(str(abs(yCoordinateOfLinkZero*zminTorso**2/angle2/angle1)))
        outfile.close()
#        print(str(abs(yCoordinateOfLinkZero*(0.03 if zminTorso<3 else zminTorso)**2/(0.5+abs(angle2))/(0.5+abs(angle1)))))
#        print(p.getBasePositionAndOrientation(self.robotId))
