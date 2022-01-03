# To run the NetMF approximation implementation

# Run approximation
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/blogcat_netmf_approx_embedding_128d.pkl --large

# Run exact
# python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../data/BlogCatalog-dataset/blogcat_netmf_exact_embedding_128d.npy