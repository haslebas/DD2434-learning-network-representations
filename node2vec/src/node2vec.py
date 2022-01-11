# Author: Manuel Fraile

import sys
import numpy as np
import networkx as nx
import random
import gensim
import pkg_resources
from collections import defaultdict
from tqdm import tqdm
from joblib import Parallel, delayed


class Graph:
    def __init__(self, graph: nx.Graph, walk_length: int = 80, num_walks: int = 10, p: float = 1,
                 q: float = 1, weight_key: str = 'weight', workers: int = 1, progress_bar: bool = True,
                 sampling_strategy: dict = None):

        self.graph = graph
        self.walk_length = walk_length
        self.num_walks = num_walks
        self.p = p
        self.q = q
        self.weight_key = weight_key
        self.workers = workers
        self.progress_bar = progress_bar
        self.alt_graph = defaultdict(dict)

        if sampling_strategy is None:
            self.sampling_strategy = {}
        else:
            self.sampling_strategy = sampling_strategy

        self.precompute_transition_probs()
        self.walks = self.simulate_walks()

    def simulate_walks(self) -> list:
        num_walks_lists = np.array_split(range(self.num_walks), self.workers)

        # https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html
        walk_results = Parallel(n_jobs=self.workers)(
            delayed(self.parallel_simulate_walks)(len(num_walks), idx) for idx, num_walks in enumerate(num_walks_lists, 1))

        return [item for sublist in walk_results for item in sublist]

    def precompute_transition_probs(self):
        alt_graph = self.alt_graph

        print("COMPUTING TRANSITION PROBABILITIES")
        nodes_generator = self.graph.nodes()

        for n in nodes_generator:

            if 'probabilities' not in alt_graph[n]:
                alt_graph[n]['probabilities'] = dict()

            for curr_n in self.graph.neighbors(n):

                if 'probabilities' not in alt_graph[curr_n]:
                    alt_graph[curr_n]['probabilities'] = dict()

                unnormalized_weights = list()
                d_neighbors = list()

                for goal in self.graph.neighbors(curr_n):

                    p = self.sampling_strategy[curr_n].get('p', self.p) if curr_n in self.sampling_strategy else self.p
                    q = self.sampling_strategy[curr_n].get('q', self.q) if curr_n in self.sampling_strategy else self.q

                    if goal == n:
                        ss_weight = self.graph[curr_n][goal].get(self.weight_key, 1) * 1 / p
                    elif goal in self.graph[n]:
                        ss_weight = self.graph[curr_n][goal].get(self.weight_key, 1)
                    else:
                        ss_weight = self.graph[curr_n][goal].get(self.weight_key, 1) * 1 / q

                    unnormalized_weights.append(ss_weight)
                    d_neighbors.append(goal)

                unnormalized_weights = np.array(unnormalized_weights)
                alt_graph[curr_n]['probabilities'][n] = unnormalized_weights / unnormalized_weights.sum()

            first_travel_weights = []

            for goal in self.graph.neighbors(n):
                first_travel_weights.append(self.graph[n][goal].get(self.weight_key, 1))

            first_travel_weights = np.array(first_travel_weights)
            alt_graph[n]['neighbors'] = list(self.graph.neighbors(n))
            alt_graph[n]['first_travel_key'] = first_travel_weights / first_travel_weights.sum()

    def parallel_simulate_walks(self, num_walks: int, cpu_num: int) -> list:
        walks = list()

        if self.progress_bar:
            pbar = tqdm(total=num_walks, desc='Generating walks (CPU: {})'.format(cpu_num))

        for n_walk in range(num_walks):

            if self.progress_bar:
                pbar.update(1)

            shuffled_nodes = list(self.alt_graph.keys())
            random.shuffle(shuffled_nodes)

            for init_node in shuffled_nodes:
                walk = [init_node]

                while len(walk) < self.walk_length:
                    walk_options = self.alt_graph[walk[-1]].get('neighbors', None)

                    if not np.any(walk_options):
                        break

                    if len(walk) == 1:
                        probabilities = self.alt_graph[walk[-1]]['first_travel_key']
                        walk_to = random.choices(walk_options, weights=probabilities)[0]
                    else:
                        probabilities = self.alt_graph[walk[-1]]['probabilities'][walk[-2]]
                        walk_to = random.choices(walk_options, weights=probabilities)[0]

                    walk.append(walk_to)

                walk = list(map(str, walk))
                walks.append(walk)

        if self.progress_bar:
            pbar.close()

        return walks
