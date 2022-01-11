# Author: Manuel Fraile

#############################################
#            NODE CLASSIFICATION            #
#############################################

# Run node2vec on BlogCatalog (undirected)
python3 ../NodeClassification/node_classification.py ./emb/NodeClassification/blogcatalog_node2vec_32d_20w.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# Run node2vec on PubMed (directed)
python3 ../NodeClassification/node_classification.py ./emb/LPdir/pubmed_node2vec_32d_20w.pkl ../data/PubMed/data/group-edges.csv --dataset_name PubMed

# Run node2vec on PubMed (undirected)
python3 ../NodeClassification/node_classification.py ./emb/NodeClassification/pubmed_und_node2vec_32d_20w.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed

# Run node2vec Cora Small (directed)
python3 ../NodeClassification/node_classification.py ./emb/NodeClassification/corasmall_node2vec_32d_20w.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name Corasmall

# Run node2vec Cora Big (directed)
python3 ../NodeClassification/node_classification.py ./emb/NodeClassification/corabig_node2vec_32d_20w.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name Corabig

# Run node2vec Reddit (directed)


# Run node2vec Flickr (undirected)


# Run node2vec Youtube (undirected)

