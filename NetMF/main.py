# Referenced implementations: 
# Implementation provided by authors: https://github.com/xptree/NetMF

# Author: Filippa Kärrfelt

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random
import argparse
import scipy.sparse as sparse
import scipy.sparse.linalg as linalg
import pickle

def svd(M, d):
    print('SVD for result...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html
    U, S, V = linalg.svds(M, d, return_singular_vectors="u")
    return sparse.diags(np.sqrt(S)).dot(U.T).T

def eigenval_filter(eigen_vals, w):
    for i in range(len(eigen_vals)):
        eigen_vals[i] = (1 - np.power(eigen_vals[i], w + 1)) / (1 - eigen_vals[i]) - 1
        eigen_vals[i] = np.sqrt(eigen_vals[i] / w)
    return sparse.diags(eigen_vals)

    # Sum of the powers of the eigen values
    # ev = sparse.diags(eigen_vals)
    # S = ev
    # P_power = ev
    # for i in range(2, w):
    #     # Compute power for each window size
    #     P_power = P_power.dot(ev)
    #     S += P_power
    # return S * 1/w

def deepwalk_approx(eigen_vals, D_inv_sqrt_U, w, vol_G, b):
    print('Computing M...')
    # Spectrum filter - the sum of the powers of the eigen values
    filter = eigenval_filter(eigen_vals, w)
    # take sqrt so that we can take dot prod of term and its transpose..
    D_inv_sqrt_U = D_inv_sqrt_U
    M_sqrt = filter.dot(D_inv_sqrt_U.T).T
    M = M_sqrt.dot(M_sqrt.T) * vol_G/b
    print('M shape (before max): ', M.shape)
    M_prime_log = np.log(np.maximum(M, 1))
    return M_prime_log

def get_laplacian(A, n_nodes):
    print('Computing laplacian...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.laplacian.html
    # L: Laplacian matrix (D-A) where D is the degree matrix and A the adjacency matrix
    # diag: Array of square roots of the vertext degrees sqrt(D)
    L, D_sqrt = sparse.csgraph.laplacian(A, normed=True, return_diag=True)
    # D^{-1/2} A D^{-1/2} calculated by I - L
    D_A_D = sparse.identity(n_nodes) - L
    return D_A_D, D_sqrt

def eigen_decomposition_approx(A, r):
    n_nodes = A.shape[0]
    D_A_D, D_sqrt = get_laplacian(A, n_nodes)
    print('Eigen decomposition...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html
    eigen_vals, eigen_vecs = linalg.eigsh(D_A_D, r, which="LA", tol=1e-3, maxiter=300)
    D_inv_sqrt = sparse.diags(D_sqrt ** -1)
    D_inv_sqrt_U = D_inv_sqrt.dot(eigen_vecs)
    return eigen_vals, D_inv_sqrt_U

def net_mf_approx(A, r, w, b, d):
    # eigen decomposition approximation
    eigen_vals, D_inv_sqrt_U = eigen_decomposition_approx(A, r)
    # approximate M
    vol_G = float(A.sum())
    M = deepwalk_approx(eigen_vals, D_inv_sqrt_U, w, vol_G, b)
    # rank-d approximation by SVD
    embedding = svd(M, d)
    return embedding

def net_mf_exact(A, r, w, b, d):
    n_nodes = A.shape[0]
    vol_G = float(A.sum())
    D_A_D, diag = get_laplacian(A, n_nodes)
    print('Computing matrix powers...')
    # S is the sum of the powers
    S = np.zeros(D_A_D.shape)
    P_power = sparse.identity(n_nodes)
    for i in range(w):
        # Compute power for each window size
        P_power = P_power.dot(D_A_D)
        S += P_power
    S = S * vol_G / (b * w)
    invD = sparse.diags(diag ** -1)
    M = invD.dot(invD.dot(S).T)
    M_prime = np.log(np.maximum(M, 1))
    # rank-d approximation by SVD
    embedding = svd(M_prime, d)
    return embedding

def main(args):
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle(args.graph_path)
    G = G.to_undirected()
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges)))
    # Create adjacency matrix
    A = nx.linalg.graphmatrix.adjacency_matrix(G)
    if args.large_window:
        print('Running approximation for large window size')    
        netmf_embedding = net_mf_approx(A, args.r, args.w, args.b, args.d)
    else:
        print('Running matrix factorization for small window size')
        netmf_embedding = net_mf_exact(A, args.r, args.w, args.b, args.d)

    # np.save(args.output_path, netmf_embedding)
    # make embedding a dict:
    E = {}
    id = 0
    for n in G.nodes():
        E[n] = netmf_embedding[id]
        id += 1
    with open(args.output_path, 'wb') as handle:
        pickle.dump(E, handle)
    print('Saved NetMF embeddings to pkl file')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='learn network representations with Line')

    # command-line arguments
    parser.add_argument('graph_path', type=str, 
        help='path to pickle-file of networkx graph', action='store')
    parser.add_argument('output_path', type=str, 
        help='path to output file where represenations are stored', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seed', action='store', default=1)
    parser.add_argument("-l", "--large", dest='large_window',
        help='True if using approximation for large window size', action="store_true")
    parser.add_argument('-r', dest='r', type=int, 
        help='rank -- number of eigenpairs to approximate eigen decomposition', action='store', default=256)
    parser.add_argument('-w', dest='w', type=int, 
        help='window size', action='store', default=10)
    parser.add_argument('-b', dest='b', type=float, 
        help='negative sampling', action='store', default=1.0)
    parser.add_argument('-d', dest='d', type=int, 
        help='embedding length', action='store', default=128) # in the original implementation the embedding size is 128

    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    main(args)