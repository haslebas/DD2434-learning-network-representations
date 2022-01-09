This project was part of the course DD2434 at KTH in Autumn 2021. 

## Organisation
This project folder is structured as follows:

- Running 'download_datasets.sh' creates a 'data' directory and puts all the datasets in there.
- The folder LoadGraphs contains a shell script to load all the graphs into networkx format and store them using pickle.
- Every algorithm has its own dedicated directory where the code for that algorithm is located along with a shell script to execute the code.
- The embeddings should be stored in an additional 'embeddings'-directory. 
- The evaluation on NC and LP are provided in the respective directories along with shell scripts that run all the evaluations and print the scores to the standard output.
