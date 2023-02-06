import numpy as np
import constants as c

import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.loopCount)

    def __del__(self):
        np.save("data/"+self.linkName+"Data.npy",self.values)

    def Get_Value(self, tc):
        self.values[tc] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
