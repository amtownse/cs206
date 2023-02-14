import simulate as s
import os
from hillclimber import HILL_CLIMBER

def main():
    hc = HILL_CLIMBER()
    hc.Evolve()
#    os.system("python3 simulate.py")
#    for i in range(5):
#        os.system("python3 simulate.py")

main()
