# Sebastian Haslebacher 2021-12-23

# Epinions
python3 main.py ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle ../embeddings/epinions_line_128d_T100_lp.pkl -T 100000000

# BlogCatalog
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_line_128d_T100.pkl -T 100000000
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_line_128d_T100_lp.pkl -T 100000000

# Youtube
python3 main.py ../data/Youtube-dataset/youtube_graph.gpickle ../embeddings/youtube_line_128d_T100.pkl -T 100000000
python3 main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_line_128d_T100_lp.pkl -T 100000000

# Flickr
python3 main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_line_128d_T100.pkl -T 100000000
python3 main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flickr_line_128d_T100_lp.pkl -T 100000000

# Twitter
python3 main.py ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle ../embeddings/twitter_line_128d_T100_lp.pkl -T 100000000

# big Cora
python3 main.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../embeddings/cora_line_128d_T100_lp.pkl -T 100000000
python3 main.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../embeddings/cora_line_128d_T100.pkl -T 100000000

# small Cora
python3 main.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle ../embeddings/small_cora_line_128d_T100_lp.pkl -T 100000000
python3 main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../embeddings/small_cora_line_128d_T100.pkl -T 100000000

# AstroPh
python3 main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_line_128d_T100_lp.pkl -T 100000000

# PPI
python3 main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_line_128d_T100_lp.pkl -T 100000000

# Pubmed
python3 main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_line_128d_T100_lp.pkl -T 100000000
python3 main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_line_128d_T100.pkl -T 100000000

python3 main.py ../data/pubmed-dataset/pubmed_graph_undir_lp.gpickle ../embeddings/pubmed_undir_line_128d_T100_lp.pkl -T 100000000
python3 main.py ../data/pubmed-dataset/pubmed_graph_undir.gpickle ../embeddings/pubmed_undir_line_128d_T100.pkl -T 100000000

# Reddit
python3 main.py ../data/reddit/reddit_graph_lp.gpickle ../embeddings/reddit_line_128d_T100_lp.pkl -T 100000000
python3 main.py ../data/reddit/reddit_graph.gpickle ../embeddings/reddit_line_128d_T100.pkl -T 100000000

# DBLP-Ci
python3 main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_line_128d_T100_lp.pkl -T 100000000

# DBLP-Au
python3 main.py ../data/DBLP-Au-dataset/dblp-au_graph_dir_lp.gpickle ../embeddings/dblp-au_line_128d_T100_lp.pkl -T 100000000