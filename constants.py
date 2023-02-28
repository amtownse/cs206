import numpy as np

debug = False
numberOfGenerations = 10
nog = numberOfGenerations
loopCount = 1000
lc = loopCount
time_sleep = 0.00001
ts = time_sleep
BLamp = np.pi/3
BLfeq = 1#1.7
BLoff = 0#0.01
FLamp = np.pi/3
FLfeq = 0.5#1.9
FLoff = 0#0.19
g = -9.8
populationSize = 10
ps = populationSize
numSensorNeurons = 4
numMotorNeurons = 8
motorJointRange = 0.2
motorStrength = 100
