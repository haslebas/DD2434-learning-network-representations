# author: Luca Marini

from stellargraph import StellarGraph
from stellargraph import datasets
import networkx as nx  # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import pandas as pd
import json
from networkx.readwrite import json_graph
from LoadGraphs.load_graph_from_edges import get_node_features_from_edges


def get_graph_from_pickle(pickle_path, get_node_features=False, node_features=None):
    G = nx.read_gpickle(pickle_path)
    print(nx.info(G))
    if get_node_features:
        num_nodes = len(list(nx.nodes(G)))
        node_features = np.eye(num_nodes, dtype=int)
        node_features_df = pd.DataFrame(data=node_features)
        node_features_df.index += 1
        node_features_df.columns += 1

        G = StellarGraph.from_networkx(G, node_features=node_features_df)
    else:
        G = StellarGraph.from_networkx(G, node_features=node_features)
    return G


def get_node_ids(node_ids_path):
    node_ids_df = pd.read_csv(node_ids_path, index_col=False, header=None)
    node_ids = node_ids_df.set_index(0)[1]
    node_ids.name = "node_ids"
    # print(node_ids)
    return node_ids


def get_dataset(dataset_name):
    node_ids = []
    if dataset_name == "big_cora":
        G = get_graph_from_pickle("../data/subelj_cora/cora_big_graph_dir.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/subelj_cora/data/group-edges.csv")
    elif dataset_name == "small_cora":
        #G = get_graph_from_pickle("../data/Cora-dataset/cora_graph_dir_lp.gpickle", get_node_features=True)
        #node_ids = get_node_ids("../data/Cora-dataset/data/group-edges.csv")
        dataset = datasets.Cora()
        G, node_ids = dataset.load(directed=True)
    elif dataset_name == "pubmed":
        G = get_graph_from_pickle("../data/PubMed/pubmed_graph_dir_lp.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/PubMed/data/group-edges.csv")
    elif dataset_name == "pubmed_undir":
        G = get_graph_from_pickle("../data/pubmed-dataset/pubmed_graph_undir_lp.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/pubmed-dataset/data/group-edges.csv")
        # dataset = datasets.PubMedDiabetes()
        # G, node_ids = dataset.load()
    elif dataset_name == "blog_catalog":
        G = get_graph_from_pickle("../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/BlogCatalog-dataset/data/group-edges.csv")
    elif dataset_name == "youtube":
        G = get_graph_from_pickle("../data/YouTube-dataset/youtube_graph.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/YouTube-dataset/data/group-edges.csv")
    elif dataset_name == "flickr":
        G = get_graph_from_pickle("../data/Flickr-dataset/flickr_graph.gpickle", get_node_features=True)
        node_ids = get_node_ids("../data/Flickr-dataset/data/group-edges.csv")
    elif dataset_name == "twitter":
        node_features, node_ids = get_node_features_from_edges("../data/Twitter-dataset/data/out.munmun_twitter_social",
                                                               "%", " ", directed=True)
        G = get_graph_from_pickle("../data/Twitter-dataset/twitter_graph_dir_lp.gpickle", get_node_features=False,
                                  node_features=node_features)
    elif dataset_name == "ppi":
        node_features, node_ids = get_node_features_from_edges("../data/PPI-dataset/PP-Pathways_ppi.csv", "#", ",",
                                                               directed=False)
        G = get_graph_from_pickle("../data/PPI-dataset/ppi_graph_lp.gpickle", get_node_features=False,
                                  node_features=node_features)
    elif dataset_name == "astro-ph":
        node_features, node_ids = get_node_features_from_edges("../data/AstroPh-dataset/ca-AstroPh.txt", "#", "\t",
                                                               directed=False)
        G = get_graph_from_pickle("../data/AstroPh-dataset/astro_graph_lp.gpickle", get_node_features=False,
                                  node_features=node_features)
    elif dataset_name == "epinion":
        node_features, node_ids = get_node_features_from_edges("../data/Epinions-dataset/soc-Epinions1.txt", "#", "\t",
                                                               directed=True)
        G = get_graph_from_pickle("../data/Epinions-dataset/epinions_graph_dir_lp.gpickle", get_node_features=False,
                                  node_features=node_features)
    elif dataset_name == "reddit":
        prefix = "../data/reddit/reddit"
        G_data = json.load(open(prefix + "-G.json"))
        G = json_graph.node_link_graph(G_data)
        if isinstance(G.nodes()[0], int):
            conversion = lambda n: int(n)
        else:
            conversion = lambda n: n
        G = get_graph_from_pickle("../data/reddit/reddit_graph.gpickle", get_node_features=True)
        class_map = json.load(open(prefix + "-class_map.json"))
        if isinstance(list(class_map.values())[0], list):
            lab_conversion = lambda n: n
        else:
            lab_conversion = lambda n: int(n)

        class_map = {conversion(k): lab_conversion(v) for k, v in class_map.items()}
        node_ids = class_map.values()
    elif dataset_name == "dblp-ci":
        node_features, node_ids = get_node_features_from_edges("../data/DBLP-Ci-dataset/dblp-cite.edges", "%", ",",
                                                               directed=True)
        G = get_graph_from_pickle("../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle", get_node_features=True,
                                  node_features=node_features)
    elif dataset_name == "dblp-au":
        node_features, node_ids = get_node_features_from_edges("../data/DBLP-Au-dataset/com-dblp.ungraph.txt", "#",
                                                               "\t", directed=True)
        G = get_graph_from_pickle("../data/DBLP-Au-dataset/dblp-au_graph_lp.gpickle", get_node_features=True,
                                  node_features=node_features)
    else:
        raise Exception('The specified dataset is not available')
    print(G.info())
    nodes = list(G.nodes())
    return G, node_ids, nodes
