# This script can be used to plot 2d embeddings and the node labels.
# Note that usually 128 dimensional embeddings are used and hence 
# nothing interesting should be expected from these plots.
# Author: Sebastian Haslebacher 2021-12-24

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import csv
import argparse
import pickle
import matplotlib.pyplot as plt

def main(args):
    with open(args.embeddings_path, 'rb') as file:
        emb = pickle.load(file)

    groups = {}
    with open(args.labels_path, 'r') as file:
        datareader = csv.reader(file)
        for row in datareader:
            groups[int(row[0])] = int(row[1])
    print(len(groups))    

    c = [value for _, value in sorted(groups.items())]
    x = [emb[node][0] for node in sorted(groups.keys())]
    y = [emb[node][1] for node in sorted(groups.keys())]

    plt.scatter(x, y, c=c, s=3)
    plt.show()        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='plot 2d-embeddings along with node labels')

    # command-line arguments
    parser.add_argument('embeddings_path', type=str, 
        help='path to pickle-file containing embeddings', action='store')
    parser.add_argument('labels_path', type=str, 
        help='path to csv-file containing node labels', action='store')

    args = parser.parse_args()
    main(args)