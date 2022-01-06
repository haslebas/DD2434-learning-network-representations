# Run link prediction on all datasets for DeepWalk embeddings

# DeepWalk BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_lp_deepwalk_128d.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# DeepWalk Cora (small) embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_lp_deepwalk_128d.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# DeepWalk Cora (big) embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_lp_deepwalk_128d.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# DeepWalk DBLP-Ci embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_lp_deepwalk_128d.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci
