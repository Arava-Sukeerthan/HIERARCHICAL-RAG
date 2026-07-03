import sys
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from retrieval.hierarchical_retriever import hierarchical_retrieval

q="What are the subsites of the larynx?"

res=hierarchical_retrieval(

q

)

print()

print("FINAL DOCS")

print()

for d in res["documents"]:

    print()

    print(

        d["score"]

    )

    print()

    print(

        d["text"][:600]

    )

    print()

    print(

        "-"*60

    )