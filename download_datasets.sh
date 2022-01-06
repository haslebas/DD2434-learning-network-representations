# Sebastian Haslebacher 2021-12

# Create data directory
mkdir data

# BlogCatalog3 (with 10k nodes) 
wget -P ./data http://datasets.syr.edu/uploads/1283153973/BlogCatalog-dataset.zip
unzip -d data data/BlogCatalog-dataset.zip

# BlogCatalog (with 80k nodes)
# wget http://datasets.syr.edu/uploads/1252092625/BlogCatalog-dataset.zip
# unzip -d data data/BlogCatalog-dataset.zip

# Flickr
wget -P ./data http://datasets.syr.edu/uploads/1283157931/Flickr-dataset.zip
unzip -d data data/Flickr-dataset.zip

# Youtube
wget -P ./data http://datasets.syr.edu/uploads/1283158247/YouTube-dataset.zip
unzip -d data data/YouTube-dataset.zip

# Reddit
wget -P ./data http://snap.stanford.edu/graphsage/reddit.zip
unzip -d data data/reddit.zip

# Twitter
wget -P ./data http://konect.cc/files/download.tsv.munmun_twitter_social.tar.bz2
mkdir ./data/Twitter-dataset
mkdir ./data/Twitter-dataset/data
tar -xf data/download.tsv.munmun_twitter_social.tar.bz2 -C ./data/Twitter-dataset/data --strip-components 1

# Epinion
wget -P ./data https://snap.stanford.edu/data/soc-Epinions1.txt.gz
gunzip ./data/soc-Epinions1.txt.gz
mkdir ./data/Epinions-dataset
mv ./data/soc-Epinions1.txt ./data/Epinions-dataset/soc-Epinions1.txt

# Cora: Big directed graph version
wget -P ./data http://konect.cc/files/download.tsv.subelj_cora.tar.bz2 
tar -xf ./data/download.tsv.subelj_cora.tar.bz2 -C ./data/

# Pubmed: Directed dataset
wget -P ./data http://zhang18f.myweb.cs.uwindsor.ca/datasets/PubMed.tar.gz
tar -xf ./data/PubMed.tar.gz -C ./data

# DBLP-Ci (citation network) 13k/50k:
wget -P ./data http://statml.com/download/data_7z/misc/dblp-cite.7z
7za e ./data/dblp-cite.7z -o./data/DBLP-Ci-dataset

# # DBLP-Au (Authoprship network) 3M/10M:
wget -P ./data https://snap.stanford.edu/data/bigdata/communities/com-dblp.ungraph.txt.gz
gunzip ./data/com-dblp.ungraph.txt.gz
mkdir ./data/DBLP-Au-dataset
mv ./data/com-dblp.ungraph.txt ./data/DBLP-Au-dataset/com-dblp.ungraph.txt

# PPI (additional dataset)
wget -P ./data https://snap.stanford.edu/biodata/datasets/10000/files/PP-Pathways_ppi.csv.gz
gunzip ./data/PP-Pathways_ppi.csv.gz
mkdir ./data/PPI-dataset
mv ./data/PP-Pathways_ppi.csv ./data/PPI-dataset/PP-Pathways_ppi.csv

# ASTRO-PH
wget -P ./data https://snap.stanford.edu/data/ca-AstroPh.txt.gz
gunzip ./data/ca-AstroPh.txt.gz
mkdir ./data/AstroPh-dataset
mv ./data/ca-AstroPh.txt ./data/AstroPh-dataset/ca-AstroPh.txt

# Twitter (larger than the original dataset)
# wget -P ./data http://datasets.syr.edu/uploads/1296759055/Twitter-dataset.zip
# unzip -d data data/Twitter-dataset.zip

# DBLP (larger than the original dataset)
# wget -P ./data https://originalstatic.aminer.cn/misc/dblp.v13.7z
# 7za e ./data/dblp.v13.7z -o./data

# CoCit (also not original dataset)
# wget -P ./data https://academicgraphv2.blob.core.windows.net/oag/linkage/paper_linking_pairs.zip
# unzip -d data data/paper_linking_pairs.zip
