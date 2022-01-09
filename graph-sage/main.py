# author: Luca Marini
# inspired by https://colab.research.google.com/github/stellargraph/stellargraph/blob/master/demos/embeddings/
# graphsage-unsupervised-sampler-embeddings.ipynb

import argparse
import random
from stellargraph.mapper import GraphSAGELinkGenerator
from stellargraph.layer import GraphSAGE, link_classification
from stellargraph.data import UnsupervisedSampler
from tensorflow import keras
from stellargraph.mapper import GraphSAGENodeGenerator
import pickle
from dataset_utils import *
from NodeClassification.node_classification import get_score


def main(args):
    # load dataset
    G, labels, nodes = get_dataset(args.dataset_name)

    unsupervised_samples = UnsupervisedSampler(
        G, nodes=nodes, length=args.length, number_of_walks=args.number_of_walks
    )

    generator = GraphSAGELinkGenerator(G, args.batch_size, args.num_samples)
    train_gen = generator.flow(unsupervised_samples)

    graphsage_model = GraphSAGE(
        layer_sizes=args.layer_sizes, generator=generator, bias=True, dropout=args.dropout, normalize=args.normalization
    )

    # Build the model and expose input and output sockets of graphsage, for node pair inputs:
    x_inp, x_out = graphsage_model.in_out_tensors()

    prediction = link_classification(
        output_dim=1, output_act="sigmoid", edge_embedding_method="ip"
    )(x_out)

    model = keras.Model(inputs=x_inp, outputs=prediction)

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=args.learning_rate),
        loss=keras.losses.binary_crossentropy,
        metrics=[keras.metrics.binary_accuracy]
    )

    history = model.fit(
        train_gen,
        epochs=args.epochs,
        verbose=1,
        use_multiprocessing=False,
        workers=4,
        shuffle=True,
    )

    x_inp_src = x_inp[0::2]
    x_out_src = x_out[0]
    embedding_model = keras.Model(inputs=x_inp_src, outputs=x_out_src)
    if args.labels_ids:
        node_ids = labels.index
    else:
        node_ids = labels

    node_gen = GraphSAGENodeGenerator(G, args.batch_size, args.num_samples).flow(node_ids)

    node_embeddings = embedding_model.predict(node_gen, workers=4, verbose=1)

    # dictionary with the embeddings
    E = {}
    for i, node_id in enumerate(node_ids):
        if args.labels_ids:
            node_subject = labels.astype("category").cat.codes
            E[node_id] = node_embeddings[node_subject[node_id]]
        else:
            E[node_id] = node_embeddings[i]
    # write the learned node embeddings into a pickle file
    with open(args.output_path, 'wb') as handle:
        pickle.dump(E, handle)

    # node classification
    if args.task == "nc":
        X = node_embeddings
        if args.labels_ids:
            y = np.array(node_subject)
        else:
            y = np.array(node_ids)

        get_score(X, y, args.seed, args.dataset_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='graphsage - generation of node embeddings')

    # command-line arguments
    parser.add_argument('-output_path', type=str,
                        help='path to output file where node embeddings are stored', action='store',
                        default='../embeddings/pubmed_graphsage_lp.pkl')
    parser.add_argument('-lbls_ids', dest='labels_ids',
                        help='are labels already ids', action='store_true') #, default=True)
    parser.add_argument('-task', dest='task', type=str,
                        help='are labels already ids', action='store', default="nc")
    parser.add_argument('-dataset', dest='dataset_name', type=str,
                        help='chosen dataset', action='store', default="pubmed")
    parser.add_argument('--seed', dest='seed', type=int,
                        help='fix random seeds', action='store', default=1)
    parser.add_argument('-e', dest='epochs', type=int,
                        help='number of epochs', action='store', default=1)
    parser.add_argument('-nw', dest='number_of_walks', type=int,
                        help='number of walks to take per node', action='store', default=1)
    parser.add_argument('-l', dest='length', type=int,
                        help='length of each walk', action='store', default=5)
    parser.add_argument('-bs', dest='batch_size', type=int,
                        help='minibatch size', action='store', default=50)
    parser.add_argument('-ns', dest='num_samples', type=list,
                        help='sizes of 1- and 2-hop neighbor samples', action='store', default=[10, 5])
    parser.add_argument('-ls', dest='layer_sizes', type=list,
                        help='number of neurons in the 2-layer GraphSAGE encoder', action='store', default=[50, 50])
    parser.add_argument('-d', dest='dropout', type=float,
                        help='dropout rate', action='store', default=0.0)
    parser.add_argument('-norm', dest='normalization', type=str,
                        help='normalization', action='store', default="l2")
    parser.add_argument('-lr', dest='learning_rate', type=float,
                        help='learning rate', action='store', default=1e-3)

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)
