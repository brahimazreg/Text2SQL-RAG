import faiss
import numpy as np


def create_index(vectors):

    dimension = len(vectors[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(
        np.array(
            vectors,
            dtype="float32"
        )
    )

    return index


def search(index, query_vector, k=3):

    distances, ids = index.search(
        np.array(
            [query_vector],
            dtype="float32"
        ),
        k
    )

    return ids[0]