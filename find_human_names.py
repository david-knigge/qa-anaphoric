import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nameparser.parser import HumanName

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)

text2 = """
People like Marthijn Den Hartog and David Knigge and Laurence Bont and Pepijn Sibbes are all students at the UVA. 
They work on assignments for their Prof. Tom Lentz and the TA Noa."
"""

text = "People like Laurence, Marthijn and David and Pepijn"

#names = get_human_names(text2)
#print(names)
#print("LAST, FIRST")
#for name in names: 
    #print(name)