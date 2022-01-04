# Sebastian Haslebacher 2022-01-01

# Line-1 Youtube embeddings 
python3 node_classification.py ../embeddings/youtube_128d_line_1.pkl ../data/YouTube-dataset/data/group-edges.csv

# Line-1 BlogCatalog embeddings 
python3 node_classification.py ../embeddings/blog_catalog_128d_line_1.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# DeepWalk BlogCatalog embeddings
python3 node_classification.py ../data/BlogCatalog-dataset/blog_catalog_deepwalk_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# DeepWalk Cora embeddings
python3 node_classification.py ../data/Cora-dataset/cora_deepwalk_128d.pkl ../data/Cora-dataset/data/group-edges.csv