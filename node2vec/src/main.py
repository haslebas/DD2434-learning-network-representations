import networkx as nx
#import node2vecgood as n2v
import argparse
import pickle
import numpy as np
from node2vec import Graph


def parse_args():
    """
    Parses the node2vec arguments.
    """

    parser = argparse.ArgumentParser(description="Run node2vec.")

    parser.add_argument('--input', nargs='?', default='./graph/BlogCatalog.edgelist',
                        help='Input graph path')

    parser.add_argument('--output', nargs='?', default='../emb/karate.emb',
                        help='Embeddings path')

    parser.add_argument('--dimensions', type=int, default=3,
                        help='Number of dimensions. Default is 128.')

    parser.add_argument('--walk-length', type=int, default=5,
                        help='Length of walk per source. Default is 80.')

    parser.add_argument('--num-walks', type=int, default=10,
                        help='Number of walks per source. Default is 10.')

    parser.add_argument('--window-size', type=int, default=10,
                        help='Context size for optimization. Default is 10.')

    parser.add_argument('--iter', default=1, type=int,
                        help='Number of epochs in SGD')

    parser.add_argument('--workers', type=int, default=8,
                        help='Number of parallel workers. Default is 8.')

    parser.add_argument('--p', type=float, default=0.25,
                        help='Return hyperparameter. Default is 0.25')

    parser.add_argument('--q', type=float, default=0.25,
                        help='Inout hyperparameter. Default is 0.25')

    parser.add_argument('--weighted', dest='weighted', action='store_true',
                        help='Boolean specifying (un)weighted. Default is unweighted.')
    parser.add_argument('--unweighted', dest='unweighted', action='store_false')
    parser.set_defaults(weighted=False)

    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='undirected', action='store_false')
    parser.set_defaults(directed=False)

    parser.add_argument('--dataset', nargs='?', default='BlogCatalog',
                        help='Name of dataset')

    return parser.parse_args()


def set_p_q_params(dataset):
    if dataset == "BlogCatalog":
        return 0.25, 0.25

    elif dataset == "PPI":
        return 4, 1

    elif dataset == "Wikipedia":
        return 4, 0.5


def main(args):
    nx_G = nx.read_gpickle(args.input)
    p, q = set_p_q_params(args.dataset)

    node2vec_g = Graph(nx_G, dimensions=32, walk_length=20, num_walks=200,
                     workers=4, p=p, q=q, sampling_strategy={'q', 'p'})

    model = node2vec_g.fit(window=10, min_count=1, batch_words=4)

    model.wv.save_word2vec_format(args.output + '.txt')

    # make embedding a dict:
    E = {}
    node_embeddings = open(args.output + '.txt', 'r')
    nodes = node_embeddings.readlines()

    # print(nodes)

    num_nodes = nodes[0]
    print('num nodes: ', num_nodes)
    for node in nodes[1:]:
        tok = node.split()
        key = int(tok[0])
        val = np.array(tok[1:], dtype=float)
        E[key] = val

    with open(args.output + '.pkl', 'wb') as handle:
        pickle.dump(E, handle)
    print('Saved Node2Vec embeddings to pkl file')


"""
def load_graph():
    dataset = datasets.Cora()
    display(HTML(dataset.description))
    return dataset.load(largest_connected_component_only=True)
"""


if __name__ == "__main__":
    args = parse_args()
    main(args)



    """
    G, subjects = load_graph()

    walker = BiasedRandomWalk(
        G,
        n=n_walks,
        length=l_walks,
        p=p,
        q=q,
    )
    """

