# Run DeepWalk on BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/blog_catalog_deepwalk_128d

# Run DeepWalk on Cora
python main.py ../data/Cora-dataset/cora_graph_dir.gpickle ../data/Cora-dataset/cora_deepwalk_128d

# BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/embedding.npy
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/blog_catalog_deepwalk_128d
