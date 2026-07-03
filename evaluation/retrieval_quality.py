import sys
import os
import json # Don't forget to import json!

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from retrieval.hierarchical_retriever import hierarchical_retrieval

queries = [
    "Management of laryngeal carcinoma",
    "TNM staging of laryngeal cancer?",
    "Supraglottic carcinoma",
    "Supraglottic carcinoma",
    "Laryngeal cancer prognosis"
]

# 1. Create a list to store all results
all_results = []

for q in queries:
    print("-" * 60)
    print(q)
    print("-" * 60)
    
    # Get the result for the current query
    res = hierarchical_retrieval(q)
    
    # 2. Add the query and result to our list
    all_results.append({
        "query": q,
        "results": res
    })
    
    # Print what you need for debugging
    for doc in res["documents"]:
        print(f"Score: {doc['score']}")
        print(doc["text"][:500])
        print()

# 3. Write the entire collected list to a JSON file
with open("outputs/day2_results.json", "w") as f:
    json.dump(all_results, f, indent=4)

print("Results saved to outputs/day2_results.json")