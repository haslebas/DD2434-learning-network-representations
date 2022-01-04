# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import random
import pickle


def load_graph(nodes, edges, link_prediction):
    G = nx.Graph()

    # add the nodes
    V = add_nodes(G, nodes)
    test_edges = add_edges(G, edges, link_prediction)

    # add negative samples for link_prediction
    # TODO: make sure that negative samples are truly negative
    m = len(test_edges)
    A = random.choices(V, k=m)
    B = random.choices(V, k=m)
    test_edges.extend(zip(A, B))

    return G, test_edges


def add_nodes(G, nodes):
    V = []
    with open(nodes, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for node in datareader:
            V.append(int(node[0]))
            G.add_node(int(node[0]))
    return V


def add_edges(G, edges, link_prediction):
    E = []
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for edge in datareader:
            # TODO: make sure that no node ends up isolated
            coin = random.randint(0, 1)
            if coin and link_prediction:
                E.append((int(edge[0]), int(edge[1])))
            else:
                G.add_edge(int(edge[0]), int(edge[1]))
    return E

def main(args):
    G, test_edges = load_graph(args.nodes_path, args.edges_path, args.lp)
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    nx.write_gpickle(G, args.output_path)
    if args.lp:
        with open(args.output_path[:-8] + '_test_edges.pkl', 'wb') as f:
            pickle.dump(test_edges, f)

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