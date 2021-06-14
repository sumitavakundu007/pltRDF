import matplotlib.pyplot as plt
import numpy as np

class plot:
    def __init__(self, x, y, outfile):
        self.x = x;
        self.y = y;
        self.outfile = outfile

    def plotRDF(self):
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot(self.x, self.y, label="RDF")
        plt.title("RDF")
        ax.legend()
        plt.savefig(self.outfile, dpi=300)
