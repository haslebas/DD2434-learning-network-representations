# Network representation learning with Line algorithm
# Author: Sebastian Haslebacher 2021-12-22

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random
import argparse
import pickle

def sig(x):
    return (1 / (1 + np.exp(-x)))

def line_first_order(G, epochs, K, d):
    """
    G: networkx graph
    epochs: number of times each edge is considered
    K: number of negative edges for every positive edge
    d: dimensionality of embeddings
    """
    E = {}
    for node in G.nodes:
        E[node] = np.random.rand(d) - 0.5
    
    # asynchronous SGD to learn embeddings
    edges = [e for e in G.edges]
    random.shuffle(edges)
    for e in range(epochs):
        t = 0
        for u, v in edges:
            neg_nbrs = [1, 2, 3, 4, 5] # neg_nbrs = random.sample(G.nodes, K) # TODO: nodes should be sampled according to their degree d**(3 / 4)

            # update according to the (positive) edge
            del_u = E[v] * (1 - sig(np.dot(E[v], E[u])))
            del_v = E[u] * (1 - sig(np.dot(E[v], E[u])))
            
            # updates for negative edges
            for nbr in neg_nbrs:
                del_u -= E[nbr] * (1 - sig(-np.dot(E[nbr], E[u]))) / K # TODO: should we really divide by K here?
                del_v -= E[nbr] * (1 - sig(-np.dot(E[v], E[nbr]))) / K # TODO: should we really divide by K here?

            E[u] += del_u
            E[v] += del_v    

            if ((t + 1) % 1000 == 0):
                print('Completed %d out of %d edges in epoch %d'%(t + 1, len(G.edges), e))  
            t += 1  
        print('Completed epoch %d'%(e))
    return E
    
def line_second_order():
    pass

def main(args):
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle(args.graph_path)
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges)))
    
    print('Start to learn Line-1 embeddings')
    E = line_first_order(G, args.epochs, args.K, args.d)
    
    with open(args.output_path, 'wb') as handle:
        pickle.dump(E, handle)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='learn network representations with Line')

    # command-line arguments
    parser.add_argument('graph_path', type=str, 
        help='path to pickle-file of networkx graph', action='store')
    parser.add_argument('output_path', type=str, 
        help='path to output file where represenations are stored', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)
    parser.add_argument('-e', dest='epochs', type=int, 
        help='number of epochs', action='store', default=1)
    parser.add_argument('-K', dest='K', type=int, 
        help='number of negative samples for every edge', action='store', default=5)
    parser.add_argument('-d', dest='d', type=int, 
        help='dimensionality of embeddings', action='store', default=2)

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)