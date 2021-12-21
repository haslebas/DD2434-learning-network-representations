# Deepwalk associalted code: https://github.com/phanein/deepwalk
# Other simpler DeepWalk implementation: https://github.com/gen3111620/DeepWalk

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random

def skip_gram(phi, walk, window_size):
    for step in walk:
        for w in window_size:
            # Estimate J(phi)
            a = 1

def deep_walk(G, w, d, n_walks, t):
    num_nodes = G.number_of_nodes()
    phi = np.zeros((num_nodes, d)) # matrix of vertex representations. shape num_nodes x d
    print('phi shape: ', phi.shape)
    for node in G.nodes():
        walks = []
        for i in range(n_walks):
            current_walk = []
            # 
            walk_node = node
            print('walk node: ', walk_node)
            current_walk.append(walk_node)
            for j in range(t):
                neighbors = list(G.neighbors(walk_node)) # get the neighbors
                walk_node = random.choice(neighbors)
                current_walk.append(walk_node)
            current_walk = np.array(current_walk)
            skip_gram(phi, current_walk, w)
            walks.append(current_walk)
            walks = np.array(walks)
        print('first walk: ', walks[0])

def main():
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle('../data/BlogCatalog-dataset/blog_catalog_graph.gpickle')
    w = 3 # window size
    d = 10 # embedding length
    n_walks = 20 # number of walks per vertex
    t = 10 # walk length
    deep_walk(G, w, d, n_walks, t)

if __name__ == "__main__":
    main()