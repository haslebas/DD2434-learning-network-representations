# Author: Luca Marini

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import pickle
from stellargraph.data import EdgeSplitter

def load_graph(edges, link_prediction):
    G = nx.MultiDiGraph()
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for line in datareader:
            if '#' not in line[0]:
                # if "\t" in line[0]:
                node_pair = line[0].split("\t")
                G.add_edge(int(node_pair[0]), int(node_pair[1]))

    return G

def main(args):
    edges_path = args.edges_path
    G = load_graph(edges_path, True)

    s = EdgeSplitter(G)
    G, E, _ = s.train_test_split(keep_connected=False, seed=args.seed)
    test_edges = []
    for edge in E:
        test_edges.append((int(edge[0]), int(edge[1])))

    print(test_edges[0])
    with open(args.output_path[:-8] + '_test_edges.pkl', 'wb') as f:
        pickle.dump(test_edges, f)
    nx.write_gpickle(G, args.output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='load data into networkx pickle')

    # command-line arguments
    parser.add_argument('edges_path', type=str,
        help='path to epinion edges', action='store')
    parser.add_argument('output_path', type=str,
        help='path to store the networkx pickle', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)

    args = parser.parse_args()
    main(args)
