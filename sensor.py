import numpy as np
import constants as c

import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName, brainid):
        self.linkName = linkName
        self.values = np.zeros(c.loopCount)
        self.fin = False
        self.brainid = brainid

    def __del__(self):
        if self.fin:
            h="nope"
            #np.save("data/"+self.linkName+"Data"+self.brainid+".npy",self.values)

    def Get_Value(self, tc):
        if tc<c.loopCount:
            self.values[tc] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if tc == c.loopCount-1:
            self.fin = True
