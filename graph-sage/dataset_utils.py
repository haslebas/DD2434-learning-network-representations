# author: Luca Marini
from stellargraph import StellarGraph
from stellargraph import datasets
import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import numpy as np
import pandas as pd


def get_graph_from_pickle(pickle_path, get_node_features=False, nodes_path=None):
    G = nx.read_gpickle(pickle_path)
    if get_node_features:
        nodes_df = pd.read_csv(nodes_path, index_col=False, header=None)
        node_features = np.eye(len(nodes_df.index), dtype=int)
        node_features_df = pd.DataFrame(data=node_features)  # , index = data[1:, 0], columns = data[0, 1:])
        node_features_df.index += 1
        node_features_df.columns += 1

        G = StellarGraph.from_networkx(G, node_features=node_features_df)
    return G


def get_node_labels(node_labels_path):
    node_labels_df = pd.read_csv(node_labels_path, index_col=False, header=None)
    labels = node_labels_df.set_index(0)[1]
    labels.name = "labels"
    #print(labels)
    return labels


def get_dataset(dataset_name):
    labels = []
    if dataset_name == "cora":
        dataset = datasets.Cora()
        G, labels = dataset.load()
    elif dataset_name == "pubmed":
        dataset = datasets.PubMedDiabetes()
        G, labels = dataset.load()
    elif dataset_name == "blog_catalog":
        G = get_graph_from_pickle("../data/BlogCatalog-dataset/blog_catalog_graph.gpickle", get_node_features=True,
                                  nodes_path="../data/BlogCatalog-dataset/data/nodes.csv")

        labels = get_node_labels("../data/BlogCatalog-dataset/data/group-edges.csv")
    elif dataset_name == "youtube":
        G = get_graph_from_pickle("../data/YouTube-dataset/youtube_graph.gpickle", get_node_features=True,
                                  nodes_path="../data/YouTube-dataset/data/nodes.csv")

        labels = get_node_labels("../data/YouTube-dataset/data/group-edges.csv")
    else:
        raise Exception('The specified dataset is not available')

    nodes = list(G.nodes())
    return G, labels, nodes
