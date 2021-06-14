# main function
from . import readGSD
from . import calc_RDF
from . import plot_matplotlib

def rdf(input_file, output_file):
    # inputs
    bins = float(input("Enter the number of bins: "))
    r_max = float(input("Enter the value of r_max: "))
    # num_particles, particles position, box info
    positions, box = readGSD.readGSD_func(input_file)
    # Calc RDF using Freud
    rdf_obj = calc_RDF.RDF(bins, r_max, box, positions)
    bin_centers, rdfs = rdf_obj.calc_RDF()
    # Plot in matplotlib
    plot_rdf = plot_matplotlib.plot(bin_centers, rdfs, output_file)
    plot_rdf.plotRDF()