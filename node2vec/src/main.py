import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score

import os
import networkx as nx
import numpy as np
import pandas as pd

from stellargraph.data import BiasedRandomWalk
from stellargraph import StellarGraph
from stellargraph import datasets
from IPython.display import display, HTML

from gensim.models import Word2Vec


def set_p_q_params(dataset):
    if dataset == "BlogCatalog":
        return 0.25, 0.25

    elif dataset == "PPI":
        return 4, 1

    elif dataset == "Wikipedia":
        return 4, 0.5


def load_graph():
    dataset = datasets.Cora()
    display(HTML(dataset.description))
    return dataset.load(largest_connected_component_only=True)


if __name__ == "__main__":
    dataset = "BlogCatalog"
    n_walks = 100
    l_walks = 5

    G, subjects = load_graph()
    p, q = set_p_q_params(dataset)

    walker = BiasedRandomWalk(
        G,
        n=n_walks,
        length=l_walks,
        p=p,
        q=q,
    )


