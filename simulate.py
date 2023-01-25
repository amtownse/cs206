import pybullet as p
import pybullet_data
import time

def main():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
    robotId = p.loadURDF("body.urdf")
    for i in range(100000):
        if i%100==0:
            print(i)
        p.stepSimulation()
        time.sleep(1/500)
    p.disconnect()

main()
