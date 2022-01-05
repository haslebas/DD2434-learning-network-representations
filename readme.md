## Organisation
This project folder is structured as follows:

- Running 'download_datasets.sh' creates a 'data' directory and puts all the datasets in there.
- The script 'graph.py' takes paths to a dataset and creates a networkx graph object from that. This object is then pickled to a user-defined location. You can use the 'load_graphs.sh' instead of manually running 'graph.py'.
- So far the script 'load_graphs.sh' creates pickle files for the BlogCatalog and Youtube datasets. They are saved in the corresponding directory in 'data'.
- Every algorithm has its own dedicated directory where the code for that algorithm is located.

## Good to know

- We use networkx to store graphs.
- Many python files use argparse to conveniently take and manage command-line arguments (see e.g. graph.py).