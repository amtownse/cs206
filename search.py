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
    phc.Evolve()

main()
