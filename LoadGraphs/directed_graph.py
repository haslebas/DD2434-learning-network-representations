# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import stellargraph as sg
# from stellargraph import StellarGraph
# from stellargraph import datasets

def load_graph(nodes, edges):
    G = nx.MultiDiGraph()

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

def load_stellar_graph(dataset_name):
    if dataset_name == 'cora':
        dataset = sg.datasets.Cora()
        G, labels = dataset.load(directed=True)
    elif dataset_name == "pubmed":
        dataset = sg.datasets.PubMedDiabetes()
        G, labels = dataset.load()
    # transform stellargraph to networkx graph representation
    G_nx = G.to_networkx()
    print('G nx: ', G_nx)
    return G_nx

def main(args):
    if args.from_file:
        print('Loading graph from local csv files.')
        G = load_graph(args.nodes_path, args.edges_path)
    else: 
        print('Loading graph from StellarGraph datasets.')
        G = load_stellar_graph(args.dataset_name)
    
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    nx.write_gpickle(G, args.output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='load data into networkx pickle')

    # command-line arguments
    parser.add_argument('output_path', type=str, 
        help='path to store the networkx pickle', action='store')
    parser.add_argument('dataset_name', type=str, 
        help='name of the dataset', action='store')
    parser.add_argument("-f", "--file", dest='from_file',
        help='True if loading graph from csv file', action="store_true")
    parser.add_argument('--nodes_path', type=str, 
        help='path to csv-file of node-ids', action='store')
    parser.add_argument('--edges_path', type=str, 
        help='path to csv-file of edges', action='store')

    args = parser.parse_args()
    main(args)

