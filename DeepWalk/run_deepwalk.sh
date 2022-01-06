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

  # Run DeepWalk on Reddit
 python main.py ../data/reddit/reddit_graph.gpickle ../embeddings/reddit_nc_deepwalk_128d

# Run DeepWalk on Flickr
python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_deepwalk_128d

# NC DeepWalk on Youtube 
python main.py ../data/YouTube-dataset/youtube_graph.gpickle ../embeddings/youtube_deepwalk_128d -n_walks 10 -t 20 -w 5


# Make embeddings for Link Prediction (LP) task
# UNDIRECTED: 

# LP DeepWalk for BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_lp_deepwalk_128d

# LP DeepWalk on Youtube
python main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_lp_deepwalk_128d -n_walks 10 -t 20 -w 5

# LP DeepWalk on Reddit
python main.py ../data/reddit/reddit_graph_lp.gpickle ../embeddings/reddit_lp_deepwalk_128d -n_walks 10 -t 20 -w 5

# LP DeepWalk on DBLP-Au
python main.py ../data/DBLP-Au-dataset/deblp-au_graph_lp.gpickle ../embeddings/dblp-au_lp_deepwalk_128d -n_walks 10 -t 20 -w 5

# LP DeepWalk on Flickr
python main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flicker_lp_deepwalk_128d -n_walks 10 -t 20 -w 5

# LP DeepWalk on PPI
python main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_lp_deepwalk_128d

# LP DeepWalk on Astro-Ph
python main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_lp_deepwalk_128d


# DIRECTED:
# LP DeepWalk for Cora (small)
python main.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle ../embeddings/cora_small_lp_deepwalk_128d 

# LP DeepWalk for Cora (big)
python main.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../embeddings/cora_big_lp_deepwalk_128d 

# LP DeepWalk for Twitter
python main.py ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle ../embeddings/twitter_dir_lp_deepwalk_128d 

# LP DeepWalk for DBLP-Ci
python main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_lp_deepwalk_128d

# LP DeepWalk for PubMed
python main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_dir_lp_deepwalk_128d 

# LP DeepWalk for Epinion
python main.py ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle ../embeddings/epinions_dir_lp_deepwalk_128d 
