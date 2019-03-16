import nltk
import spacy

nlp = spacy.load("xx_ent_wiki_sm")

# Run once
# nltk.download()

# List with all possible tags
# print(nltk.help.upenn_tagset())

common_pronouns = ["this","these","that","those","here","there"]


def get_anaphoric_words(input_sentence):
    '''
    Returns a list anaphoric words found in the sentence
    '''
    anaphoric_words = []
    tokens = nltk.word_tokenize(input_sentence)
    tagged = nltk.pos_tag(tokens)
    for word, tag in tagged:
        # print(word, tag)
        if 'PRP' in tag:
            anaphoric_words.append(word)
        elif tag == "RB" and word in common_pronouns:
            anaphoric_words.append(word)
    return anaphoric_words


def get_entities(input_sentence):
    entities = []
    doc = nlp(input_sentence)
    for entity in doc.ents:
        entities.append((entity.text, entity.label_))
    return entities

