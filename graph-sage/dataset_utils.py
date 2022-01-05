# author: Luca Marini
import stellargraph as sg
from stellargraph import StellarGraph
from stellargraph import datasets
import networkx as nx  # https://networkx.org/documentation/stable/tutorial.html
import csv
import numpy as np
import pandas as pd
import os


def get_graph_from_pickle(pickle_path, get_node_features=False):
    G = nx.read_gpickle(pickle_path)
    if get_node_features:
        num_nodes = len(list(nx.nodes(G)))
        node_features = np.eye(num_nodes, dtype=int)
        node_features_df = pd.DataFrame(data=node_features)
        node_features_df.index += 1
        node_features_df.columns += 1

        G = StellarGraph.from_networkx(G, node_features=node_features_df)
    else:
        G = StellarGraph.from_networkx(G)
    return G


def get_node_labels(node_labels_path):
    node_labels_df = pd.read_csv(node_labels_path, index_col=False, header=None)
    labels = node_labels_df.set_index(0)[1]
    labels.name = "labels"
    # print(labels)
    return labels


def get_dataset(dataset_name):
    labels = []
    if dataset_name == "cora":
        dataset = datasets.Cora()
        G, labels = dataset.load(directed=True)
    elif dataset_name == "pubmed":
        dataset = datasets.PubMedDiabetes()
        G, labels = dataset.load()
    elif dataset_name == "blog_catalog":
        G = get_graph_from_pickle("../data/BlogCatalog-dataset/blog_catalog_graph.gpickle", get_node_features=True)
        labels = get_node_labels("../data/BlogCatalog-dataset/data/group-edges.csv")
    elif dataset_name == "youtube":
        G = get_graph_from_pickle("../data/YouTube-dataset/youtube_graph.gpickle", get_node_features=True)
        labels = get_node_labels("../data/YouTube-dataset/data/group-edges.csv")
    elif dataset_name == "flickr":
        G = get_graph_from_pickle("../data/Flickr-dataset/flickr_graph.gpickle", get_node_features=True)
        labels = get_node_labels("../data/Flickr-dataset/data/group-edges.csv")
    elif dataset_name == "reddit":
        G = get_graph_from_pickle("../data/Reddit-dataset/reddit_graph.gpickle", get_node_features=True)
    elif dataset_name == "epinion":
        G = get_graph_from_pickle("../data/Epinion-dataset/epinion_graph.gpickle", get_node_features=True)
        # TODO: node_ids
    elif dataset_name == "dbpl":
        # https://stellargraph.readthedocs.io/en/stable/demos/link-prediction/attri2vec-link-prediction.html
        data_dir = "../data/DBLP-dataset/data/"

        # Load the graph from the edge list
        edgelist = pd.read_csv(
            os.path.join(data_dir, "edgeList.txt"),
            sep=",",
            header=None,
            names=["source", "target"],
        )
        edgelist["label"] = "cites"  # set the edge type

        # Load paper content features, subjects and publishing years
        feature_names = ["w_{}".format(ii) for ii in range(2476)]
        node_column_names = feature_names + ["subject", "year"]
        node_data = pd.read_csv(
            os.path.join(data_dir, "content.txt"), sep="\t", header=None, names=node_column_names
        )
        # Construct the whole graph from edge list
        G_all_nx = nx.from_pandas_edgelist(edgelist, edge_attr="label")
        # Specify node types
        nx.set_node_attributes(G_all_nx, "paper", "label")
        # Get node features
        all_node_features = node_data[feature_names]
        # Create the Stellargraph with node features
        G = sg.StellarGraph.from_networkx(G_all_nx, node_features=all_node_features)
    else:
        raise Exception('The specified dataset is not available')
    print(G.info())
    nodes = list(G.nodes())
    #print(nodes)
    return G, labels, nodes
