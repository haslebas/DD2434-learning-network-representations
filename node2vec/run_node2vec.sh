#############################################
#            NODE CLASSIFICATION            #
#############################################
# Run node2vec on BlogCatalog (undirected) ERROR
#FILE=./emb/NodeClassification/blogcatalog_node2vec_16d_10w.pkl
#if [ -f "$FILE" ]; then
#    echo "$FILE exists."
#else
#    echo "creating $FILE embeddings"
#    python ./src/main.py --input ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle --output ./emb/NodeClassification/blogcatalog_node2vec_16d_10w --dimensions 16 --walklength 10 --dataset BlogCatalog
#fi

# Run node2vec on PubMed (directed)
FILE=./emb/NodeClassification/pubmed_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/PubMed/pubmed_graph_dir.gpickle --output ./emb/NodeClassification/pubmed_node2vec_32d_20w --dataset PubMed-directed
fi

# Run node2vec on PubMed (undirected)
FILE=./emb/NodeClassification/pubmed_und_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/PubMed/pubmed_graph_undir.gpickle --output ./emb/NodeClassification/pubmed_und_node2vec_32d_20w --dataset PubMed-undirected
fi

# Run node2vec Cora Small (directed)
FILE=./emb/NodeClassification/corasmall_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Cora-dataset/cora_graph_dir.gpickle --output ./emb/NodeClassification/corasmall_node2vec_32d_20w --dataset Cora-small
fi

# Run node2vec Cora Big (directed)
FILE=./emb/NodeClassification/corabig_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/subelj_cora/cora_big_graph_dir.gpickle --output ./emb/NodeClassification/corabig_node2vec_32d_20w --dataset Cora-big
fi

# Run node2vec Reddit (directed)
FILE=./emb/NodeClassification/reddit_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/reddit/reddit_graph.gpickle --output ./emb/NodeClassification/reddit_node2vec_32d_20w --dataset Reddit
fi

# Run node2vec Flickr (undirected) RAM OVERLOAD
FILE=./emb/NodeClassification/flickr_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Flickr-dataset/flickr_graph.gpickle --output ./emb/NodeClassification/flickr_node2vec_32d_20w --dataset Flickr
fi

# Run node2vec Youtube (undirected) RAM OVERLOAD
FILE=./emb/NodeClassification/youtube_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Youtube-dataset/youtube_graph.gpickle --output ./emb/NodeClassification/youtube_node2vec_32d_20w --dataset Youtube
fi


##############################################
#         LINK PREDICTION undirected         #
##############################################
# Run node2vec on BlogCatalog (undirected)
FILE=./emb/LPundir/blogcatalog_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle --output ./emb/LPundir/blogcatalog_lp_node2vec_32d_20w --dataset BlogCatalog
fi

# Run node2vec on Youtube (undirected) RAM OVERLOAD
FILE=./emb/LPundir/youtube_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Youtube-dataset/youtube_graph_lp.gpickle --output ./emb/LPundir/youtube_lp_node2vec_32d_20w --dataset Youtube
fi

# Run node2vec on Reddit (undirected)


# Run node2vec on DBLP-Au (undirected) RAM OVERLOAD
FILE=./emb/LPundir/dblpau_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/DBLP-Au-dataset/dblp-au_graph_lp.gpickle --output ./emb/LPundir/dblpau_lp_node2vec_32d_20w --dataset DBLP-Au
fi

# Run node2vec on Flickr (undirected) RAM OVERLOAD
FILE=./emb/LPundir/flickr_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Flickr-dataset/flickr_graph_lp.gpickle --output ./emb/LPundir/flickr_lp_node2vec_32d_20w --dataset Flickr
fi

# Run node2vec on PPI (undirected)
FILE=./emb/LPundir/ppi_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/PPI-dataset/ppi_graph_lp.gpickle --output ./emb/LPundir/ppi_lp_node2vec_32d_20w --dataset PPI
fi

# Run node2vec on Astro-Ph (undirected)
FILE=./emb/LPundir/astroph_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/AstroPh-dataset/astro_graph_lp.gpickle --output ./emb/LPundir/astroph_lp_node2vec_32d_20w --dataset Astro-Ph
fi


# Run node2vec on Pubmed (undirected)
FILE=./emb/NodeClassification/pubmed_und_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/PubMed/pubmed_graph_undir_lp.gpickle --output ./emb/NodeClassification/pubmed_und_lp_node2vec_32d_20w --dataset PubMed-undirected
fi

##############################################
#          LINK PREDICTION directed          #
##############################################

# Run node2vec on Cora Small (directed)
FILE=./emb/LPdir/corasmall_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Cora-dataset/cora_graph_dir_lp.gpickle --output ./emb/LPdir/corasmall_lp_node2vec_32d_20w --dataset Cora-small
fi

# Run node2vec on Cora Big (directed)
FILE=./emb/LPdir/corabig_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/subelj_cora/cora_big_graph_dir_lp.gpickle --output ./emb/LPdir/corabig_lp_node2vec_32d_20w --dataset Cora-big
fi

# Run node2vec on Twitter (directed)
FILE=./emb/LPdir/twitter_lp_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle --output ./emb/LPdir/twitter_lp_node2vec_32d_20w --dataset Twitter
fi

# Run node2vec on DBLP-Ci (directed)
FILE=./emb/NodeClassification/dblpci_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle --output ./emb/NodeClassification/dblpci_node2vec_32d_20w --dataset PubMed-undirected
fi

# Run node2vec on Pubmed (directed)
FILE=./emb/LPdir/pubmed_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/PubMed/pubmed_graph_dir_lp.gpickle --output ./emb/LPdir/pubmed_node2vec_32d_20w --dataset PubMed-directed
fi

# Run node2vec on Epinion (directed)
FILE=./emb/LPdir/epinion_node2vec_32d_20w.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "creating $FILE embeddings"
    python ./src/main.py --input ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle --output ./emb/LPdir/epinion_node2vec_32d_20w --dataset Cora-big
fi
