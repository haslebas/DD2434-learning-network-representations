# To run the NetMF approximation implementation

# Run approximation
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/netmf_approx_embedding.npy --large

# Run exact
# python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/netmf_embedding.npy