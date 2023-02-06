import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

from motor import MOTOR
from sensor import SENSOR

class ROBOT:

    def __init__(self):
        self.sensors={}
        self.motors={}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, tc):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(tc)

    
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            amp = c.BLamp if jointName==b'Torso_BackLeg' else c.FLamp if jointName==b'Torso_FrontLeg' else 1
            feq = c.BLfeq if jointName==b'Torso_BackLeg' else c.FLfeq if jointName==b'Torso_FrontLeg' else 1
            off = c.BLoff if jointName==b'Torso_BackLeg' else c.FLoff if jointName==b'Torso_FrontLeg' else 0
            self.motors[jointName] = MOTOR(jointName, self.robotId, amp, feq, off)
    
    def Act(self, tc):
        for motor in self.motors:
            self.motors[motor].Set_Value(tc)
