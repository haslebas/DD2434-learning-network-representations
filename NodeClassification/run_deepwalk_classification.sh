# BlogCatalog
python3 node_classification.py ../embeddings/blog_catalog_deepwalk_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# Youtube
python3 node_classification.py ../embeddings/youtube_deepwalk_128d.pkl ../data/YouTube-dataset/data/group-edges.csv

# Flickr
python3 node_classification.py ../embeddings/flickr_deepwalk_128d.pkl ../data/Flickr-dataset/data/group-edges.csv

# big Cora
python3 node_classification.py ../embeddings/cora_big_deepwalk_128d.pkl ../data/subelj_cora/data/group-edges.csv

# small Cora
python3 node_classification.py ../embeddings/cora_deepwalk_128d.pkl ../data/Cora-dataset/data/group-edges.csv

# Pubmed (directed)
python3 node_classification.py ../embeddings/pubmed_dir_deepwalk_128d.pkl ../data/PubMed/data/group-edges.csv

# Pubmed (undirected)
python3 node_classification.py ../embeddings/pubmed_undir_deepwalk_128d.pkl ../data/PubMed/data/group-edges.csv

# Reddit
python3 node_classification.py ../embeddings/reddit_nc_deepwalk_128d.pkl ../data/reddit/data/group-edges.csv
