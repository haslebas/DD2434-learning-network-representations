# To run the NetMF approximation implementation

# Run approximation on BlogCatalog
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blogcat_netmf_approx_embedding_128d.pkl --large
python main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blogcat_netmf_approx_embedding_128d_lp.pkl --large

# Run approximation on Flickr: ~50GB memory
# python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_netmf_approx_embedding_128d.pkl --large

# Run exact
python main.py ../data/Flickr-dataset/flickr_graph.gpickle ../embeddings/flickr_netmf_exact_128d.npy -w 1