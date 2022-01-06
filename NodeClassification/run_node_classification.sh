# Sebastian Haslebacher 2022-01-01

# Line-1 Youtube embeddings 
python3 node_classification.py ../embeddings/youtube_line_128d_e50.pkl ../data/YouTube-dataset/data/group-edges.csv

# Line-1 BlogCatalog embeddings 
python3 node_classification.py ../embeddings/blog_catalog_line_128d_e50.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# NetMF BlogCatalog embeddings 
python3 node_classification.py ../embeddings/blogcat_netmf_approx_embedding_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# DeepWalk BlogCatalog embeddings
python3 node_classification.py ../embeddings/blog_catalog_deepwalk_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# DeepWalk Cora (small) embeddings
python3 node_classification.py ../embeddings/cora_deepwalk_128d.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name Cora-small

# DeepWalk Cora (big) embeddings
python3 node_classification.py ../embeddings/cora_big_deepwalk_128d.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name Cora-big

# DeepWalk Pubmed (directed) embeddings
python3 node_classification.py ../embeddings/pubmed_dir_deepwalk_128d.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed-directed

# DeepWalk Pubmed (undirected) embeddings
python3 node_classification.py ../embeddings/pubmed_undir_deepwalk_128d.pkl ../data/Pubmed-dataset/data/group-edges.csv --dataset_name Pubmed-undirected