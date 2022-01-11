# Author: Manuel Fraile

from functools import reduce
from itertools import combinations_with_replacement

import numpy as np
import pkg_resources
from gensim.models import KeyedVectors
from tqdm import tqdm


class EdgeFeatures:
    def __init__(self, keyed_vectors: KeyedVectors, progress_bar: bool = True, embedder: string = 'average'):
        self.kv = keyed_vectors
        self.progress_bar = progress_bar
        self.embedder = embedder

    def embed(self, edge: tuple) -> np.ndarray:
        if self.embedder.lower() == 'average':
            return (self.kv[edge[0]] + self.kv[edge[1]]) / 2

        elif self.embedder.lower() == 'hadamard':
            return self.kv[edge[0]] * self.kv[edge[1]]

        elif self.embedder.lower() == 'weighted-l1':
            return np.abs(self.kv[edge[0]] - self.kv[edge[1]])

        elif self.embedder.lower() == 'weighted-l2':
            return (self.kv[edge[0]] - self.kv[edge[1]]) ** 2

        else:
            print("ERROR: Invalid embedder.")

    def as_keyed_vectors(self) -> KeyedVectors:
        generate_edges = combinations_with_replacement(getattr(self.kv, 'index_to_key'), r=2)

        # Generate features
        tokens = []
        features = []
        for e in generate_edges:
            token = str(tuple(sorted(e)))
            tokens.append(token)

            embedding = self._embed(e)
            features.append(embedding)

        # Build KV instance
        edge_kv = KeyedVectors(vector_size=self.kv.vector_size)
        edge_kv.add_vectors(keys=tokens, weights=features)
        return edge_kv
