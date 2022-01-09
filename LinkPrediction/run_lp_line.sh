# UNDIRECTED:

# Line BlogCatalog embeddings 
python3 link_prediction.py ../embeddings/blog_catalog_line_128d_T100_lp.pkl ../data/BlogCatalog-dataset/blog_catalog_graph_lp_test_edges.pkl --dataset_name BlogCatalog

# LP Line on Youtube
python3 link_prediction.py ../embeddings/youtube_line_128d_T100_lp.pkl ../data/Youtube-dataset/youtube_graph_lp_test_edges.pkl --dataset_name Youtube

# LP Line on Reddit
python3 link_prediction.py ../embeddings/reddit_line_128d_T100_lp.pkl ../data/reddit/reddit_graph_lp_test_edges.pkl --dataset_name Reddit

# LP Line on DBLP-Au
python3 link_prediction.py ../embeddings/dblp-au_line_128d_T100_lp.pkl ../data/DBLP-Au-dataset/dblp-au_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Au

# LP Line on Flickr
python3 link_prediction.py ../embeddings/flickr_line_128d_T100_lp.pkl ../data/Flickr-dataset/flickr_graph_lp_test_edges.pkl --dataset_name Flickr

# LP Line on PPI
python3 link_prediction.py ../embeddings/ppi_line_128d_T100_lp.pkl ../data/PPI-dataset/ppi_graph_lp_test_edges.pkl --dataset_name PPI

# LP Line on Astro-Ph
python3 link_prediction.py ../embeddings/astro_line_128d_T100_lp.pkl ../data/AstroPh-dataset/astro_graph_lp_test_edges.pkl --dataset_name AstroPh

# LP Line for PubMed
python3 link_prediction.py ../embeddings/pubmed_undir_line_128d_T100_lp.pkl ../data/pubmed-dataset/pubmed_graph_undir_lp_test_edges.pkl --dataset_name Pubmed


# DIRECTED

# Line Cora (small) embeddings 
python3 link_prediction.py ../embeddings/small_cora_line_128d_T100_lp.pkl ../data/Cora-dataset/cora_graph_dir_lp_test_edges.pkl --dataset_name Cora-small

# Line Cora (big) embeddings 
python3 link_prediction.py ../embeddings/cora_line_128d_T100_lp.pkl ../data/subelj_cora/cora_big_graph_dir_lp_test_edges.pkl --dataset_name Cora-big

# LP Line for Twitter
python3 link_prediction.py ../embeddings/twitter_line_128d_T100_lp.pkl ../data/Twitter-dataset/twitter_graph_dir_lp_test_edges.pkl --dataset_name Twitter

# Line DBLP-Ci embeddings 
python3 link_prediction.py ../embeddings/dblp-ci_line_128d_T100_lp.pkl ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp_test_edges.pkl --dataset_name DBLP-Ci

# LP Line for PubMed
python3 link_prediction.py ../embeddings/pubmed_line_128d_T100_lp.pkl ../data/PubMed/pubmed_graph_dir_lp_test_edges.pkl --dataset_name Pubmed

# LP Line for Epinion
python3 link_prediction.py ../embeddings/epinions_line_128d_T100_lp.pkl ../data/Epinions-dataset/epinions_graph_dir_lp_test_edges.pkl --dataset_name Epinions
