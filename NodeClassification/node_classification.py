# This script evaluates the embeddings on a node classification task.
# Author: Sebastian Haslebacher 2021-12-31

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import pickle
import numpy as np
import random
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import cross_val_score

def get_score(X, y, seed, dataset_name):
    model = OneVsRestClassifier(LogisticRegression(random_state=seed))
    micro_scores = cross_val_score(model, X, y, cv=5, scoring='f1_micro')
    macro_scores = cross_val_score(model, X, y, cv=5, scoring='f1_macro')

    print('Dataset: ', dataset_name)
    print('Micro scores are:')
    print(micro_scores)
    print('avg: ', np.average(micro_scores))
    print('Macro scores are:')
    print(macro_scores)
    print('avg: ', np.average(macro_scores))

def main(args):
    with open(args.embeddings_path, 'rb') as file:
        emb = pickle.load(file)

    groups = {}
    with open(args.labels_path, 'r') as file:
        datareader = csv.reader(file)
        for row in datareader:
            key = row[0]
            try:
                key = int(row[0])
            except ValueError:
                pass
            val = int(row[1])
            if key not in groups:
                groups[key] = []
            groups[key].append(val)  
    
    X = []
    list_y = []
    for node in sorted(groups.keys()):
        if node in emb:
            X.append(emb[node])
            list_y.append(groups[node])
    data = list(zip(X, list_y))
    random.shuffle(data)
    X, list_y = zip(*data)
    y = MultiLabelBinarizer().fit_transform(list_y)

    get_score(X, y, args.seed, args.dataset_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='evaluate embeddings on node classification task')

    # command-line arguments
    parser.add_argument('embeddings_path', type=str, 
        help='path to pickle-file containing embeddings', action='store')
    parser.add_argument('labels_path', type=str, 
        help='path to csv-file containing node labels', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)
    parser.add_argument('--dataset_name', dest='dataset_name', type=str, 
        help='fix random seeds', action='store')

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)