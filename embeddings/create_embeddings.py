import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading chunks...")

chunks = pickle.load(

    open(

        "processed/chunks.pkl",

        "rb"

    )

)

texts = [

    c["text"]

    for c in chunks

]

print(

    len(texts),

    "chunks"

)

model = SentenceTransformer(

    "pritamdeka/S-PubMedBert-MS-MARCO"

)

print()

print(

"Encoding..."

)

vectors = model.encode(

    texts,

    batch_size=16,

    show_progress_bar=True,

    normalize_embeddings=True

)

vectors=np.array(

vectors

)

pickle.dump(

vectors,

open(

"chunk_vectors.pkl",

"wb"

)

)

print()

print(

"Saved chunk_vectors.pkl"

)

print(

vectors.shape

)