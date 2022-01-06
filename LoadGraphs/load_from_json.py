import networkx as nx # https://networkx.org/documentation/stable/tutorial.html
import argparse
import pickle
import json
import csv
from stellargraph.data import EdgeSplitter
from networkx.readwrite import json_graph

def main(args):
    G_data = json.load(open(args.edges_path))
    G = json_graph.node_link_graph(G_data, multigraph=True)
    
    s = EdgeSplitter(G)
    G, E, _ = s.train_test_split(keep_connected=True, seed=args.seed)
    test_edges = []
    for edge in E:
        test_edges.append((edge[0], edge[1]))

    print(test_edges[0])
    with open(args.output_path[:-8] + '_test_edges.pkl', 'wb') as f:
        pickle.dump(test_edges, f)

    nx.write_gpickle(G, args.output_path)

    if not args.lp:
        class_map = json.load(open(args.labels_path))
        with open(args.labels_path[:-5] + '.csv', 'w') as file:
            writer = csv.writer(file)
            for key, value in class_map.items():
                writer.writerow([key, value])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='load data into networkx pickle')

    # command-line arguments
    parser.add_argument('edges_path', type=str,
        help='path to json file containing graph', action='store')
    parser.add_argument('labels_path', type=str,
        help='path to json file containing node labels', action='store')
    parser.add_argument('output_path', type=str,
        help='path to store the networkx pickle', action='store')
    parser.add_argument('--seed', dest='seed', type=int, 
        help='fix random seeds', action='store', default=1)
    parser.add_argument('-l', '--linkprediction', dest='lp', 
        help='add this flag if you want to use the graph for link prediction', action='store_true')

    args = parser.parse_args()
    main(args)