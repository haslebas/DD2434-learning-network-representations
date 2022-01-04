# Sebastian Haslebacher 2021-12

# load BlogCatalog dataset and pickle the constructed networkx graph
python3 graph.py ./data/BlogCatalog-dataset/data/nodes.csv ./data/BlogCatalog-dataset/data/edges.csv ./data/BlogCatalog-dataset/blog_catalog_graph.gpickle
python3 graph.py ./data/BlogCatalog-dataset/data/nodes.csv ./data/BlogCatalog-dataset/data/edges.csv ./data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle -l

# load Youtube dataset and pickle the constructed networkx graph
python3 graph.py ./data/Youtube-dataset/data/nodes.csv ./data/Youtube-dataset/data/edges.csv ./data/Youtube-dataset/youtube_graph.gpickle
python3 graph.py ./data/Youtube-dataset/data/nodes.csv ./data/Youtube-dataset/data/edges.csv ./data/Youtube-dataset/youtube_graph_lp.gpickle -l

# load Flickr dataset and pickle the constructed networkx graph
python3 graph.py ./data/Flickr-dataset/data/nodes.csv ./data/Flickr-dataset/data/edges.csv ./data/Flickr-dataset/flickr_graph.gpickle
python3 graph.py ./data/Flickr-dataset/data/nodes.csv ./data/Flickr-dataset/data/edges.csv ./data/Flickr-dataset/flickr_graph_lp.gpickle -l
