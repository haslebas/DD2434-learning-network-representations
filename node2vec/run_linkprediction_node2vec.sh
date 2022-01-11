# Author: Manuel Fraile

##############################################
#         LINK PREDICTION undirected         #
##############################################

# Run node2vec on BlogCatalog (undirected)
python3 ../LinkPrediction/link_prediction.py ./emb/LPundir/blogcatalog_lp_node2vec_32d_20w.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# Run node2vec on Youtube (undirected)


# Run node2vec on Reddit (undirected)


# Run node2vec on DBLP-Au (undirected)


# Run node2vec on Flickr (undirected)


# Run node2vec on PPI (undirected)
python3 ../LinkPrediction/link_prediction.py ./emb/LPundir/ppi_lp_node2vec_32d_20w.pkl ../data/PPI-dataset/ppi_graph_lp_test_edges.pkl --dataset_name PPI

# Run node2vec on Astro-Ph (undirected)
python3 ../LinkPrediction/link_prediction.py ./emb/LPundir/astroph_lp_node2vec_32d_20w.pkl ../data/AstroPh-dataset/astro_graph_lp_test_edges.pkl --dataset_name AstroPh

# Run node2vec on Pubmed (undirected)
python3 ../LinkPrediction/link_prediction.py ./emb/LPundir/pubmed_und_lp_node2vec_32d_20w.pkl ../data/PubMed/pubmed_graph_undir_lp_test_edges.pkl --dataset_name PubMed-undirected


##############################################
#          LINK PREDICTION directed          #
##############################################

# Run node2vec on Cora Small (directed)
python3 ../LinkPrediction/link_prediction.py ./emb/LPdir/corasmall_lp_node2vec_32d_20w.pkl ../data/Cora-dataset/cora_graph_dir_lp_test_edges.pkl --dataset_name Cora-small

# Run node2vec on Cora Big (directed)
python3 ../LinkPrediction/link_prediction.py ./emb/LPdir/corabig_lp_node2vec_32d_20w.pkl ../data/subelj_cora/cora_big_graph_dir_lp_test_edges.pkl --dataset_name Cora-big

# Run node2vec on Twitter (directed)


# Run node2vec on DBLP-Ci (directed)
python3 ../LinkPrediction/link_prediction.py ./emb/LPdir/dblpci_node2vec_32d_20w.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# Run node2vec on Pubmed (directed)
python3 ../LinkPrediction/link_prediction.py ./emb/LPdir/pubmed_node2vec_32d_20w.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name PubMed-directed

# Run node2vec on Epinion (directed)
