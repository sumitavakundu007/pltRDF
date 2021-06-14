from freud import density

class RDF:
    def __init__(self, bins, r_max, box, positions):
        self.bins = bins
        self.r_max = r_max
        self.box = box
        self.positions = positions

    def calc_RDF(self):
        RDF = density.RDF(self.bins, self.r_max)
        box_arr = self.box
        RDF.compute(system=(box_arr, self.positions), reset=False)

        return RDF.bin_centers, RDF.rdf