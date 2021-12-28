# author: Luca Marini
# inspired by https://github.com/stellargraph/stellargraph

import argparse
import random
from stellargraph.mapper import GraphSAGELinkGenerator
from stellargraph.layer import GraphSAGE, link_classification
from stellargraph.data import UnsupervisedSampler
from sklearn.model_selection import train_test_split

from tensorflow import keras
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from stellargraph.mapper import GraphSAGENodeGenerator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import *


def main(args):
    cora_dataset, G, node_subjects, nodes = get_cora()

    unsupervised_samples = UnsupervisedSampler(
        G, nodes=nodes, length=args.length, number_of_walks=args.number_of_walks
    )

    generator = GraphSAGELinkGenerator(G, args.batch_size, args.num_samples)
    train_gen = generator.flow(unsupervised_samples)

    graphsage = GraphSAGE(
        layer_sizes=args.layer_sizes, generator=generator, bias=True, dropout=args.dropout, normalize=args.normalization
    )

    # Build the model and expose input and output sockets of graphsage, for node pair inputs:
    x_inp, x_out = graphsage.in_out_tensors()

    prediction = link_classification(
        output_dim=1, output_act="sigmoid", edge_embedding_method="ip"
    )(x_out)

    model = keras.Model(inputs=x_inp, outputs=prediction)

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=args.learning_rate),
        loss=keras.losses.binary_crossentropy,
        metrics=[keras.metrics.binary_accuracy],
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

    node_ids = node_subjects.index
    node_gen = GraphSAGENodeGenerator(G, args.batch_size, args.num_samples).flow(node_ids)

    node_embeddings = embedding_model.predict(node_gen, workers=4, verbose=1)

    node_subject = node_subjects.astype("category").cat.codes





    #'''
    X = node_embeddings
    if X.shape[1] > 2:
        transform = TSNE  # PCA

        trans = transform(n_components=2)
        emb_transformed = pd.DataFrame(trans.fit_transform(X), index=node_ids)
        emb_transformed["label"] = node_subject
    else:
        emb_transformed = pd.DataFrame(X, index=node_ids)
        emb_transformed = emb_transformed.rename(columns={"0": 0, "1": 1})
        emb_transformed["label"] = node_subject
    
    alpha = 0.7

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(
        emb_transformed[0],
        emb_transformed[1],
        c=emb_transformed["label"].astype("category"),
        cmap="jet",
        alpha=alpha,
    )
    ax.set(aspect="equal", xlabel="$X_1$", ylabel="$X_2$")
    plt.title(
        "{} visualization of GraphSAGE embeddings for cora dataset".format(transform.__name__)
    )
    plt.show()
    #'''







    '''
    # X will hold the 50 input features (node embeddings)
    X = node_embeddings
    # y holds the corresponding target values
    y = np.array(node_subject)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.05, test_size=None, stratify=y
    )

    clf = LogisticRegression(verbose=0, solver="lbfgs", multi_class="auto")
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy_score(y_test, y_pred)

    print(pd.Series(y_pred).value_counts())

    print(pd.Series(y).value_counts())
    '''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='graphsage - generation of node embeddings')

    # command-line arguments
    parser.add_argument('--seed', dest='seed', type=int,
                        help='fix random seeds', action='store', default=1)
    parser.add_argument('-e', dest='epochs', type=int,
                        help='number of epochs', action='store', default=4)
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
