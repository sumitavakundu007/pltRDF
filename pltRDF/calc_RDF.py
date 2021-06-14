# This class calculates RDF using freud

from freud import density, box

class RDF:
    def __init__(self, bins, r_max, box, positions):
        self.bins = bins
        self.r_max = r_max
        self.box = box
        self.positions = positions

    def calc_RDF(self):
        RDF = density.RDF(self.bins, self.r_max)
        box_arr = box.Box(Lx=self.box[0], Ly=self.box[1], Lz=self.box[2],
                                                    xy=self.box[3], xz=self.box[4], yz=self.box[5], is2D=False)

        RDF.compute(system=(box_arr, self.positions), reset=False)

        return RDF.bin_centers, RDF.rdf
