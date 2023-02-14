import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time as t
import random as r
import constants as c
from simulation import SIMULATION
import generate as g
import sys

def main():
#    g.main()
    directOrGUI = "DIRECT"
    if len(sys.argv)>1:
        directOrGUI = sys.argv[1]
    simulation = SIMULATION(directOrGUI)
    simulation.run()
    simulation.Get_Fitness()
'''
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,c.g)
    planeId = p.loadURDF("plane.urdf")
pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'Torso_FrontLeg',controlMode = p.POSITION_CONTROL,
            targetPosition = frontLegMotorControl[i],maxForce = 90)    
p.loadSDF("world.sdf")
    robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId)
    backLegSensorValues = np.zeros(c.loopCount)
    backLegMotorControl = c.BLamp*np.sin(np.array(range(0,1000)) * np.pi / 180 * c.BLfeq + c.BLoff)
    frontLegSensorValues = np.zeros(c.loopCount)
    frontLegMotorControl = c.FLamp*np.sin(np.array(range(0,1000)) * np.pi / 180 * c.FLfeq + c.FLoff)
    for i in range(c.loopCount):
        if i%100==0:
            print(i)
        p.stepSimulation()
        backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        backLegSensorValues[i] = backLegTouch
        frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        frontLegSensorValues[i] = frontLegTouch
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg',controlMode = p.POSITION_CONTROL,
            targetPosition = backLegMotorControl[i],maxForce = 90)
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'Torso_FrontLeg',controlMode = p.POSITION_CONTROL,
            targetPosition = frontLegMotorControl[i],maxForce = 90)
        t.sleep(c.time_sleep)
    p.disconnect()
    np.save("data/backLegData.npy",backLegSensorValues)
    np.save("data/frontLegData.npy",frontLegSensorValues)
'''


if __name__ == "__main__":
    main()
