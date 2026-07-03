from sentence_transformers import CrossEncoder

print("Loading CrossEncoder...")

reranker = CrossEncoder(

    "cross-encoder/ms-marco-MiniLM-L-12-v2"

)

print("CrossEncoder Loaded")

def rerank(

        query,

        docs,

        top_k=10

):

    if len(docs)==0:

        return []

    pairs=[]

    for doc in docs:

        pairs.append(

            (

                query,

                doc["text"]

            )

        )

    scores = reranker.predict(

        pairs

    )

    for doc,score in zip(

            docs,

            scores

    ):

        doc["score"]=float(

            score

        )

    docs.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    return docs[:top_k]