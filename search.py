import simulate as s
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

def main():
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
#    os.system("python3 simulate.py")
#    for i in range(5):
#        os.system("python3 simulate.py")

main()
