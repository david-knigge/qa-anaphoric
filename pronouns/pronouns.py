import nltk

# Run once
# nltk.download()

# List with all possible tags
# print(nltk.help.upenn_tagset())

def getPronouns(inputSentence):
    '''
    Returns a list with personal/possesive pronouns and 'there', found in the sentence
    '''
    pronouns = []
    tokens = nltk.word_tokenize(inputSentence)
    tagged = nltk.pos_tag(tokens)
    for word, tag in tagged:
        # print(word, tag)
        if 'PRP' in tag:
            pronouns.append(word)
        elif tag == 'EX':
            pronouns.append(word)
    return pronouns

inputSentence = "Who is his son?"
print(getPronouns(inputSentence))

