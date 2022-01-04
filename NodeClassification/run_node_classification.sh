# Sebastian Haslebacher 2022-01-01

# Line-1 Youtube embeddings 
# python3 node_classification.py ../embeddings/youtube_line_128d_e50.pkl ../data/YouTube-dataset/data/group-edges.csv

# Line-1 BlogCatalog embeddings 
# python3 node_classification.py ../embeddings/blog_catalog_line_128d_e50.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# NetMF BlogCatalog embeddings 
python3 node_classification.py ../embeddings/blogcat_netmf_approx_embedding_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv
python3 node_classification.py ../embeddings/blog_catalog_128d_line_1.pkl ../data/BlogCatalog-dataset/data/group-edges.csv

# DeepWalk BlogCatalog embeddings
python3 node_classification.py ../data/BlogCatalog-dataset/blog_catalog_deepwalk_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv
