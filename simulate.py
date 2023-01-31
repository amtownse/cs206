import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random as r

def main():
    BLamp = numpy.pi/3
    BLfeq = 1.7
    BLoff = 0.01
    FLamp = numpy.pi/3
    FLfeq = 1.9
    FLoff = 0.19


    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
    robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId)
    backLegSensorValues = numpy.zeros(1000)
    backLegMotorControl = BLamp*numpy.sin(numpy.array(range(0,1000)) * 
numpy.pi / 180 * BLfeq + BLoff)
    frontLegMotorControl = FLamp*numpy.sin(numpy.array(range(0,1000)) *
numpy.pi / 180 * FLfeq + FLoff)
    frontLegSensorValues = numpy.zeros(1000)
    for i in range(1000):
        if i%100==0:
            print(i)
        p.stepSimulation()
        backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        backLegSensorValues[i] = backLegTouch
        frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        frontLegSensorValues[i] = frontLegTouch
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
            jointName = b'Torso_BackLeg',controlMode = p.POSITION_CONTROL,
            targetPosition = backLegMotorControl[i],maxForce = 
90)
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
            jointName = b'Torso_FrontLeg',controlMode = p.POSITION_CONTROL,
            targetPosition = frontLegMotorControl[i],maxForce = 
90)
        time.sleep(1/1000)
    p.disconnect()
    numpy.save("data/backLegData.npy",backLegSensorValues)
    numpy.save("data/frontLegData.npy",frontLegSensorValues)

main()
