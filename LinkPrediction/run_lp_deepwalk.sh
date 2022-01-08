# Run link prediction on all datasets for DeepWalk embeddings

# UNDIRECTED:

# DeepWalk BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_lp_deepwalk_128d.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# LP DeepWalk on Youtube
python3 link_prediction.py ../embeddings/youtube_lp_deepwalk_128d.pkl ../data/Youtube-dataset/youtube_graph_lp_test_edges.pkl --dataset_name Youtube

# LP DeepWalk on Reddit
python3 link_prediction.py ../embeddings/reddit_lp_deepwalk_128d.pkl ../data/reddit/reddit_graph_lp_test_edges.pkl --dataset_name Reddit

# LP DeepWalk on DBLP-Au
python3 link_prediction.py ../embeddings/dblp-au_lp_deepwalk_128d.pkl ../data/DBLP-Au-dataset/dblp-au_graph_lp_test_edges.pkl --dataset_name DBLP-Au

# LP DeepWalk on Flickr
python3 link_prediction.py ../embeddings/flickr_lp_deepwalk_128d.pkl ../data/Flickr-dataset/flickr_graph_lp_test_edges.pkl --dataset_name Flickr

# LP DeepWalk on PPI
python3 link_prediction.py ../embeddings/ppi_lp_deepwalk_128d.pkl ../data/PPI-dataset/ppi_graph_lp_test_edges.pkl --dataset_name PPI

# LP DeepWalk on Astro-Ph
python3 link_prediction.py ../embeddings/astro_lp_deepwalk_128d.pkl ../data/AstroPh-dataset/astro_graph_lp_test_edges.pkl --dataset_name AstroPh


# DIRECTED

# DeepWalk Cora (small) embeddings 
python3 link_prediction.py ../embeddings/cora_small_lp_deepwalk_128d.pkl ../data/Cora-dataset/cora_graph_dir_lp_test_edges.pkl --dataset_name Cora-small

# DeepWalk Cora (big) embeddings 
python3 link_prediction.py ../embeddings/cora_big_lp_deepwalk_128d.pkl ../data/subelj_cora/cora_big_graph_dir_lp_test_edges.pkl --dataset_name Cora-big

# LP DeepWalk for Twitter
python3 link_prediction.py ../embeddings/twitter_lp_deepwalk_128d.pkl ../data/Twitter-dataset/twitter_graph_dir_lp_test_edges.pkl --dataset_name Twitter

# DeepWalk DBLP-Ci embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_lp_deepwalk_128d.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# LP DeepWalk for PubMed
python3 link_prediction.py ../embeddings/pubmed_dir_lp_deepwalk_128d.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name Pubmed

# LP DeepWalk for Epinion
python3 link_prediction.py ../embeddings/epinions_dir_lp_deepwalk_128d.pkl ../data/Epinions-dataset/epinions_graph_dir_lp_test_edges.pkl --dataset_name Epinions
