# author: Luca Marini
from stellargraph import datasets


def get_dataset(dataset_name):
    if dataset_name == "cora":
        dataset = datasets.Cora()
    elif dataset_name == "pubmed":
        dataset = datasets.PubMedDiabetes()
    else:
        raise Exception('The specified dataset is not available')

    G, labels = dataset.load()
    nodes = list(G.nodes())
    return dataset, G, labels, nodes
