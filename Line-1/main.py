# Network representation learning with Line algorithm
# Author: Sebastian Haslebacher 2021-12-22

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random
import argparse
import pickle

class Sampler:
    """
    Maintains data-structure for negative sampling.
    """
    def __init__(self, G):
        self.G = G
        self.nodes = []
        for node in G.nodes:
            deg = (int)(np.ceil(np.power(G.degree[node], 3/4)))
            for _ in range(deg):
                self.nodes.append(node)
        random.shuffle(self.nodes)
        self.current = 0

    def draw(self, K):
        samples = []
        for k in range(K):
            if(self.current == len(self.nodes)):
                random.shuffle(self.nodes)
                self.current = 0
            samples.append(self.nodes[self.current])
            self.current += 1
        return samples

def sig(x):
    """
    Sigmoid-function.
    """
    return (1 / (1 + np.exp(-x)))

def line_first_order(G, timesteps, K, d, eps=0.1):
    """
    G: networkx graph
    timesteps: number of optimisation steps
    K: number of negative edges for every positive edge
    d: dimensionality of embeddings
    """
    E = {}
    for node in G.nodes:
        E[node] = np.random.rand(d) - 0.5
    edges = [(e[0], e[1]) for e in G.edges]
    sampler = Sampler(G)
    
    # asynchronous SGD to learn embeddings
    count = 0
    N = timesteps
    while(count < N):
        random.shuffle(edges)
        for u, v in edges:
            neg_nbrs = sampler.draw(K)

            # update according to the (positive) edge
            del_u = E[v] * (1 - sig(np.dot(E[v], E[u])))
            del_v = E[u] * (1 - sig(np.dot(E[v], E[u])))
            
            # updates for negative edges
            for nbr in neg_nbrs:
                del_u -= E[nbr] * (1 - sig(-np.dot(E[nbr], E[u]))) / K
                del_v -= E[nbr] * (1 - sig(-np.dot(E[v], E[nbr]))) / K

            # only update one of the two endpoints
            coin = random.randint(0, 1)
            if(coin):
                E[u] += eps * del_u
            else:
                E[v] += eps * del_v    

            if ((count + 1) % 10000 == 0):
                print('Completed %d out of %d optimisation steps'%(count + 1, N))  
            count += 1
            if count >= N:
                break
    return E

def main(args):
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle(args.graph_path)
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges)))
    
    print('Start to learn Line-1 embeddings')
    E = line_first_order(G, args.timesteps, args.K, args.d)

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
    parser.add_argument('-T', dest='timesteps', type=int, 
        help='number of optimisation steps', action='store', default=1)
    parser.add_argument('-K', dest='K', type=int, 
        help='number of negative samples for every edge', action='store', default=5)
    parser.add_argument('-d', dest='d', type=int, 
        help='dimensionality of embeddings', action='store', default=128)

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)