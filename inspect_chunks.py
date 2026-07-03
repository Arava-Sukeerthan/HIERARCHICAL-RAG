import pickle

hierarchy = pickle.load(

open(

"processed/hierarchy.pkl",

"rb"

)

)

print(len(hierarchy))

print()

print(hierarchy[0])

print()

print(hierarchy[100])

print()

print(hierarchy[500])

import pickle

hierarchy = pickle.load(

open(

"processed/hierarchy.pkl",

"rb"

)

)

sections = set()

chapters = set()

for h in hierarchy:

    sections.add(

        (

            h["book"],

            h["chapter"],

            h["section"]

        )

    )

    chapters.add(

        (

            h["book"],

            h["chapter"]

        )

    )

print(

"Sections",

len(sections)

)

print(

"Chapters",

len(chapters)

)

import pickle
import re

docs = pickle.load(

open(

"processed/raw_documents.pkl",

"rb"

)

)

lengths=[]

for doc in docs:

    chapters = re.split(

        r'Chapter\s+\d+',

        doc["text"]

    )

    for c in chapters:

        lengths.append(

            len(c)

        )

print(

"Average chapter length",

sum(lengths)/len(lengths)

)

print(

"Max",

max(lengths)

)

print(

"Min",

min(lengths)

)

import pickle

hierarchy = pickle.load(

open(

"processed/hierarchy.pkl",

"rb"

)

)

count={}

for h in hierarchy:

    key=(

        h["book"],

        h["chapter"]

    )

    count[key]=count.get(

        key,

        0

    )+1

vals=list(

count.values()

)

print(

"Average sections/chapter",

sum(vals)/len(vals)

)

print(

"Max",

max(vals)

)

print(

"Min",

min(vals)

)