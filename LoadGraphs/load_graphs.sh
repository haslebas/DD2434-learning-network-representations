# load BlogCatalog dataset and pickle the constructed networkx graph
python3 graph.py ../data/BlogCatalog-dataset/data/nodes.csv ../data/BlogCatalog-dataset/data/edges.csv ../data/BlogCatalog-dataset/blog_catalog_graph.gpickle
python3 graph.py ../data/BlogCatalog-dataset/data/nodes.csv ../data/BlogCatalog-dataset/data/edges.csv ../data/BlogCatalog-dataset/blog_catalog_graph_lp.gpickle -l

# load Youtube dataset and pickle the constructed networkx graph
python3 graph.py ../data/Youtube-dataset/data/nodes.csv ../data/Youtube-dataset/data/edges.csv ../data/Youtube-dataset/youtube_graph.gpickle
python3 graph.py ../data/Youtube-dataset/data/nodes.csv ../data/Youtube-dataset/data/edges.csv ../data/Youtube-dataset/youtube_graph_lp.gpickle -l

# load Flickr dataset and pickle the constructed networkx graph
python3 graph.py ../data/Flickr-dataset/data/nodes.csv ../data/Flickr-dataset/data/edges.csv ../data/Flickr-dataset/flickr_graph.gpickle
python3 graph.py ../data/Flickr-dataset/data/nodes.csv ../data/Flickr-dataset/data/edges.csv ../data/Flickr-dataset/flickr_graph_lp.gpickle -l

# load Twitter dataset and pickle the constructed networkx graph
python3 load_graph_from_edges.py --separator=" " --excl_char="%" ../data/Twitter-dataset/data/out.munmun_twitter_social ../data/Twitter-dataset/twitter_graph_dir_lp.gpickle

# load Epinion dataset and pickle the constructed networkx graph
python3 load_graph_from_edges.py --separator=$'\t' --excl_char="#" ../data/Epinions-dataset/soc-Epinions1.txt ../data/Epinions-dataset/epinions_graph_dir_lp.gpickle -d

# load big Cora dataset and pickle the constructed networkx graph
mkdir ../data/subelj_cora/data/
python3 load_cora_big.py ../data/subelj_cora/cora_big_graph_dir.gpickle ../data/subelj_cora/data/ ../data/subelj_cora/out.subelj_cora_cora Cora --classes_path ../data/subelj_cora/ent.subelj_cora_cora.class.name -c
python3 load_cora_big.py ../data/subelj_cora/cora_big_graph_dir_lp.gpickle ../data/subelj_cora/data/ ../data/subelj_cora/out.subelj_cora_cora Cora --classes_path ../data/subelj_cora/ent.subelj_cora_cora.class.name -l

# load small Cora dataset and pickle the constructed networkx graph
mkdir ../data/Cora-dataset
mkdir ../data/Cora-dataset/data
python3 directed_graph.py ../data/Cora-dataset/cora_graph_dir.gpickle cora ../data/Cora-dataset/data/
python3 directed_graph.py ../data/Cora-dataset/cora_graph_dir_lp.gpickle cora ../data/Cora-dataset/data/ -l

# load directed PubMed dataset and pickle the constructed networkx graph
mkdir ../data/PubMed/data/
python3 load_directed_pubmed.py ../data/PubMed/pubmed_graph_dir.gpickle ../data/PubMed/data/ ../data/PubMed/edges.csv ../data/PubMed/group-edges.csv
python3 load_directed_pubmed.py ../data/PubMed/pubmed_graph_dir_lp.gpickle ../data/PubMed/data/ ../data/PubMed/edges.csv ../data/PubMed/group-edges.csv -l

# load DBLP-Ci dataset and pickle the constructed networkx graph
python3 load_cora_big.py ../data/DBLP-Ci-dataset/dblp-ci_graph_dir_lp.gpickle ../data/DBLP-Ci-dataset/data/ ../data/DBLP-Ci-dataset/dblp-cite.edges DBLP -l

# load DBLP-Au dataset and pickle the constructed networkx graph
python3 load_cora_big.py ../data/DBLP-Au-dataset/dblp-au_graph_lp.gpickle ../data/DBLP-Au-dataset/data/ ../data/DBLP-Au-dataset/com-dblp.ungraph.txt DBLP-AU -l

# load Reddit dataset and pickle the constructed networkx graph
python3 load_from_json.py ../data/reddit/reddit-G.json ../data/reddit/reddit-class_map.json ../data/reddit/reddit_graph.gpickle
python3 load_from_json.py ../data/reddit/reddit-G.json ../data/reddit/reddit-class_map.json ../data/reddit/reddit_graph_lp.gpickle -l

# load PPI dataset and pickle the constructed networkx graph
python3 load_graph_from_edges.py ../data/PPI-dataset/PP-Pathways_ppi.csv ../data/PPI-dataset/ppi_graph_lp.gpickle --separator=',' --excl_char="#"

# load AstroPh dataset and pickle the constructed networkx graph
python3 load_graph_from_edges.py ../data/AstroPh-dataset/ca-AstroPh.txt ../data/AstroPh-dataset/astro_graph_lp.gpickle --separator=$'\t' --excl_char="#"

# load PubMed dataset and pickle the constructed networkx graph
mkdir ../data/pubmed-dataset
mkdir ../data/pubmed-dataset/data
python3 directed_graph.py ../data/pubmed-dataset/pubmed_graph_undir.gpickle pubmed ../data/pubmed-dataset/data/
python3 directed_graph.py ../data/pubmed-dataset/pubmed_graph_undir_lp.gpickle pubmed -l ../data/pubmed-dataset/data/
