# BlogCatalog
python3 node_classification.py ../embeddings/blogcat_netmf_128d.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# big Cora
python3 node_classification.py ../embeddings/cora_netmf_128d.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name bigCora

# small Cora
python3 node_classification.py ../embeddings/small_cora_netmf_128d.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name smallCora

# Pubmed
python3 node_classification.py ../embeddings/pubmed_netmf_128d.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed
