def add_citations(

answer,

documents

):

    refs=[]

    for d in documents:

        refs.append(

            (

                d["book"],

                d["chapter"]

            )

        )

    refs=list(

        set(

            refs

        )

    )

    answer += "\n\nReferences:\n"

    for b,c in refs:

        answer += (

            f"- {b}"

        )

        answer += (

            f" Chapter {c}\n"

        )

    return answer