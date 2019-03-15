import nltk

# Run once
# nltk.download()

# List with all possible tags
# print(nltk.help.upenn_tagset())

def getAnaphoricWords(inputSentence):
    '''
    Returns a list with personal/possesive pronouns and 'there', found in the sentence
    '''
    anaphoricWords = []
    tokens = nltk.word_tokenize(inputSentence)
    tagged = nltk.pos_tag(tokens)
    for word, tag in tagged:
        # print(word, tag)
        if 'PRP' in tag:
            anaphoricWords.append(word)
        elif tag == 'RB' and word == "there":
            anaphoricWords.append(word)
        elif tag == 'IN' and word == "that":
            anaphoricWords.append(word)
    return anaphoricWords

inputSentence = "Is that true?"
print(getAnaphoricWords(inputSentence))

