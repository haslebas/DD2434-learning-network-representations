from stellargraph import datasets


def get_dataset(dataset_name):
    if dataset_name == "cora":
        dataset = datasets.Cora()
        G, labels = dataset.load()
        nodes = list(G.nodes())
    else:
        raise Exception('The specified dataset is not available')

    return dataset, G, labels, nodes
