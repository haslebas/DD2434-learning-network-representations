# Sebastian Haslebacher 2021-12-23

# Epinions
python3 main.py ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle ../embeddings/epinions_line_128d_T50_lp.pkl -T 50

# BlogCatalog
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_line_128d_T50.pkl -T 50
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_line_128d_T50_lp.pkl -T 50

# Youtube
python3 main.py ../data/Youtube-dataset/youtube_graph.gpickle ../embeddings/youtube_line_128d_T50.pkl -T 50
python3 main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_line_128d_T50_lp.pkl -T 50

# Flickr
python3 main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_line_128d_T50.pkl -T 50
python3 main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flickr_line_128d_T50_lp.pkl -T 50

# Twitter
python3 main.py ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle ../embeddings/twitter_line_128d_T50_lp.pkl -T 50

# big Cora
python3 main.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../embeddings/cora_line_128d_T50_lp.pkl -T 50
python3 main.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../embeddings/cora_line_128d_T50.pkl -T 50

# small Cora
python3 main.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle ../embeddings/small_cora_line_128d_T50_lp.pkl -T 50
python3 main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../embeddings/small_cora_line_128d_T50.pkl -T 50

# AstroPh
python3 main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_line_128d_T50_lp.pkl -T 50

# PPI
python3 main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_line_128d_T50_lp.pkl -T 50

# Pubmed
python3 main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_line_128d_T50_lp.pkl -T 50
python3 main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_line_128d_T50.pkl -T 50

# Reddit
python3 main.py ../data/reddit/reddit_graph_lp.gpickle ../embeddings/reddit_line_128d_T50_lp.pkl -T 50
python3 main.py ../data/reddit/reddit_graph.gpickle ../embeddings/reddit_line_128d_T50.pkl -T 50

# DBLP-Ci
python3 main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_line_128d_T50_lp.pkl -T 50

# DBLP-Au
python3 main.py ../data/DBLP-Au-dataset/dblp-au_graph_dir_lp.gpickle ../embeddings/dblp-au_line_128d_T50_lp.pkl -T 50