# Sebastian Haslebacher 2021-12-23

# Line embeddings for BlogCatalog
# python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle ../embeddings/blog_catalog_line_128d_e50.pkl -e 50
python3 main.py ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle ../embeddings/blog_catalog_line_128d_e5_lp.pkl -e 5

# Line embeddings for Youtube
# python3 main.py ../data/Youtube-dataset/youtube_graph.gpickle ../embeddings/youtube_line_128d_e50.pkl -e 50
# python3 main.py ../data/Youtube-dataset/youtube_graph_lp.gpickle ../embeddings/youtube_line_128d_e50_lp.pkl -e 50
