import simulate as s
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys

def main():
    loadOrRun = "R"
    if len(sys.argv)>1:
        loadOrRun = sys.argv[1]
    phc = PARALLEL_HILL_CLIMBER(loadOrRun)
    phc.Evolve()
#    os.system("python3 simulate.py")
#    for i in range(5):
#        os.system("python3 simulate.py")

main()
