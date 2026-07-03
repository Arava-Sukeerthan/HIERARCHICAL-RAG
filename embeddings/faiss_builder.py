import pickle
import numpy as np
import faiss

vectors=pickle.load(

open(

"chunk_vectors.pkl",

"rb"

)

)

vectors=np.array(

vectors

)

dim=vectors.shape[1]

index=faiss.IndexFlatIP(

dim

)

index.add(

vectors

)

faiss.write_index(

index,

"chunk.index"

)

print()

print(

index.ntotal

)