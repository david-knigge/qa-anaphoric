from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy


class Parser:

    vocab = set()
    common_pronouns = ["this", "these", "that", "those", "here", "there"]

    def __init__(self) -> None:
        super().__init__()

        with open("words.txt") as f:
            line = f.readline()
            while line:
                self.vocab.add(line.rstrip("\n").lower())
                line = f.readline()

        self.model = TfidfVectorizer(ngram_range=(1, 1), vocabulary=self.vocab, min_df=1, stop_words="english", use_idf=False)
        self.nlp = spacy.load("en")
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
        for sent in docs.sents:
            for word in sent:
                if word.pos_ in ['PRON', 'PRP', 'PRP$'] or (word.pos_ in ["RB", "ADV"] and word in self.common_pronouns):
                    anaphoric_words.append([word.text, self.transform([sent.text])])
        return anaphoric_words

    def get_entities(self, input_sentence):
        entities = []
        doc = self.nlp(input_sentence)
        for entity in doc.ents:
            entities.append((entity.text, entity.label_))
        return entities


