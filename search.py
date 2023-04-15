import simulate as s
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys
import constants as c

def main():
    loadOrRun = "R"
    if len(sys.argv)>1:
        loadOrRun = sys.argv[1]
    phc = PARALLEL_HILL_CLIMBER(loadOrRun)
    try:
        phc.Evolve()
    except:
        print("something went wrong")
    loadFile = open('save.txt','r')
    loadWrk = loadFile.read()
    loadFile.close()
    loadWrk = loadWrk.split("!")
    curGen = int(loadWrk[0])
    if curGen<c.numberOfGenerations-1:
        print("loading")
        phc = PARALLEL_HILL_CLIMBER("L")
        try:
            phc.Evolve()
        except:
            print("something went wrong")
#    os.system("python3 simulate.py")
#    for i in range(5):
#        os.system("python3 simulate.py")

main()
