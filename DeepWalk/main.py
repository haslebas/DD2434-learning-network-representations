# DeepWalk network representation
# Author: Filippa Kärrfelt 2021-12-20

# Deepwalk associalted code: https://github.com/phanein/deepwalk
# Other simpler DeepWalk implementation: https://github.com/gen3111620/DeepWalk

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random
import argparse
import pickle
from gensim.models import Word2Vec # https://radimrehurek.com/gensim/


def deep_walk(G, w, d, n_walks, t):
    walks = []
    print('making random walks for %d nodes...'%(len(G.nodes)))
    for node in G.nodes:
        if str(node).isnumeric() and int(node) % 1000 == 0:
            print('current node: ', node)
        for i in range(n_walks):
            current_walk = []
            walk_node = node # set the initial walk node
            current_walk.append(str(walk_node))
            for j in range(t):
                neighbors = list(G.edges([walk_node])) # get the neighbors
                if (len(neighbors) > 0): # only take a step if current node has out-edge!
                    picked_edge = random.choice(neighbors)
                    # picked edge is a tuple -- select the new node
                    if picked_edge[0] == walk_node:
                        walk_node = picked_edge[1]
                    else:
                        walk_node = picked_edge[0]
                current_walk.append(str(walk_node))

            walks.append(current_walk)
    print('total number of walks: ', len(walks))
    print('creating embeddings...')
    # create skip-gram embeddings based on existing implementation
    # TODO: this seems to make embeddinbgs for n_nodes / 2 -- why?
    embedding = Word2Vec(walks, vector_size=d, window=w, min_count=0, workers=2, sg=1, hs=1)
    return embedding

def main(args):
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle(args.graph_path)
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges)))
    w2v_embedding = deep_walk(G, args.w, args.d, args.n_walks, args.t)
    w2v_embedding.wv.save_word2vec_format(args.output_path+'.txt')
    # make embedding a dict:
    E = {}
    node_embeddings = open(args.output_path+'.txt', 'r')
    nodes = node_embeddings.readlines()
    num_nodes = nodes[0]
    print('num nodes: ', num_nodes)
    for node in nodes[1:]:
        tok = node.split()
        key = tok[0]
        val = np.array(tok[1:], dtype=float)
        E[key] = val

    with open(args.output_path+'.pkl', 'wb') as handle:
        pickle.dump(E, handle)
    print('Saved DeepWalk embeddings to pkl file')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='learn network representations with Line')

    # command-line arguments
    parser.add_argument('graph_path', type=str, 
        help='path to pickle-file of networkx graph', action='store')
    parser.add_argument('output_path', type=str, 
        help='path to output file where represenations are stored', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)
    parser.add_argument('-d', dest='d', type=int, 
        help='embedding length', action='store', default=128)
    parser.add_argument('-n_walks', dest='n_walks', type=int, 
        help='number of walks for each node', action='store', default=30)
    parser.add_argument('-t', dest='t', type=int, 
        help='random walk length', action='store', default=40)
    parser.add_argument('-w', dest='w', type=int, 
        help='skip-gram window size', action='store', default=10)

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)