# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import random
import pickle
from stellargraph.data import EdgeSplitter

def load_graph(nodes, edges):
    G = nx.MultiGraph()

    # add the nodes
    add_nodes(G, nodes)
    add_edges(G, edges)

    return G


def add_nodes(G, nodes):
    with open(nodes, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for node in datareader:
            G.add_node(int(node[0]))

def add_edges(G, edges):
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for edge in datareader:
            G.add_edge(int(edge[0]), int(edge[1]))

def main(args):
    G = load_graph(args.nodes_path, args.edges_path)
    
    if args.lp:
        s = EdgeSplitter(G)
        G, E, _ = s.train_test_split(keep_connected=True, seed=args.seed)
        test_edges = []
        for edge in E:
            test_edges.append((int(edge[0]), int(edge[1])))
        
        with open(args.output_path[:-8] + '_test_edges.pkl', 'wb') as f:
            pickle.dump(test_edges, f)

    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    nx.write_gpickle(G, args.output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='load data into networkx pickle')

    # command-line arguments
    parser.add_argument('nodes_path', type=str, 
        help='path to csv-file of node-ids', action='store')
    parser.add_argument('edges_path', type=str, 
        help='path to csv-file of edges', action='store')
    parser.add_argument('output_path', type=str, 
        help='path to store the networkx pickle', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)
    parser.add_argument('-l', '--linkprediction', dest='lp', 
        help='add this flag if you want to use the graph for link prediction', action='store_true')

    args = parser.parse_args()
    random.seed(args.seed)
    main(args)