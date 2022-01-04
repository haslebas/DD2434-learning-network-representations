# Sebastian Haslebacher 2021-12-23

# Line embeddings for BlogCatalog
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_line_128d_e50.pkl -e 50
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_line_128d_e50_lp.pkl -e 50

# Line embeddings for Youtube
python3 main.py ../data/Youtube-dataset/youtube_graph.gpickle ../embeddings/youtube_line_128d_e50.pkl -e 50
python3 main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_line_128d_e50_lp.pkl -e 50

# Line embeddings for Flickr
python3 main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_line_128d_e50.pkl -e 50
python3 main.py ../data/Flickr-dataset/flickr_graph_lp.gpickle ../embeddings/flickr_line_128d_e50_lp.pkl -e 50

# Line embeddings for Twitter
python3 main.py ../data/Twitter-dataset/twitter_graph_lp.gpickle ../embeddings/twitter_line_128d_e50_lp.pkl -e 50
