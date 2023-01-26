import matplotlib.pyplot as pyplot
import numpy

def main():
    backLegData = numpy.load("data/backLegData.npy")
    frontLegData = numpy.load("data/frontLegData.npy")
    pyplot.plot(backLegData, label="back leg", linewidth=5)
    pyplot.plot(frontLegData, label="front leg")
    pyplot.legend()
    pyplot.show()

main()
