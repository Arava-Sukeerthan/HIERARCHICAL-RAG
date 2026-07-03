from retrieval.hierarchical_retriever import (

hierarchical_retrieval

)

from generator.grounded_generator import (

grounded_generation

)

query=(

"What are the anatomical "

"divisions of the larynx?"

)

result=hierarchical_retrieval(

query

)

answer = grounded_generation(

query,

result["documents"]

)

print()

print(answer)