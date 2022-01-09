# BlogCatalog
python3 node_classification.py ../embeddings/blog_catalog_line_128d_T100.pkl ../data/BlogCatalog-dataset/data/group-edges.csv --dataset_name BlogCatalog

# Youtube
python3 node_classification.py ../embeddings/youtube_line_128d_T100.pkl ../data/YouTube-dataset/data/group-edges.csv --dataset_name Youtube

# Flickr
python3 node_classification.py ../embeddings/flickr_line_128d_T100.pkl ../data/Flickr-dataset/data/group-edges.csv --dataset_name Flickr

# big Cora
python3 node_classification.py ../embeddings/cora_line_128d_T100.pkl ../data/subelj_cora/data/group-edges.csv --dataset_name bigCora

# small Cora
python3 node_classification.py ../embeddings/small_cora_line_128d_T100.pkl ../data/Cora-dataset/data/group-edges.csv --dataset_name smallCora

# Pubmed
python3 node_classification.py ../embeddings/pubmed_line_128d_T100.pkl ../data/PubMed/data/group-edges.csv --dataset_name Pubmed
python3 node_classification.py ../embeddings/pubmed_undir_line_128d_T100.pkl ../data/pubmed-dataset/data/group-edges.csv --dataset_name Pubmed

# Reddit
python3 node_classification.py ../embeddings/reddit_line_128d_T100.pkl ../data/reddit/reddit-class_map.csv --dataset_name Reddit
