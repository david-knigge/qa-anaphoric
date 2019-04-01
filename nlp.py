from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from spacy.tokens.doc import get_entity_info


class Parser:

    vocab = set()
    common_pronouns = ["this", "these", "that", "those", "here", "there"]

    def __init__(self) -> None:
        super().__init__()

        with open("data/words.txt") as f:
            line = f.readline()
            while line:
                self.vocab.add(line.rstrip("\n").lower())
                line = f.readline()

        self.model = TfidfVectorizer(ngram_range=(1, 1), vocabulary=self.vocab, min_df=1, stop_words="english", use_idf=False)
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(self.nlp.create_pipe('sentencizer'))

    def transform(self, doc: list):
        return self.model.transform(doc).getrow(0)

    def get_feature_names(self):
        return self.model.get_feature_names()

    def sim(self, v1, v2):
        return cosine_similarity(v1, v2)[0][0]

    def get_anaphora(self, input_doc):
        anaphoric_words = []
        docs = self.nlp(input_doc.lower())
        w_index = 0
        for s_index, sent in enumerate(docs.sents):
            for _, word in enumerate(sent):
                if word.tag_ in ['PRON', 'PRP', 'PRP$'] or (word.pos_ in ["RB", "ADV"] and word.text in self.common_pronouns):
                    anaphoric_words.append([word.text, self.transform([sent.text]), w_index])
                w_index += 1
        return anaphoric_words

    def get_entities(self, input_sentence):
        entities = []
        doc = self.nlp(input_sentence)
        for entity in doc.ents:
            entities.append((entity.text, entity.label_, get_entity_info(entity)))
        return entities
