import numpy as np
import constants as c

import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName, robotId, amp, feq, off):
        self.jointName = jointName
        self.values = amp*np.sin(np.array(range(0,c.loopCount)) * np.pi / 180 * feq + off)
        self.robotId = robotId
        self.amp = amp
        self.feq = feq
        self.off = off

    def Set_Value(self, tc):
        pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = self.jointName,controlMode = p.POSITION_CONTROL,
            targetPosition = self.values[tc], maxForce = 90)

