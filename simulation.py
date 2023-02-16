import pybullet as p
import pybullet_data
import constants as c
import time as t
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI, id):
        self.fin = False
        self.id = id
        self.directOrGUI = directOrGUI
        if directOrGUI[0]=="D":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.g)
        self.world = WORLD()
        self.robot = ROBOT(self.id)

    def __del__(self):
        if self.fin:
            p.disconnect()

    def run(self):
        for tc in range(c.loopCount):
            p.stepSimulation()
            if self.directOrGUI[0] == "G":
                t.sleep(c.time_sleep)
                if tc%100==0:   
                    print(tc)
            self.robot.Sense(tc)
            self.robot.Think(tc)
            self.robot.Act(tc)
        self.fin = True

    def Get_Fitness(self):
        self.robot.Get_Fitness()
