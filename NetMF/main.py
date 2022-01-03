# Implementation provided by authors: https://github.com/xptree/NetMF
# Library implementation: https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.neighbourhood.netmf.NetMF
# Author: Filippa Kärrfelt

import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import numpy as np
import random
import argparse
import scipy.sparse as sparse
import scipy.sparse.linalg as linalg

def svd(M, d):
    print('SVD for result...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html
    U, S, V = linalg.svds(M, d, return_singular_vectors="u")
    return sparse.diags(np.sqrt(S)).dot(U.T).T

def eigenval_filter(eigen_vals, w):
    # This should be the sum of the powers of each of the eigen values!
    filter_sum = 0
    for i in range(w-1):
        pow = eigen_vals ** (w+1)
        filter_sum += pow
    return filter_sum * 1/w

def deepwalk_approx(eigen_vals, eigen_vecs, D_inv_sqrt_U, D_inv_sqrt, w, vol_G, b):
    print('Computing M...')
    # Spectrum filter - the sum of the powers of the eigen values
    filter = eigenval_filter(eigen_vals, w)
    M_sqrt = sparse.diags(np.sqrt(filter)).dot(D_inv_sqrt_U.T).T
    M = np.dot(M_sqrt, M_sqrt.T) * vol_G/b
    print('M shape (before max): ', M.shape)
    M_prime_log = np.log(np.maximum(M, 1))
    return M_prime_log

def get_laplacian(A, n_nodes):
    print('Computing laplacian...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.laplacian.html
    # L: Laplacian matrix (D-A) where D is the degree matrix and A the adjacency matrix
    # diag: Array of square roots of the vertext degrees sqrt(D)
    L, D_sqrt = sparse.csgraph.laplacian(A, normed=True, return_diag=True)
    # eig_approx = D^{-1/2} A D^{-1/2} approximated by I - L
    eig_approx = sparse.identity(n_nodes) - L
    return eig_approx, D_sqrt

def eigen_decomposition_approx(A, r):
    n_nodes = A.shape[0]
    eig_approx, D_sqrt = get_laplacian(A, n_nodes)
    print('Eigen decomposition...')
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html
    eigen_vals, eigen_vecs = linalg.eigsh(eig_approx, r, which="LA", tol=1e-3, maxiter=300)
    D_inv_sqrt = sparse.diags(D_sqrt ** -1)
    D_inv_sqrt_U = D_inv_sqrt.dot(eigen_vecs)
    return eigen_vals, eigen_vecs, D_inv_sqrt_U, D_inv_sqrt

def net_mf_approx(A, r, w, b, d):
    # eigen decomposition approximation
    eigen_vals, eigen_vecs, D_inv_sqrt_U, D_inv_sqrt = eigen_decomposition_approx(A, r)
    # approximate M
    vol_G = float(A.sum())
    M = deepwalk_approx(eigen_vals, eigen_vecs, D_inv_sqrt_U, D_inv_sqrt, w, vol_G, b)
    # rank-d approximation by SVD
    embedding = svd(M, d)
    return embedding

def net_mf_exact(A, r, w, b, d):
    n_nodes = A.shape[0]
    vol_G = float(A.sum())
    eig_approx, diag = get_laplacian(A, n_nodes)
    print('Computing matrix powers...')
    # S is the sum of the powers
    S = np.zeros(eig_approx.shape)
    P_power = sparse.identity(n_nodes)
    for i in range(w):
        # Compute power for each window size
        P_power = P_power.dot(eig_approx)
        S += P_power
    S = S * vol_G / (b * w)
    invU = sparse.diags(diag ** -1)
    M = S.dot(invU)
    M_prime = np.log(np.maximum(M, 1))
    # rank-d approximation by SVD
    embedding = svd(M_prime, d)
    return embedding

def main(args):
    # https://networkx.org/documentation/stable/reference/readwrite/gpickle.html
    G = nx.read_gpickle(args.graph_path)
    print('Loaded graph with %d nodes and %d edges'%(len(G.nodes), len(G.edges)))
    # Create adjacency matrix
    A = nx.linalg.graphmatrix.adjacency_matrix(G)
    A = np.array(A.todense())
    if args.large_window:
        print('Running approximation for large window size')    
        netmf_embedding = net_mf_approx(A, args.r, args.w, args.b, args.d)
    else:
        print('Running matrix factorization for small window size')
        netmf_embedding = net_mf_exact(A, args.r, args.w, args.b, args.d)

    np.save(args.output_path, netmf_embedding)
    print('Saved NetMF embeddings to file')

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