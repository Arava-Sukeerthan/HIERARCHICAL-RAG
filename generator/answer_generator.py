from generator.model_loader import (

model,

tokenizer

)

def generate_answer(

prompt

):

    inputs=tokenizer(

        prompt,

        return_tensors="pt"

    )

    outputs=model.generate(

        **inputs,

        max_new_tokens=256,

        do_sample=True,

        temperature=0.1

    )

    answer=tokenizer.decode(

        outputs[0],

        skip_special_tokens=True

    )

    return answer