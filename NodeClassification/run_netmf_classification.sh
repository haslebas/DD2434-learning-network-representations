# BlogCatalog
python3 node_classification.py ../embeddings/blogcat_netmf_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# big Cora
python3 node_classification.py ../embeddings/cora_netmf_128d.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name bigCora

# small Cora
python3 node_classification.py ../embeddings/small_cora_netmf_128d.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name smallCora

# Pubmed (dir)
python3 node_classification.py ../embeddings/pubmed_netmf_128d.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed-dir

# Pubmed (undir)
python3 node_classification.py ../embeddings/pubmed_undir_netmf_128d_lp.pkl ../data/Pubmed-dataset/data/group-edges.csv --dataset_name Pubmed-undir

# Flickr
python3 node_classification.py ../embeddings/flickr_netmf_exact_128d.pkl ../data/Flickr-dataset/data/group-edges.csv --dataset_name Flickr

# Reddit
python3 node_classification.py ../embeddings/reddit_netmf_exact_128d.pkl ../data/reddit/data/group-edges.csv --dataset_name Reddit

