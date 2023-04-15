import os
import constants as c


def main():
    os.system("python3 search.py R")
    loadFile = open('save.txt','r')
    loadWrk = loadFile.read()
    loadFile.close()
    loadWrk = loadWrk.split("!")
    curGen = int(loadWrk[0])
    if curGen<c.numberOfGenerations-1:
        print("loading")
        os.system("python3 search.py L")
        loadFile = open('save.txt','r')
        loadWrk = loadFile.read()
        loadFile.close()
        loadWrk = loadWrk.split("!")
        curGen = int(loadWrk[0])

main()
