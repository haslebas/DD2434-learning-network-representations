from stellargraph import datasets


def get_cora():
    dataset = datasets.Cora()
    G, labels = dataset.load()
    nodes = list(G.nodes())

    return dataset, G, labels, nodes
