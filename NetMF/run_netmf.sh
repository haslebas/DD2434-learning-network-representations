# To run the NetMF approximation implementation

# BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blogcat_netmf_128d.pkl --large
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blogcat_netmf_128d_lp.pkl --large

# DBLP-Ci
python3 main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_netmf_128d_lp.pkl --large

# small Cora
python3 main.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle ../embeddings/small_cora_netmf_128d_lp.pkl --large
python3 main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../embeddings/small_cora_netmf_128d.pkl --large

# big Cora
python3 main.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../embeddings/cora_netmf_128d_lp.pkl --large
python3 main.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../embeddings/cora_netmf_128d.pkl --large

# PubMed (directed)
python3 main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_netmf_128d_lp.pkl --large
python3 main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_netmf_128d.pkl --large

# PubMed (undirected)
python3 main.py ../data/Pubmed-dataset/pubmed_graph_undir_lp.gpickle ../embeddings/pubmed_undir_netmf_128d_lp.pkl --large
python3 main.py ../data/PubMed/pubmed_graph_undir.gpickle ../embeddings/pubmed_undir_netmf_128d.pkl --large

# PPI
python3 main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_netmf_128d_lp.pkl --large

# AstroPH
python3 main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_netmf_128d_lp.pkl --large

# RUN EXACT SOLUTION!

# Flickr - exact solution
python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_netmf_exact_128d.pkl -w 1
python main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flickr_netmf_exact_lp_128d.pkl -w 1

# Reddit
python main.py ../data/reddit/reddit_graph.gpickle ../embeddings/reddit_netmf_exact_128d.pkl -w 1
python main.py ../data/reddit/reddit_graph_lp.gpickle ../embeddings/reddit_netmf_exact_lp_128d.pkl -w 1