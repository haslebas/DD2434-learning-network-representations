# Run node2Vec on BlogCatalog
python ./src/main.py --input ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle --output ./emb/my_model --dataset BlogCatalog

# Run node2Vec on BlogCatalog
#python ./src/mainref.py --input ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle --output ./emb/node2vec_model2

# Run node2Vec on BlogCatalog
#python ./src/mainref.py --input ./graph/karate.edgelist --output ./emb/pruebas

# Run node2Vec on Cora Big
#python ./src/mainref.py --input ../data/subelj_cora/cora_big_graph_dir.gpickle --output ./emb/node2vec_corabig_m2 --directed
#python ./src/mainref.py --input ./graph/CoraBig.edgelist --output ./emb/node2vec_corabig_m2 --directed
