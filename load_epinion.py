# Author: Luca Marini

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse


def load_graph(edges, link_prediction):
    V = set()
    E = []
    G = nx.MultiGraph()
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for line in datareader:
            if '#' not in line[0]:
                # if "\t" in line[0]:
                node_pair = line[0].split("\t")

                V.add(int(node_pair[0]))
                V.add(int(node_pair[1]))

                E.append((int(node_pair[0]), int(node_pair[1])))
                G.add_edge(int(node_pair[0]), int(node_pair[1]))

    V = list(V)
    nx.write_gpickle(G, "./data/Epinion-dataset/epinion_graph.gpickle")
    print(G)
    return G


def main(args):
    edges_path = "./data/Epinion-dataset/data/soc-Epinions1.txt"
    link_prediction = False
    load_graph(edges_path, link_prediction)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='load data into networkx pickle')

    # command-line arguments
    #parser.add_argument('edges_path', type=str,
    #                    help='path to csv-file of edges', action='store')
    #parser.add_argument('output_path', type=str,
    #                    help='path to store the networkx pickle', action='store')

    args = parser.parse_args()
    main(args)
