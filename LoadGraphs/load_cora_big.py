# Code to load graph data as networkx graph and dump it as pickle file
# Right now this file is used to load the Cora, DBLP-Au and DBLP-Ci datasets
# Author: Filippa Kärrfelt 2022-01-06

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import stellargraph as sg
import pickle
from stellargraph.data import EdgeSplitter
import pandas as pd


def load_graph(edges, dataset):
    G = nx.MultiDiGraph()

    # add the nodes
    add_graph_data(G, edges, dataset)
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges))) 
    return G

def add_graph_data(G, edges, dataset):
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        it = 0
        for edge in datareader:
            if dataset == 'DBLP-AU':
                if (it > 3):
                    e = edge[0].split()
                    if len(e) == 2:
                        G.add_node(int(e[0]))
                        G.add_node(int(e[1]))
                        G.add_edge(int(e[0]), int(e[1]))
            else:
                if (it > 1):
                    if dataset == 'DBLP':
                        e = edge
                    else:
                        e = edge[0].split()
                    if len(e) == 2:
                        G.add_node(int(e[0]))
                        G.add_node(int(e[1]))
                        G.add_edge(int(e[0]), int(e[1]))
            it += 1


def save_labels_as_csv(labels_path, out_path):
    node_classes = {}
    node_labels = []
    class_num = 0
    with open(labels_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        it = 1
        for row in datareader:
            node = it
            label = row[0].strip()
            if label in node_classes:
                node_labels.append([node, node_classes[label]])
            else:
                node_classes[label] = class_num
                class_num += 1
                node_labels.append([node, node_classes[label]])
            it += 1

    # write the labels to file
    df = pd.DataFrame(node_labels)
    df.to_csv(out_path + 'group-edges.csv', header=None, index=False)
    classes_list = list(node_classes.items())
    df_c = pd.DataFrame(classes_list)
    df_c.to_csv(out_path + 'groups.csv', header=None, index=False)

def main(args):
    G = load_graph(args.edges_path, args.dataset)
    if args.load_classes:
        save_labels_as_csv(args.classes_path, args.labels_output_path)
   
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
    parser.add_argument('dataset', type=str, 
        help='separator between nodes in graph edge txt file', action='store')
    parser.add_argument('-c', '--classes', dest='load_classes', 
        help='add this flag if class labels should be added', action='store_true')
    parser.add_argument('--classes_path', type=str, 
        help='path to csv-file of edges', action='store')
    parser.add_argument('-l', '--linkprediction', dest='lp', 
        help='add this flag if you want to use the graph for link prediction', action='store_true')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)

    args = parser.parse_args()
    main(args)

