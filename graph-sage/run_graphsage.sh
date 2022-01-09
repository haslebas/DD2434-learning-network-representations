# Luca Marini

# Epinion
python3 main.py -output_path="../embeddings/epinion_graphsage_lp.pkl" -dataset="epinion" -task="lp"

# BlogCatalog
python3 main.py -output_path="../embeddings/blog_catalog_graphsage.pkl" -dataset="blog_catalog" -task="nc"
python3 main.py -output_path="../embeddings/blog_catalog_graphsage_lp.pkl" -dataset="blog_catalog" -task="lp"

# Youtube
python3 main.py -output_path="../embeddings/youtube_graphsage.pkl" -dataset="youtube" -task="nc"
python3 main.py -output_path="../embeddings/youtube_graphsage_lp.pkl" -dataset="youtube" -task="lp"

# Flickr
python3 main.py -output_path="../embeddings/flickr_graphsage.pkl" -dataset="youtube" -task="nc"
python3 main.py -output_path="../embeddings/flickr_graphsage_lp.pkl" -dataset="youtube" -task="lp"

# Twitter
python3 main.py -output_path="../embeddings/twitter_graphsage_lp.pkl" -dataset="twitter" -task="lp"

# big Cora
python3 main.py -output_path="../embeddings/big_cora_graphsage.pkl" -dataset="big_cora" -task="nc"
python3 main.py -output_path="../embeddings/big_cora_graphsage_lp.pkl" -dataset="big_cora" -task="lp"

# small Cora
python3 main.py -output_path="../embeddings/small_cora_graphsage.pkl" -dataset="small_cora" -task="nc" -lbls_ids
python3 main.py -output_path="../embeddings/small_cora_graphsage_lp.pkl" -dataset="small_cora" -task="lp" -lbls_ids

# AstroPh
python3 main.py -output_path="../embeddings/astroph_graphsage_lp.pkl" -dataset="astro-ph" -task="lp"

# PPI
python3 main.py -output_path="../embeddings/ppi_graphsage_lp.pkl" -dataset="ppi" -task="lp"

# Pubmed
python3 main.py -output_path="../embeddings/pubmed_graphsage.pkl" -dataset="pubmed" -task="nc"
python3 main.py -output_path="../embeddings/pubmed_graphsage_lp.pkl" -dataset="pubmed" -task="lp"

# Reddit
python3 main.py -output_path="../embeddings/reddit_graphsage.pkl" -dataset="reddit" -task="nc"
python3 main.py -output_path="../embeddings/reddit_graphsage_lp.pkl" -dataset="reddit" -task="lp"

# DBLP-Ci
python3 main.py -output_path="../embeddings/dblp_ci_graphsage_lp.pkl" -dataset="dblp-ci" -task="lp"

# DBLP-Au
python3 main.py -output_path="../embeddings/dblp_au_graphsage_lp.pkl" -dataset="dblp-au" -task="lp"