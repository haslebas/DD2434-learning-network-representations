# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse

def load_graph(nodes, edges):
    G = nx.Graph()

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
    nodes = args.nodes_path # '../data/BlogCatalog-dataset/data/nodes.csv'
    edges = args.edges_path # '../data/BlogCatalog-dataset/data/edges.csv'
    output_file = args.output_path # 'blog_catalog_graph'
    G = load_graph(nodes, edges)
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    nx.write_gpickle(G, output_file) # '../data/BlogCatalog-dataset/blog_catalog_graph.gpickle')

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