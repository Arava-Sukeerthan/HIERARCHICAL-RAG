from transformers import AutoTokenizer

from transformers import AutoModelForCausalLM

import torch

MODEL_NAME = (

    "microsoft/Phi-3-mini-4k-instruct"

)

print(

"Loading model..."

)

tokenizer = AutoTokenizer.from_pretrained(

MODEL_NAME

)

model = AutoModelForCausalLM.from_pretrained(

MODEL_NAME,

torch_dtype=torch.float16,

device_map="auto"

)

print(

"model Loaded"

)