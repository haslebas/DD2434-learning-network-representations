# Run link prediction on all datasets for DeepWalk embeddings

# UNDIRECTED:

# BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blogcat_netmf_128d_lp.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# LP on PPI
python3 link_prediction.py ../embeddings/ppi_netmf_128d_lp.pkl ../data/PPI-dataset/ppi_graph_lp_test_edges.pkl --dataset_name PPI

# LP on Astro-Ph
python3 link_prediction.py ../embeddings/astro_netmf_128d_lp.pkl ../data/AstroPh-dataset/astro_graph_lp_test_edges.pkl --dataset_name AstroPh

# LP DeepWalk for PubMed (undir)
python3 link_prediction.py ../embeddings/pubmed_undir_netmf_128d_lp.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name Pubmed

# DIRECTED

# Cora (small) embeddings 
python3 link_prediction.py ../embeddings/small_cora_netmf_128d_lp.pkl ../data/Cora-dataset/cora_graph_dir_lp_test_edges.pkl --dataset_name Cora-small

# Cora (big) embeddings 
python3 link_prediction.py ../embeddings/cora_netmf_128d_lp.pkl ../data/subelj_cora/cora_big_graph_dir_lp_test_edges.pkl --dataset_name Cora-big

# DBLP-Ci embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_netmf_128d_lp.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# LP for PubMed (dir)
python3 link_prediction.py ../embeddings/pubmed_netmf_128d_lp.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name Pubmed-dir

