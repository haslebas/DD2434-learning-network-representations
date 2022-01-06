# This script evaluates the embeddings on a link prediction task.
# Author: Sebastian Haslebacher 2021-01-03.

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import pickle
import numpy as np
import random
from sklearn.metrics import roc_auc_score

def main(args):
    with open(args.embeddings_path, 'rb') as file:
        emb = pickle.load(file)

    with open(args.edges_path, 'rb') as file:
        edges = pickle.load(file)

    y_pred = []
    for edge in edges:
        pred = 1 / (1 + np.exp(- np.dot(emb[edge[0]], emb[edge[1]])))
        y_pred.append(pred)
    
    y_true = [1] * (len(edges) // 2) + [0] * (len(edges) // 2)
    
    print('Dataset: ', args.dataset_name)
    print('ROC-AUC score is:')
    print(roc_auc_score(y_true, y_pred))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='evaluate embeddings on link prediction task')

    # command-line arguments
    parser.add_argument('embeddings_path', type=str, 
        help='path to pickle-file containing embeddings', action='store')
    parser.add_argument('edges_path', type=str, 
        help='path to pickle-file containing test edges', action='store')
    parser.add_argument('--dataset_name', type=str, 
        help='path to pickle-file containing test edges', action='store', default='unknown')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)