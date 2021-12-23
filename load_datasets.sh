# Sebastian Haslebacher 2021-12

# load BlogCatalog dataset and pickle the constructed networkx graph
python3 DeepWalk/graph.py ./data/BlogCatalog-dataset/data/nodes.csv ./data/BlogCatalog-dataset/data/edges.csv ./data/BlogCatalog-dataset/blog_catalog_graph.gpickle

# load Youtube dataset and pickle the constructed networkx graph
python3 DeepWalk/graph.py ./data/Youtube-dataset/data/nodes.csv ./data/Youtube-dataset/data/edges.csv ./data/Youtube-dataset/youtube_graph.gpickle