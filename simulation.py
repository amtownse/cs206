import pybullet as p
import pybullet_data
import constants as c
import time as t
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.fin = False
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.g)
        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        if self.fin:
            p.disconnect()

    def run(self):
        for tc in range(c.loopCount):
            if tc%100==0:
                print(tc)
            p.stepSimulation()
            t.sleep(c.time_sleep)
            self.robot.Sense(tc)
            self.robot.Think(tc)
            self.robot.Act(tc)
        self.fin = True
