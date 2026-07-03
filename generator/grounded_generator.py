from generator.prompt_builder import (

build_prompt

)

from generator.answer_generator import (

generate_answer

)

from generator.citation_generator import (

add_citations

)

def grounded_generation(

query,

documents

):

    prompt=build_prompt(

        query,

        documents

    )

    answer=generate_answer(

        prompt

    )

    answer=add_citations(

        answer,

        documents

    )

    return answer