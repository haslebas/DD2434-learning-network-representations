# BlogCatalog
python3 node_classification.py ../embeddings/blog_catalog_deepwalk_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# Youtube
python3 node_classification.py ../embeddings/youtube_deepwalk_128d_2_5_5.pkl ../data/YouTube-dataset/data/group-edges.csv --dataset_name Youtube

# Flickr
python3 node_classification.py ../embeddings/flickr_deepwalk_128d_10_20_5.pkl ../data/Flickr-dataset/data/group-edges.csv --dataset_name Flickr

# big Cora
python3 node_classification.py ../embeddings/cora_big_deepwalk_128d.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name Cora-big

# small Cora
python3 node_classification.py ../embeddings/cora_deepwalk_128d.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name Cora-small

# Pubmed (directed)
python3 node_classification.py ../embeddings/pubmed_dir_deepwalk_128d.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed-dir

# Pubmed (undirected)
python3 node_classification.py ../embeddings/pubmed_undir_deepwalk_128d.pkl ../data/Pubmed-dataset/data/group-edges.csv --dataset_name Pubmed-undir

# Reddit
python3 node_classification.py ../embeddings/reddit_nc_deepwalk_128d_5_20_5.pkl ../data/reddit/reddit-class_map.csv --dataset_name Reddit
