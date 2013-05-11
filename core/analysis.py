import util
import similarity
import tokenizer
import graph
import matplotlib.pyplot as plt
import networkx as nx
import csv
from multiprocessing import Pool
import pickle
import numpy

def compute_number_sim_threshold(sim_threshold):
    g = graph.Graph(simm, sim_threshold)

    clustersize_clique = len(g.cliques())

    clustersize_single_link = len(g.single_link())

    clustersize_star = len(g.star())

    clustersize_string = len(g.string())

    return [sim_threshold, clustersize_clique, clustersize_single_link, clustersize_star, clustersize_string]

def compute_size_sim_threshold(sim_threshold):
    g = graph.Graph(simm, sim_threshold)

    clustersize_clique = numpy.mean(map(len, g.cliques()))

    clustersize_single_link = numpy.mean(map(len, g.single_link()))

    clustersize_star = numpy.mean(map(len, g.star()))

    clustersize_string = numpy.mean(map(len, g.string()))

    return [sim_threshold, clustersize_clique, clustersize_single_link, clustersize_star, clustersize_string]


def t(x):
    return x

if __name__ == "__main__":
    try:
        pkl_file = open('../analysis/simm.pkl', 'rb')
        simm = pickle.load(pkl_file)
        print 'SIM CACHED'
    except IOError:
        docs = util.getFileContent("../examples/TEST.DAT")
        tfm = tokenizer.createTermFrequencyMatrix(docs, 7)
        simm = similarity.calculateSimilarityMatrix(tfm)
        print 'SIM DONE'
        pkl_file = open('../analysis/simm.pkl', 'wb')
        pickle.dump(simm, pkl_file)

    import argparse

    parser = argparse.ArgumentParser(description='Produce data analysis for the different clustering algorithms.')

    parser.add_argument('--number', action='store_true',
                        help='analysis number of clusters by similarity threshold')

    parser.add_argument('--size', action='store_true',
                        help='analysis size of clusters by similarity threshold')

    args = parser.parse_args()

    if args.number:
        for t in xrange(10,200):
            row = compute_number_sim_threshold(t)

            with open('../analysis/similarity_threshold.csv', 'a') as f:
                 writer = csv.writer(f)
                 writer.writerow(row)

    elif args.size:
        for t in xrange(600,800):
            row = compute_size_sim_threshold(t)

            with open('../analysis/size_by_similarity_threshold.csv', 'a') as f:
                  writer = csv.writer(f)
                  writer.writerow(row)

    else:
        parser.print_help()
