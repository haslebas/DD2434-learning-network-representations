# UNDIRECTED:

# Line BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_graphsage_lp.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# LP Line on Youtube
python3 link_prediction.py ../embeddings/youtube_graphsage_lp.pkl ../data/Youtube-dataset/youtube_graph_lp_test_edges.pkl --dataset_name Youtube

# LP Line on Reddit
python3 link_prediction.py ../embeddings/reddit_graphsage_lp.pkl ../data/reddit/reddit_graph_lp_test_edges.pkl --dataset_name Reddit

# LP Line on DBLP-Au
python3 link_prediction.py ../embeddings/dblp_au_graphsage_lp.pkl ../data/DBLP-Au-dataset/dblp-au_graph_lp_test_edges.pkl --dataset_name DBLP-Au

# LP Line on Flickr
python3 link_prediction.py ../embeddings/flickr_graphsage_lp.pkl ../data/Flickr-dataset/flickr_graph_lp_test_edges.pkl --dataset_name Flickr

# LP Line on PPI
python3 link_prediction.py ../embeddings/ppi_graphsage_lp.pkl ../data/PPI-dataset/ppi_graph_lp_test_edges.pkl --dataset_name PPI

# LP Line on Astro-Ph
python3 link_prediction.py ../embeddings/astroph_graphsage_lp.pkl ../data/AstroPh-dataset/astro_graph_lp_test_edges.pkl --dataset_name AstroPh


# DIRECTED

# Line Cora (small) embeddings 
python3 link_prediction.py ../embeddings/small_cora_graphsage_lp.pkl ../data/Cora-dataset/cora_graph_dir_lp_test_edges.pkl --dataset_name Cora-small

# Line Cora (big) embeddings 
python3 link_prediction.py ../embeddings/big_cora_graphsage_lp.pkl ../data/subelj_cora/cora_big_graph_dir_lp_test_edges.pkl --dataset_name Cora-big

# LP Line for Twitter
python3 link_prediction.py ../embeddings/twitter_graphsage_lp.pkl ../data/Twitter-dataset/twitter_graph_dir_lp_test_edges.pkl --dataset_name Twitter

# Line DBLP-Ci embeddings 
python3 link_prediction.py ../embeddings/dblp_ci_graphsage_lp.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# LP Line for PubMed
python3 link_prediction.py ../embeddings/pubmed_graphsage_lp.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name Pubmed

# LP Line for Epinion
python3 link_prediction.py ../embeddings/epinion_graphsage_lp.pkl ../data/Epinions-dataset/epinions_graph_dir_lp_test_edges.pkl --dataset_name Epinions
