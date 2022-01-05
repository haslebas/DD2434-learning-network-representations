# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import stellargraph as sg
import pickle
from stellargraph.data import EdgeSplitter
import pandas as pd


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

def save_labels_as_csv(labels, path):
    node_classes = {}
    node_labels = []
    class_num = 0
    for node, label in labels.items():
        if label in node_classes:
            node_labels.append([node, node_classes[label]])
        else:
            node_classes[label] = class_num
            class_num += 1
            node_labels.append([node, node_classes[label]])
    # write the labels to file
    df = pd.DataFrame(node_labels)
    df.to_csv(path + 'group-edges.csv', header=None, index=False)
    classes_list = list(node_classes.items())
    df_c = pd.DataFrame(classes_list)
    df_c.to_csv(path + 'groups.csv', header=None, index=False)

def load_stellar_graph(dataset_name):
    if dataset_name == 'cora':
        dataset = sg.datasets.Cora()
        G, labels = dataset.load(directed=True)
        save_labels_as_csv(labels, args.labels_output_path)
    elif dataset_name == "pubmed":
        dataset = sg.datasets.PubMedDiabetes()
        G, labels = dataset.load()
        save_labels_as_csv(labels, args.labels_output_path)
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
    
    if args.lp:
        s = EdgeSplitter(G)
        G, E, _ = s.train_test_split(keep_connected=False, seed=args.seed)
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
    parser.add_argument('output_path', type=str, 
        help='path to store the networkx pickle', action='store')
    parser.add_argument('dataset_name', type=str, 
        help='name of the dataset', action='store')
    parser.add_argument('labels_output_path', type=str, 
        help='path to store the label files', action='store')
    parser.add_argument("-f", "--file", dest='from_file',
        help='True if loading graph from csv file', action="store_true")
    parser.add_argument('--nodes_path', type=str, 
        help='path to csv-file of node-ids', action='store')
    parser.add_argument('--edges_path', type=str, 
        help='path to csv-file of edges', action='store')
    parser.add_argument('-l', '--linkprediction', dest='lp', 
        help='add this flag if you want to use the graph for link prediction', action='store_true')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)

    args = parser.parse_args()
    main(args)

