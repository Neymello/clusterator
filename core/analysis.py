import util
import similarity
import tokenizer
import graph
import matplotlib.pyplot as plt
import networkx as nx
import csv
import pickle
import numpy
from pprint import pprint

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

def show_cluster_example(sim_threshold):
    g = graph.Graph(simm, 150)

    clustersize_clique = [c for c in g.cliques() if len(c) == 8][0]
    sg = g.nx_graph.subgraph(clustersize_clique)
    nx.draw_circular(sg, alpha=0.8, node_size=2000, node_color='b')
    plt.show()

    clustersize_star = [c for c in g.star() if len(c) == 10][0]
    sg = g.nx_graph.subgraph(clustersize_star)
    pos = nx.spring_layout(sg)
    nx.draw(sg, alpha=0.8, node_size=2000, node_color='b', pos=pos)
    plt.show()

    clustersize_string = g.string()[0]
    sg = g.nx_graph.subgraph(clustersize_string)
    nx.draw_random(sg, alpha=0.8, node_size=2000, node_color='b')
    plt.show()

    #g = graph.Graph(simm, 600)

    clustersize_single_link = []# map(len, g.single_link())

    return [sim_threshold, clustersize_clique, clustersize_single_link, clustersize_star, clustersize_string]

def draw_cluster(g, c):
    sg = g.nx_graph.subgraph(c)
    nx.draw_circular(sg, alpha=0.8, node_size=2000, node_color='b')
    plt.show()

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

    parser.add_argument('--cluster', action='store_true',
                        help='show an example of a cluster for each algorithm')

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

    elif args.cluster:
        pprint(show_cluster_example(150))


    else:
        parser.print_help()
