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
# wget -P ./data http://snap.stanford.edu/graphsage/reddit.zip
# unzip -d data data/reddit.zip

# Twitter (larger than the original dataset)
wget -P ./data http://datasets.syr.edu/uploads/1296759055/Twitter-dataset.zip
unzip -d data data/Twitter-dataset.zip

# Epinion
wget -P ./data https://snap.stanford.edu/data/soc-Epinions1.txt.gz
gunzip ./data/soc-Epinions1.txt.gz

# DBLP (larger than the original dataset)
# wget -P ./data https://originalstatic.aminer.cn/misc/dblp.v13.7z
# unzip -d data data/dblp.v13.7z

# CoCit (also not original dataset)
# wget -P ./data https://academicgraphv2.blob.core.windows.net/oag/linkage/paper_linking_pairs.zip
# unzip -d data data/paper_linking_pairs.zip

# Cora
wget -P ./data http://konect.cc/files/download.tsv.subelj_cora.tar.bz2 
tar -xf ./data/download.tsv.subelj_cora.tar.bz2 -C ./data/

# Pubmed
wget -P ./data https://linqs-data.soe.ucsc.edu/public/Pubmed-Diabetes.tgz
tar -xf ./data/Pubmed-Diabetes.tgz -C ./data/