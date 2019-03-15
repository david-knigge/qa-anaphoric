import nltk

# Run once
# nltk.download()

# List with all possible tags
# print(nltk.help.upenn_tagset())

commonPronouns = ["this","these","that","those","here","there"]

def getAnaphoricWords(inputSentence):
    '''
    Returns a list anaphoric words found in the sentence
    '''
    anaphoricWords = []
    tokens = nltk.word_tokenize(inputSentence)
    tagged = nltk.pos_tag(tokens)
    for word, tag in tagged:
        # print(word, tag)
        if 'PRP' in tag:
            anaphoricWords.append(word)
        elif tag == "RB" and word in commonPronouns:
            anaphoricWords.append(word)
    return anaphoricWords

inputSentence = "Who lives there?"
print(getAnaphoricWords(inputSentence))

