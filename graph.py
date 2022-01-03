# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse

def load_graph(nodes, edges, undirected):
    G = nx.Graph()

    # add the nodes
    add_nodes(G, nodes)
    add_edges(G, edges, undirected)
    return G

def add_nodes(G, nodes):
    with open(nodes, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for node in datareader:
            G.add_node(int(node[0]))

def add_edges(G, edges, undirected):
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for edge in datareader:
            G.add_edge(int(edge[0]), int(edge[1]))
            if undirected:
                G.add_edge(int(edge[1]), int(edge[0]))

def main(args):
    # variable that must be true if the csv file containing the edges is about an undirected graph and does not contain
    # both direction of each edge
    undirected = True
    G = load_graph(args.nodes_path, args.edges_path, undirected)
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

    args = parser.parse_args()
    main(args)