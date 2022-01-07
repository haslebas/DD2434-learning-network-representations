# Scripts to make DeepWalk embeddings for all datasets
# Author: Filippa Kärrfelt 2022-01-06

# Make embeddings to use for Node Classification (NC) task

FILE=../embeddings/blog_catalog_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    # NC DeepWalk on BlogCatalog
    echo "creating $FILE embeddings"
    python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_deepwalk_128d
fi

FILE=../embeddings/cora_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # Run DeepWalk on Cora (small)
    python main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../embeddings/cora_deepwalk_128d
fi

FILE=../embeddings/cora_big_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
     # Run DeepWalk on Cora (big)
    python main.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../embeddings/cora_big_deepwalk_128d
fi

FILE=../embeddings/pubmed_dir_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # Run DeepWalk on Pubmed (directed)
    python main.py ../data/PubMed/pubmed_graph_dir.gpickle ../embeddings/pubmed_dir_deepwalk_128d
fi

FILE=../embeddings/pubmed_undir_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # Run DeepWalk on Pubmed (undirected)
    python main.py ../data/Pubmed-dataset/pubmed_graph_undir.gpickle ../embeddings/pubmed_undir_deepwalk_128d
fi

FILE=../embeddings/reddit_nc_deepwalk_128d_5_20_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # Run DeepWalk on Reddit
    python main.py ../data/reddit/reddit_graph.gpickle ../embeddings/reddit_nc_deepwalk_128d_5_20_5 -n_walks 5 -t 20 -w 5
fi

FILE=../embeddings/flickr_deepwalk_128d_2_5_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # Run DeepWalk on Flickr
    python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_deepwalk_128d_5_20_5 -n_walks 2 -t 5 -w 5
fi

FILE=../embeddings/youtube_deepwalk_128d_2_5_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # NC DeepWalk on Youtube 
    python main.py ../data/YouTube-dataset/youtube_graph.gpickle ../embeddings/youtube_deepwalk_128d_2_5_5 -n_walks 2 -t 5 -w 5
fi

# Make embeddings for Link Prediction (LP) task
# UNDIRECTED: 

FILE=../embeddings/blog_catalog_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for BlogCatalog
    python main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_lp_deepwalk_128d
fi

FILE=../embeddings/youtube_lp_deepwalk_128d_2_5_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on Youtube
    python main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_lp_deepwalk_128d_2_5_5 -n_walks 2 -t 5 -w 5
fi

FILE=../embeddings/reddit_lp_deepwalk_128d_5_20_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on Reddit
    python main.py ../data/reddit/reddit_graph_lp.gpickle ../embeddings/reddit_lp_deepwalk_128d_5_20_5 -n_walks 5 -t 20 -w 5
fi

FILE=../embeddings/dblp-au_lp_deepwalk_128d_2_5_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on DBLP-Au
    python main.py ../data/DBLP-Au-dataset/dblp-au_graph_dir_lp.gpickle ../embeddings/dblp-au_lp_deepwalk_128d_2_5_5 -n_walks 2 -t 5 -w 5
fi

FILE=../embeddings/flickr_lp_deepwalk_128d_5_20_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on Flickr
    python main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flickr_lp_deepwalk_128d_5_20_5 -n_walks 5 -t 20 -w 5
fi

FILE=../embeddings/ppi_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on PPI
    python main.py ../data/PPI-dataset/ppi_graph_lp.gpickle ../embeddings/ppi_lp_deepwalk_128d
fi

FILE=../embeddings/astro_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk on Astro-Ph
    python main.py ../data/AstroPh-dataset/astro_graph_lp.gpickle ../embeddings/astro_lp_deepwalk_128d
fi

# DIRECTED:

FILE=../embeddings/cora_small_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for Cora (small)
    python main.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle ../embeddings/cora_small_lp_deepwalk_128d 
if

FILE=../embeddings/cora_big_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for Cora (big)
    python main.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../embeddings/cora_big_lp_deepwalk_128d 
if

FILE=../embeddings/twitter_dir_lp_deepwalk_128d_5_20_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for Twitter
    python main.py ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle ../embeddings/twitter_dir_lp_deepwalk_128d_5_20_5 -n_walks 5 -t 20 -w 5
fi

FILE=../embeddings/dblp-ci_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for DBLP-Ci
    python main.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../embeddings/dblp-ci_lp_deepwalk_128d
fi 

FILE=../embeddings/pubmed_dir_lp_deepwalk_128d.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for PubMed
    python main.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../embeddings/pubmed_dir_lp_deepwalk_128d 
fi

FILE=../embeddings/epinions_dir_lp_deepwalk_128d_5_20_5.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE embeddings"
    # LP DeepWalk for Epinion
    python main.py ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle ../embeddings/epinions_dir_lp_deepwalk_128d_5_20_5 -n_walks 5 -t 20 -w 5
fi