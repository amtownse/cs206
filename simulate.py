import pybullet as p
import time

def main():
    physicsClient = p.connect(p.GUI)
    for i in range(1000):
        if i%100==0:
            print(i)
        p.stepSimulation()
        time.sleep(1/500)
    p.disconnect()

main()
