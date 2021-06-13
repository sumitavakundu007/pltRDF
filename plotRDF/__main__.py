# main function
import os
import argparse
import readGSD
from calc_RDF import RDF 
from plot_matplotlib import plot_matplotlib 

parser = argparse.ArgumentParser(description='Process some images')
parser.add_argument('--input', help='the input file', required=True)
parser.add_argument('--output', help='the output file', required=True)

args = parser.parse_args()

def main():
    # inputs
    bins = 50
    r_max = 5
    # num_particles, particles position, box info
    num_particles, positions, box = readGSD.readGSD_func(args.input)
    # Calc RDF using Freud
    rdf_obj = RDF(bins, r_max, box, positions)
    bin_centers, rdfs = rdf_obj.calc_RDF()
    # Plot in matplotlib
    plot_rdf = plot_matplotlib(bin_centers, rdfs, args.output)
    plot_rdf.plotRDF()

if __name__=='__main__':
    main()
