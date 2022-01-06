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

# PubMed
python3 main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_netmf_128d_lp.pkl --large
python3 main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_netmf_128d.pkl --large

# PPI
python3 main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_netmf_128d_lp.pkl --large

# AstroPH
python3 main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_netmf_128d_lp.pkl --large