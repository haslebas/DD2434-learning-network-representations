# Author: Luca Marini

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import pickle
from stellargraph.data import EdgeSplitter
import pandas as pd


def get_node_features_from_edges(edges_path, exclude_char, separator, directed):
    node_ids = []
    edges = {}
    with open(edges_path, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=separator)
        for line in datareader:
            if exclude_char not in line[0]:
                node_1 = int(line[0])
                node_2 = int(line[1])

                # add nodes without duplicates
                if node_1 not in node_ids:
                    node_ids.append(node_1)
                if node_2 not in node_ids:
                    node_ids.append(node_2)

                if directed:
                    edges.setdefault(node_1, []).append(node_2)
                else:
                    edges.setdefault(node_1, []).append(node_2)
                    edges.setdefault(node_2, []).append(node_1)

    node_ids.sort()
    node_features = pd.DataFrame(0, index=node_ids, columns=node_ids)
    if directed:
        for node_a, nodes in edges.items():
            for node in nodes:
                node_features.at[node_a, node] = 1
    else:
        for node_a, nodes in edges.items():
            for node in nodes:
                node_features.at[node_a, node] = 1
                node_features.at[node, node_a] = 1
    return node_features, node_ids


def load_graph(edges, exclude_char, separator, directed):
    if directed:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()
    with open(edges, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=separator)
        for line in datareader:
            if exclude_char not in line[0]:
                G.add_edge(int(line[0]), int(line[1]))
    return G


def main(args):
    edges_path = args.edges_path
    G = load_graph(edges_path, args.excl_char, args.separator, args.directed)

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
    parser.add_argument('--separator', dest='separator', type=str,
                        help='separator in csv file', action='store')
    parser.add_argument('--excl_char', dest='excl_char', type=str,
                        help='lines to exclude in csv file that contain the exclude char', action='store')
    parser.add_argument('-d', '--directed', dest='directed', 
        help='add this flag if you want to use a directed graph', action='store_true')

    args = parser.parse_args()
    main(args)
