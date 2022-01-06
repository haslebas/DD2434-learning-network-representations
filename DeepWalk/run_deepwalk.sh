# Make embeddings to use for Node Classification (NC) task

# NC DeepWalk on BlogCatalog
 python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_deepwalk_128d

# Run DeepWalk on Cora (small)
 python main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../embeddings/cora_deepwalk_128d

 # Run DeepWalk on Cora (big)
 python main.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../embeddings/cora_big_deepwalk_128d

 # Run DeepWalk on Pubmed (directed)
 python main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_dir_deepwalk_128d

 # Run DeepWalk on Pubmed (undirected)
 python main.py ../data/Pubmed-dataset/pubmed_graph_undir.gpickle ../embeddings/pubmed_undir_deepwalk_128d

# Run DeepWalk on Flickr
python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_deepwalk_128d

# NC DeepWalk on Youtube
python main.py ../data/YouTube-dataset/youtube_graph.gpickle ../embeddings/youtube_deepwalk_128d


# Make embeddings for Link Prediction (LP) task

# LP DeepWalk for DBLP-Ci
python main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_lp_deepwalk_128d

# LP DeepWalk for BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_lp_deepwalk_128d
