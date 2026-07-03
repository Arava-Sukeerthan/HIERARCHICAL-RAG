def build_prompt(

query,

documents

):

    evidence=""

    for i,d in enumerate(

            documents

    ):

        evidence += (

            f"\nEvidence {i+1}:\n"

        )

        evidence += (

            d["text"]

        )

        evidence += "\n"

    prompt=f"""

You are an expert oncology assistant.

Answer ONLY using the provided evidence.

Do not hallucinate.

Question:

{query}

Evidence:

{evidence}

Provide:

1. Answer

2. Clinical Explanation

3. Key Points

"""

    return prompt