from retrieval.hierarchical_retriever import hierarchical_retrieval

query = (

"What are the anatomical divisions "

"of the larynx?"

)

result = hierarchical_retrieval(

query

)

print()

print("BOOKS")

for item in result["books"]:

    print(

        item

    )

print()

print("CHAPTERS")

for item in result["chapters"]:

    print(

        item

    )

print()

print("SECTIONS")

for item in result["sections"][:10]:

    print(

        item

    )

print()

print("DOCUMENTS")

for doc in result["documents"]:

    print()

    print(

        doc["book"]

    )

    print()

    print(

        doc["chapter"]

    )

    print()

    print(

        doc["section"]

    )

    print()

    print(

        doc["score"]

    )

    print()

    print(

        doc["text"][:1000]

    )

    print()

    print(

        "-"*60

    )