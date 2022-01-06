# Code to load graph data as networkx graph and dump it as pickle file
# Author: Filippa Kärrfelt 2021-12-20

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import stellargraph as sg
import pickle
from stellargraph.data import EdgeSplitter
import pandas as pd


def load_graph(edges):
    G = nx.MultiDiGraph()

    # add the nodes
    V = add_graph_data(G, edges)
    return G, V

def add_graph_data(G, edges):
    V = {}
    count = 1
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for e in datareader:
            u = int(e[0])
            v = int(e[1])
            if u not in V:
                V[u] = count
                count += 1
            if v not in V:
                V[v] = count
                count += 1
            G.add_node(V[u])
            G.add_node(V[v])
            G.add_edge(V[u], V[v])

    return V

def save_labels_as_csv(labels_path, out_path, V):
    node_classes = {}
    node_labels = []
    class_num = 0
    with open(labels_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            node = int(row[0])
            label = row[1]
            if label in node_classes:
                node_labels.append([V[node], node_classes[label]])
            else:
                node_classes[label] = class_num
                class_num += 1
                node_labels.append([V[node], node_classes[label]])

    # write the labels to file
    df = pd.DataFrame(node_labels)
    df.to_csv(out_path + 'group-edges.csv', header=None, index=False)
    classes_list = list(node_classes.items())
    df_c = pd.DataFrame(classes_list)
    df_c.to_csv(out_path + 'groups.csv', header=None, index=False)

def main(args):
    G, V = load_graph(args.edges_path)
    save_labels_as_csv(args.classes_path, args.labels_output_path, V)
   
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
    parser.add_argument('labels_output_path', type=str, 
        help='path to store the label files', action='store')
    parser.add_argument('edges_path', type=str, 
        help='path to csv-file of edges', action='store')
    parser.add_argument('classes_path', type=str, 
        help='path to csv-file of edges', action='store')
    parser.add_argument('-l', '--linkprediction', dest='lp', 
        help='add this flag if you want to use the graph for link prediction', action='store_true')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)

    args = parser.parse_args()
    main(args)

