import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

def main():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
    robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId)
    backLegSensorValues = numpy.zeros(10000)
    frontLegSensorValues = numpy.zeros(10000)
    for i in range(10000):
        if i%100==0:
            print(i)
        p.stepSimulation()
        backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        backLegSensorValues[i] = backLegTouch
        frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        frontLegSensorValues[i] = frontLegTouch
        time.sleep(1/10000)
    p.disconnect()
    numpy.save("data/backLegData.npy",backLegSensorValues)
    numpy.save("data/frontLegData.npy",frontLegSensorValues)

main()
