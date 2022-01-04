# Sebastian Haslebacher 2022-01-03

# Line-1 BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_line_128d_e50_lp.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl

# Line-1 Youtube embeddings 
python3 link_prediction.py ../embeddings/youtube_line_128d_e50_lp.pkl ../data/Youtube-dataset/youtube_graph_lp_test_edges.pkl

# Line-1 Epinions embeddings 
python3 link_prediction.py ../embeddings/epinions_line_128d_e5_lp.pkl ../data/Epinions-dataset/epinions_graph_lp_test_edges.pkl

# NetMF BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_line_128d_e50_lp.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl
