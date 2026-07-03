import pickle

from sentence_transformers import SentenceTransformer

chunks=pickle.load(

open(

"processed/hierarchy.pkl",

"rb"

)

)

model=SentenceTransformer(

"pritamdeka/S-PubMedBert-MS-MARCO"

)

sections={}

for c in chunks:

    key=(

        c["book"],

        c["chapter"],

        c["section"]

    )

    sections.setdefault(

        key,

        []

    ).append(

        c["text"]

    )

section_vectors={}

for key,texts in sections.items():

    merged=" ".join(

        texts[:20]

    )

    section_vectors[key]=model.encode(

        merged,

        normalize_embeddings=True

    )

pickle.dump(

section_vectors,

open(

"section_vectors.pkl",

"wb"

)

)

print()

print(

len(

section_vectors

)

)